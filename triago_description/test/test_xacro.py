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
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from triago_description.launch_arguments import TriagoArgs

from urdf_test.xacro_test import define_xacro_test
from launch.actions import DeclareLaunchArgument

xacro_file_path = Path(
    get_package_share_directory('triago_description'),
    'robots',
    'triago.urdf.xacro',
)

arm_args = (
    TriagoArgs.arm_type_right,
    TriagoArgs.arm_type_left,
    TriagoArgs.arm_type_head
)
wrist_args_left = (
    TriagoArgs.wrist_model_left,
    TriagoArgs.ft_sensor_left
)
wrist_args_right = (
    TriagoArgs.wrist_model_right,
    TriagoArgs.ft_sensor_right
)
wrist_args_head = (
    TriagoArgs.wrist_model_head,
    TriagoArgs.ft_sensor_head
)

camera_position_args = (
    TriagoArgs.camera_position_right,
    TriagoArgs.camera_position_left,
    TriagoArgs.camera_position_head
)
camera_tool_ee = DeclareLaunchArgument(
    name='camera-tools',
    choices=['camera-tools'])

no_ft_sensor_left = DeclareLaunchArgument(
    name='ft_sensor_left',
    choices=['no-ft-sensor'])

no_ft_sensor_right = DeclareLaunchArgument(
    name='ft_sensor_right',
    choices=['no-ft-sensor'])

no_ft_sensor_head = DeclareLaunchArgument(
    name='ft_sensor_head',
    choices=['no-ft-sensor'])

# Exclude Allegro Hand if needed


def exclude_allegro_hand(end_effector):
    _choices = getattr(end_effector, 'choices', None)
    _name = getattr(end_effector, 'name', None)
    filtered_choices = [c for c in _choices if 'allegro-hand' not in str(c)]
    end_effector = DeclareLaunchArgument(name=_name, choices=filtered_choices)
    return end_effector


if not os.environ.get('PAL_DISTRO'):
    end_effector_left = exclude_allegro_hand(TriagoArgs.end_effector_left)
    end_effector_right = exclude_allegro_hand(TriagoArgs.end_effector_right)
    end_effector_head = exclude_allegro_hand(TriagoArgs.end_effector_head)

    other_ee_left = DeclareLaunchArgument(
        name='end_effector_left',
        choices=['pal-pro-gripper', 'custom', 'no-end-effector'])

    other_ee_right = DeclareLaunchArgument(
        name='end_effector_right',
        choices=['pal-pro-gripper', 'custom', 'no-end-effector'])

    other_ee_head = DeclareLaunchArgument(
        name='end_effector_head',
        choices=['pal-pro-gripper', 'custom', 'no-end-effector'])

else:
    end_effector_left = TriagoArgs.end_effector_left
    end_effector_right = TriagoArgs.end_effector_right
    end_effector_head = TriagoArgs.end_effector_head

    other_ee_left = DeclareLaunchArgument(
        name='end_effector_left',
        choices=['pal-pro-gripper', 'custom', 'allegro-hand', 'no-end-effector'])

    other_ee_right = DeclareLaunchArgument(
        name='end_effector_right',
        choices=['pal-pro-gripper', 'custom', 'allegro-hand', 'no-end-effector'])

    other_ee_head = DeclareLaunchArgument(
        name='end_effector_head',
        choices=['pal-pro-gripper', 'custom', 'allegro-hand', 'no-end-effector'])

gripper_args = (
    end_effector_right,
    end_effector_left,
    end_effector_head
)


test_xacro_base = define_xacro_test(xacro_file_path, arm_args, TriagoArgs.base_type)
test_xacro_laser = define_xacro_test(xacro_file_path, arm_args, TriagoArgs.laser_model)
test_xacro_camera = define_xacro_test(xacro_file_path, arm_args, TriagoArgs.camera_model)
test_xacro_wrist_left = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_left, wrist_args_left)
test_xacro_wrist_right = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_right, wrist_args_right)
test_xacro_wrist_head = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_head, TriagoArgs.wrist_model_head, no_ft_sensor_head)

# Force no-ft-sensor to avoid incompatibility with camera-tools end effector
test_xacro_ee_left = define_xacro_test(
    xacro_file_path, end_effector_left,
    TriagoArgs.wrist_model_left, no_ft_sensor_left)
test_xacro_ee_right = define_xacro_test(
    xacro_file_path, end_effector_right,
    TriagoArgs.wrist_model_right, no_ft_sensor_right)
test_xacro_ee_head = define_xacro_test(
    xacro_file_path, end_effector_head,
    TriagoArgs.wrist_model_head, no_ft_sensor_head)

# Test with ft-sensor but without camera-tools
test_xacro_ee_left = define_xacro_test(
    xacro_file_path, other_ee_left,
    TriagoArgs.wrist_model_left, no_ft_sensor_left)
test_xacro_ee_right = define_xacro_test(
    xacro_file_path, other_ee_right,
    TriagoArgs.wrist_model_right, no_ft_sensor_right)
test_xacro_ee_head = define_xacro_test(
    xacro_file_path, other_ee_head,
    TriagoArgs.wrist_model_head, no_ft_sensor_head)

test_xacro_hand_type = define_xacro_test(
    xacro_file_path, end_effector_head, TriagoArgs.hand_head_type)

test_xacro_camera_left_ee = define_xacro_test(
    xacro_file_path, camera_tool_ee, TriagoArgs.camera_position_left)
test_xacro_camera_right_ee = define_xacro_test(
    xacro_file_path, camera_tool_ee, TriagoArgs.camera_position_right)
test_xacro_camera_head_ee = define_xacro_test(
    xacro_file_path, camera_tool_ee, TriagoArgs.camera_position_head)

test_xacro_camera_left = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_left, TriagoArgs.camera_position_left)
test_xacro_camera_right = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_right, TriagoArgs.camera_position_right)
test_xacro_camera_head = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_head, TriagoArgs.camera_position_head)

test_xacro_ee_arm = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_left, end_effector_left)
test_xacro_ee_arm = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_right, end_effector_right)
test_xacro_ee_arm = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_head, TriagoArgs.end_effector_head)
