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
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.conditions import LaunchConfigurationNotEquals
from launch_pal import get_pal_configuration

from launch_pal.arg_utils import LaunchArgumentsBase
from triago_description.launch_arguments import TriagoArgs

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    arm_type_right: DeclareLaunchArgument = TriagoArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TriagoArgs.arm_type_left
    arm_type_head: DeclareLaunchArgument = TriagoArgs.arm_type_head
    end_effector_right: DeclareLaunchArgument = TriagoArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TriagoArgs.end_effector_left
    end_effector_head: DeclareLaunchArgument = TriagoArgs.end_effector_head

    cmd_vel: DeclareLaunchArgument = DeclareLaunchArgument(
        name='cmd_vel',
        default_value='input_joy/cmd_vel',
        description='Joystick cmd_vel topic')


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    # PAL helper function to fetch the configuration for this package,
    # which might be installed also from other packages
    joy_teleop_config = get_pal_configuration(
        pkg="joy_teleop",
        node="joy_teleop",
        ld=launch_description)

    joy_teleop_node = Node(
        package='joy_teleop',
        executable='joy_teleop',
        parameters=joy_teleop_config['parameters'],
        remappings=joy_teleop_config['remappings'],)

    launch_description.add_action(joy_teleop_node)

    joy_config = get_pal_configuration(
        pkg="joystick",
        node="joystick",
        ld=launch_description)

    joy_node = Node(
        package='pal_joy',
        executable='game_controller_node',
        name='joystick',
        parameters=joy_config['parameters'])

    launch_description.add_action(joy_node)

    pkg_dir = get_package_share_directory('triago_bringup')

    joystick_analyzer = Node(
        package='diagnostic_aggregator',
        executable='add_analyzer',
        namespace='joystick',
        output='screen',
        emulate_tty=True,
        parameters=[
            os.path.join(pkg_dir, 'config', 'joy_teleop', 'joystick_analyzers.yaml')
        ],
    )
    launch_description.add_action(joystick_analyzer)

    torso_incrementer_server = Node(
        package='joy_teleop',
        executable='incrementer_server',
        name='incrementer',
        namespace='torso_controller')

    launch_description.add_action(torso_incrementer_server)

    gripper_incrementer_server_right = Node(
        package='joy_teleop',
        executable='incrementer_server',
        name='incrementer_right',
        namespace='gripper_right_controller',
        condition=LaunchConfigurationNotEquals('end_effector_right', 'no-end-effector'))

    launch_description.add_action(gripper_incrementer_server_right)

    gripper_incrementer_server_left = Node(
        package='joy_teleop',
        executable='incrementer_server',
        name='incrementer_left',
        namespace='gripper_left_controller',
        condition=LaunchConfigurationNotEquals('end_effector_left', 'no-end-effector'))

    launch_description.add_action(gripper_incrementer_server_left)

    return


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
