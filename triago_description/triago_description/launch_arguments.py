# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
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


from dataclasses import dataclass
from launch.actions import DeclareLaunchArgument as DLA
from launch_pal.arg_utils import parse_launch_args_from_yaml
from ament_index_python.packages import get_package_share_directory


@dataclass(frozen=True)
class TriagoArgs:
    """This dataclass contains launch arguments for TRIAGo."""

    __robot_name = 'triago'
    __pkg_dir = get_package_share_directory(f"{__robot_name}_description")
    __arg_creator = parse_launch_args_from_yaml(
        f"{__pkg_dir}/config/{__robot_name}_configuration.yaml")

    base_type: DLA = __arg_creator.get_argument("base_type")
    arm_type_right: DLA = __arg_creator.get_argument("arm_type_right")
    arm_type_left: DLA = __arg_creator.get_argument("arm_type_left")
    arm_type_head: DLA = __arg_creator.get_argument("arm_type_head")
    wrist_model_right: DLA = __arg_creator.get_argument("wrist_model_right")
    wrist_model_left: DLA = __arg_creator.get_argument("wrist_model_left")
    wrist_model_head: DLA = __arg_creator.get_argument("wrist_model_head")
    end_effector_right: DLA = __arg_creator.get_argument("end_effector_right")
    end_effector_left: DLA = __arg_creator.get_argument("end_effector_left")
    end_effector_head: DLA = __arg_creator.get_argument("end_effector_head")
    hand_head_type: DLA = __arg_creator.get_argument("hand_head_type")
    ft_sensor_right: DLA = __arg_creator.get_argument("ft_sensor_right")
    ft_sensor_left: DLA = __arg_creator.get_argument("ft_sensor_left")
    ft_sensor_head: DLA = __arg_creator.get_argument("ft_sensor_head")
    camera_model: DLA = __arg_creator.get_argument("camera_model")
    laser_model: DLA = __arg_creator.get_argument("laser_model")
    torque_estimation: DLA = __arg_creator.get_argument("torque_estimation")
    camera_position_right: DLA = __arg_creator.get_argument("camera_position_right")
    camera_position_left: DLA = __arg_creator.get_argument("camera_position_left")
    camera_position_head: DLA = __arg_creator.get_argument("camera_position_head")
    camera_right: DLA = __arg_creator.get_argument("camera_right")
    camera_left: DLA = __arg_creator.get_argument("camera_left")
    camera_head: DLA = __arg_creator.get_argument("camera_head")
