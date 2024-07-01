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

endif()

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config launch gazebo robots meshes ros2_control urdf)
