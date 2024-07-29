cmake_minimum_required(VERSION 3.8)
project(triago_description)

find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()

if(pal_module_cmake_FOUND)
  pal_register_modules(
    module/10_robot_state_publisher.yaml
  )
endif()


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  foreach(arm_type_left triago no-arm)
    foreach(arm_type_right triago no-arm)
      foreach(arm_type_head triago no-arm)      
        foreach(end_effector_left pal-pro-gripper custom no-end-effector)
            foreach(end_effector_right pal-pro-gripper custom no-end-effector)
              foreach(end_effector_head pal-pro-gripper custom no-end-effector)
                foreach(ft_sensor_left no-ft-sensor ati-mini45)
                    foreach(ft_sensor_right no-ft-sensor ati-mini45)
                      foreach(ft_sensor_head no-ft-sensor ati-mini45)

                          set(left_side "${arm_type_left}_${end_effector_left}_${ft_sensor_left}")
                          set(right_side "${arm_type_right}_${end_effector_right}_${ft_sensor_right}")
                          set(head_side "${arm_type_head}_${end_effector_head}_${ft_sensor_head}")
  
                          add_launch_test(
                            test/test_description.launch.py
                            TARGET "triago_description_${left_side}_${right_side}_${head_side}"
                            ARGS
                            "arm_type_left:=${arm_type_left}"
                            "arm_type_right:=${arm_type_right}"
                            "arm_type_head:=${arm_type_head}"
                            "end_effector_left:=${end_effector_left}"
                            "end_effector_right:=${end_effector_right}"
                            "end_effector_head:=${end_effector_head}"
                            "ft_sensor_left:=${ft_sensor_left}"
                            "ft_sensor_right:=${ft_sensor_right}"
                            "ft_sensor_head:=${ft_sensor_head}"
                          )
                          endforeach()
                        endforeach()
                      endforeach()
                    endforeach()
                endforeach()
            endforeach()
        endforeach()
      endforeach()
    endforeach()
  foreach(laser_model no-laser sick-571)
    add_launch_test(
      test/test_description.launch.py
      TARGET "triago_description_${laser_model}"
      ARGS "laser_model:=${laser_model}"
    )
  endforeach()
endif()

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config launch robots meshes ros2_control urdf)
