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

from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from triago_description.launch_arguments import TriagoArgs

from urdf_test.xacro_test import define_xacro_test

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
gripper_args = (
    TriagoArgs.end_effector_right,
    TriagoArgs.end_effector_left,
    TriagoArgs.end_effector_head
)
camera_position_args = (
    TriagoArgs.camera_position_right,
    TriagoArgs.camera_position_left,
    TriagoArgs.camera_position_head
)

test_xacro_base = define_xacro_test(xacro_file_path, arm_args, TriagoArgs.base_type)
test_xacro_laser = define_xacro_test(xacro_file_path, arm_args, TriagoArgs.laser_model)
test_xacro_camera = define_xacro_test(xacro_file_path, arm_args, TriagoArgs.camera_model)
test_xacro_wrist_left = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_left, wrist_args_left)
test_xacro_wrist_right = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_right, wrist_args_right)
test_xacro_wrist_head = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_head, wrist_args_head)

test_xacro_ee_left = define_xacro_test(
    xacro_file_path, TriagoArgs.end_effector_left, wrist_args_left)
test_xacro_ee_right = define_xacro_test(
    xacro_file_path, TriagoArgs.end_effector_right, wrist_args_right)
test_xacro_ee_head = define_xacro_test(
    xacro_file_path, TriagoArgs.end_effector_head, wrist_args_head)

test_xacro_hand_type = define_xacro_test(
    xacro_file_path, TriagoArgs.end_effector_head, TriagoArgs.hand_head_type)

test_xacro_camera_left = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_left, TriagoArgs.camera_position_left)
test_xacro_camera_right = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_right, TriagoArgs.camera_position_right)
test_xacro_camera_head = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_head, TriagoArgs.camera_position_head)

test_xacro_ee_arm = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_left, TriagoArgs.end_effector_left)
test_xacro_ee_arm = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_right, TriagoArgs.end_effector_right)
test_xacro_ee_arm = define_xacro_test(
    xacro_file_path, TriagoArgs.arm_type_head, TriagoArgs.end_effector_head)
