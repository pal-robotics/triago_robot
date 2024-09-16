# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration, OpaqueFunction

from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.robot_arguments import CommonArgs

from triago_description.launch_arguments import TriagoArgs
from triago_description.triago_launch_utils import get_triago_hw_suffix
from launch_pal.param_utils import merge_param_files
from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    arm_type_right: DeclareLaunchArgument = TriagoArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TriagoArgs.arm_type_left
    arm_type_head: DeclareLaunchArgument = TriagoArgs.arm_type_head
    end_effector_right: DeclareLaunchArgument = TriagoArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TriagoArgs.end_effector_left
    end_effector_head: DeclareLaunchArgument = TriagoArgs.end_effector_head
    hand_head_type: DeclareLaunchArgument = TriagoArgs.hand_head_type

    use_sim_time:  DeclareLaunchArgument = CommonArgs.use_sim_time


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):
    play_motion2 = include_scoped_launch_py_description(
        pkg_name='play_motion2',
        paths=['launch', 'play_motion2.launch.py'],
        launch_arguments={
            "use_sim_time":  launch_args.use_sim_time,
            "motions_file": LaunchConfiguration('motions_file'),
            'motion_planner_config': LaunchConfiguration('motion_planner_config')
        })

    launch_description.add_action(OpaqueFunction(
        function=create_play_motion_filename))
    launch_description.add_action(play_motion2)

    return


def create_play_motion_filename(context):

    pkg_name = 'triago_bringup'
    pkg_share_dir = get_package_share_directory(pkg_name)

    hw_suffix = get_triago_hw_suffix(
        arm_right=read_launch_argument('arm_type_right', context),
        arm_left=read_launch_argument('arm_type_left', context),
        arm_head=read_launch_argument('arm_type_head', context),
        end_effector_right=read_launch_argument('end_effector_right', context),
        end_effector_left=read_launch_argument('end_effector_left', context),
        end_effector_head=read_launch_argument('end_effector_head', context),
    )

    arm_right=read_launch_argument('arm_type_right', context)
    arm_left=read_launch_argument('arm_type_left', context)
    arm_head=read_launch_argument('arm_type_head', context)
    end_effector_right=read_launch_argument('end_effector_right', context)
    end_effector_left=read_launch_argument('end_effector_left', context)
    end_effector_head=read_launch_argument('end_effector_head', context)
    
    motions_folder = os.path.join(pkg_share_dir, 'config', 'motions')
    base_motions_file = 'tiago_pro_motions_no_arms.yaml'
    if arm_right != 'no-arm'  and arm_left != 'no-arm' and arm_head != 'no-arm':
        base_motions_file = 'triago_motions_general.yaml'

    elif arm_right == 'no-arm'  and arm_left != 'no-arm' and arm_head != 'no-arm':
        base_motions_file = 'triago_motions_general_arm_left_arm_head.yaml'

    elif arm_left == 'no-arm' and arm_right != 'no-arm' and arm_head != 'no-arm':
        base_motions_file = 'triago_motions_general_arm_right_arm_head.yaml'

    elif arm_head == 'no-arm' and arm_right != 'no-arm' and arm_left != 'no-arm' :
        base_motions_file = 'triago_motions_general_arm_left_arm_right.yaml'

    elif arm_head == 'no-arm' and arm_right == 'no-arm' and arm_left != 'no-arm' :
        base_motions_file = 'triago_motions_general_arm_left.yaml'   
    
    elif arm_right == 'no-arm'  and arm_left == 'no-arm' and arm_head != 'no-arm':
        base_motions_file = 'triago_motions_general_arm_head.yaml'

    elif arm_left == 'no-arm' and arm_head == 'no-arm' and arm_right != 'no-arm':
        base_motions_file = 'triago_motions_general_arm_right.yaml'
    


    base_motions_yaml = PathJoinSubstitution(
        [pkg_share_dir, 'config', 'motions', base_motions_file])

    motion_files = [base_motions_file]

    motion_yamls = [os.path.join(motions_folder, f) for f in motion_files]
    combined_yaml = merge_param_files(motion_yamls)
    # combined_yaml = merge_param_files(
    #     [base_motions_yaml.perform(context), hw_config_specific_yaml.perform(context)])

    motion_planner_file = f"motion_planner{hw_suffix}.yaml"
    motion_planner_config = PathJoinSubstitution([
        pkg_share_dir,
        'config', 'motion_planner', motion_planner_file])

    return [SetLaunchConfiguration("motions_file", combined_yaml),
            SetLaunchConfiguration("motion_planner_config", motion_planner_config)]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
