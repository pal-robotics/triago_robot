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


from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration

from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.robot_arguments import CommonArgs
from triago_description.launch_arguments import TriagoArgs

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    base_type: DeclareLaunchArgument = TriagoArgs.base_type
    arm_type_right: DeclareLaunchArgument = TriagoArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TriagoArgs.arm_type_left
    arm_type_head: DeclareLaunchArgument = TriagoArgs.arm_type_head
    end_effector_right: DeclareLaunchArgument = TriagoArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TriagoArgs.end_effector_left
    end_effector_head: DeclareLaunchArgument = TriagoArgs.end_effector_head
    hand_head_type: DeclareLaunchArgument = TriagoArgs.hand_head_type
    ft_sensor_right: DeclareLaunchArgument = TriagoArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = TriagoArgs.ft_sensor_left
    ft_sensor_head: DeclareLaunchArgument = TriagoArgs.ft_sensor_head
    wrist_model_right: DeclareLaunchArgument = TriagoArgs.wrist_model_right
    wrist_model_left: DeclareLaunchArgument = TriagoArgs.wrist_model_left
    camera_position_right: DeclareLaunchArgument = TriagoArgs.camera_position_right
    camera_position_left: DeclareLaunchArgument = TriagoArgs.camera_position_left
    camera_position_head: DeclareLaunchArgument = TriagoArgs.camera_position_head
    wrist_model_head: DeclareLaunchArgument = TriagoArgs.wrist_model_head
    camera_model: DeclareLaunchArgument = TriagoArgs.camera_model
    laser_model: DeclareLaunchArgument = TriagoArgs.laser_model
    torque_estimation: DeclareLaunchArgument = TriagoArgs.torque_estimation
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    namespace: DeclareLaunchArgument = CommonArgs.namespace


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    robot_state_publisher = include_scoped_launch_py_description(
        pkg_name='triago_description',
        paths=['launch', 'robot_state_publisher.launch.py'],
        launch_arguments={'arm_type_right': launch_args.arm_type_right,
                          'arm_type_left': launch_args.arm_type_left,
                          'arm_type_head': launch_args.arm_type_head,
                          "end_effector_right": launch_args.end_effector_right,
                          "end_effector_left": launch_args.end_effector_left,
                          "end_effector_head": launch_args.end_effector_head,
                          "ft_sensor_right": launch_args.ft_sensor_right,
                          "ft_sensor_left": launch_args.ft_sensor_left,
                          "ft_sensor_head": launch_args.ft_sensor_head,
                          "wrist_model_right": launch_args.wrist_model_right,
                          "wrist_model_left": launch_args.wrist_model_left,
                          "wrist_model_head": launch_args.wrist_model_head,
                          "laser_model": launch_args.laser_model,
                          "camera_model": launch_args.camera_model,
                          "base_type": launch_args.base_type,
                          "namespace": launch_args.namespace,
                          'torque_estimation': launch_args.torque_estimation,
                          "use_sim_time": launch_args.use_sim_time,
                          "camera_position_right": launch_args.camera_position_right,
                          "camera_position_left": launch_args.camera_position_left,
                          "camera_position_head": launch_args.camera_position_head
                          })

    launch_description.add_action(robot_state_publisher)

    joint_state_pub_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen')

    launch_description.add_action(joint_state_pub_gui)

    rviz_config_file = PathJoinSubstitution([FindPackageShare('triago_description'), 'config',
                                            'show.rviz'])
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen',
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')
                     }])
    launch_description.add_action(rviz)

    return


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
