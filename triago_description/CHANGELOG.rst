^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package triago_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.4 (2024-10-02)
------------------
* Merge branch 'vmo/fix_modules' into 'humble-devel'
  Checking all modules
  See merge request robots/triago_robot!10
* Adding description module
* Merge branch 'tpe/fix_wrist' into 'humble-devel'
  Fix wrist + update joint 6 limit + update motions
  See merge request robots/triago_robot!11
* Fix wrist + update joint 6 limit + update motions
* Merge branch 'vmo/fix_pro_gripper' into 'humble-devel'
  Adding pro gripper control
  See merge request robots/triago_robot!9
* Adding pro gripper control
* Merge branch 'vmo/fix_head' into 'humble-devel'
  Adjust config head
  See merge request robots/triago_robot!8
* Adjus tool_changer
* Adjus tool_changer
* Adjust config head
* Contributors: thomas.peyrucain, thomaspeyrucain, vivianamorlando

0.12.5 (2025-05-08)
-------------------
* Enable error_protection
* Contributors: Jordan Palacios

0.12.4 (2025-04-30)
-------------------

0.12.3 (2025-04-25)
-------------------

0.12.2 (2025-04-23)
-------------------

0.12.1 (2025-04-11)
-------------------

0.12.0 (2025-04-11)
-------------------

0.11.0 (2025-04-10)
-------------------

0.10.0 (2025-04-10)
-------------------

0.9.0 (2025-04-10)
------------------
* Add torso_imu_link
* Rename hardware component to match ros2_control imu
* Add ros2 control imu in the proper hardware component
* Adding Orientus ros2_control sensor
* Revert "Remove unused imu and broadcaster"
  This reverts commit 6e49701ec3db1b9231af05d5c39953453b1441e0.
* Contributors: Jordan Palacios, Noel Jimenez, thomas.peyrucain

0.8.3 (2025-04-08)
------------------

0.8.2 (2025-04-04)
------------------
* add no-camera choice for camera_model
* Contributors: ileniaperrella

0.8.1 (2025-04-03)
------------------
* Add has_torque_estimation
* Add arm type tiago-pro-s
* Contributors: David ter Kuile

0.8.0 (2025-03-25)
------------------

0.7.1 (2025-03-19)
------------------
* Remove unused imu and broadcaster
* Contributors: Noel Jimenez

0.7.0 (2025-03-12)
------------------

0.6.1 (2025-03-11)
------------------

0.6.0 (2025-03-10)
------------------

0.5.0 (2025-03-04)
------------------
* update max velocity for the torso lift
* Contributors: ileniaperrella

0.4.0 (2025-02-26)
------------------
* expose velocity interface for torso joint
* Remove __pycache\_\_
* Modify tests to match new behavior
* Set ft_sensor_head default value to no-ft-sensor to match xacro
* Handle properly invalid simultaneous camera-tools and ft sensor
* Fix side on ros2_control for allegro
* Add side as an argument for xela
* Contributors: Aina, Noel Jimenez, ileniaperrella

0.3.2 (2025-02-05)
------------------
* Use ft_sensor suffix for force-torque sensor name
* Fix how to send variables on xacro and macro call
* Contributors: Aina, Noel Jimenez

0.3.1 (2025-01-23)
------------------
* Merge branch 'tpe/simplify_3d_models' into 'humble-devel'
  Tpe/simplify 3d models
  See merge request robots/triago_robot!45
* Change back to collision model
* Contributors: thomas.peyrucain, vivianamorlando

0.3.0 (2025-01-22)
------------------

0.2.2 (2025-01-21)
------------------
* Merge branch 'tpe/simplify_3d_models' into 'humble-devel'
  Add simplify models + remove unecessary models
  See merge request robots/triago_robot!42
* Remove straight wrist option
* Add simplify models + remove unecessary models
* Merge branch 'air/feat/allegro_ros2control' into 'humble-devel'
  Allegro ros2control
  See merge request robots/triago_robot!43
* Add allegro hand ros2 control macro for simulation
* Contributors: Aina, thomas.peyrucain, vivianamorlando

0.2.1 (2025-01-20)
------------------
* Merge branch 'vmo/fix_collision' into 'humble-devel'
  Removing collision arm 7 link
  See merge request robots/triago_robot!40
* Adding simplified mesh
* Removing collision arm 7 link
* Contributors: vivianamorlando

0.2.0 (2025-01-13)
------------------
* Remove unnecessary variable for can
* Add macro for allegro hand system and xela
* Add head end effector allegro hand and remove comments
* Add allegro hand as different system
* Contributors: Aina

0.1.1 (2024-11-20)
------------------

0.1.0 (2024-11-04)
------------------
* Add ee camera tool test
* Fix path for urdf to triago.urdf
* Add xacro tests
* Contributors: Aina

0.0.9 (2024-10-24)
------------------
* Merge branch 'vmo/camera_model' into 'humble-devel'
  Modifying the camera model
  See merge request robots/triago_robot!32
* Modifying the camera model
* Contributors: vivianamorlando

0.0.8 (2024-10-21)
------------------
* Merge branch 'tpe/fix_joint_limit' into 'humble-devel'
  fix joint limit deleting the safety threshold
  See merge request robots/triago_robot!31
* fix joint limit deleting the safety threshold
* Add correct mesh for head arm
* Add posibility of having 3 cameras at the same time
* Add camera position as an argument
* Revert inertias
* Merge branch 'air/feat/head-no-ee' into 'humble-devel'
  Fix no-ee by default
  See merge request robots/triago_robot!29
* Fix no-ee by default
* Merge branch 'air/fix/vel_limits' into 'humble-devel'
  Air/fix/vel limits
  See merge request robots/triago_robot!28
* Fix vel in urdf
* Contributors: Aina, ileniaperrella, thomaspeyrucain, vivianamorlando

0.0.7 (2024-10-10)
------------------
* Merge branch 'tpe/fix_inertia_wrist' into 'humble-devel'
  Fix wrist inertia
  See merge request robots/triago_robot!24
* Fix wrist inertia
* Merge branch 'tpe/update-vel-lim' into 'humble-devel'
  update joint max velocity limit for tiago head arm
  See merge request robots/triago_robot!26
* update joint max velocity limit for tiago head arm
* Merge branch 'tpe/fix_5th_joint_reflect' into 'humble-devel'
  Add reflect on the 5th joint
  See merge request robots/triago_robot!22
* Add reflect on the 5th joint
* reduce joint limits according to test with robot
* Lift torso_lift link of 5mm because a part was added to prevent collsion due the the 3rd arm + modify range of torso_lift
* Merge branch 'abr/fix/use-omni-base-controller' into 'humble-devel'
  Use omni_base mobile_base_controller
  See merge request robots/triago_robot!17
* Fix inertias
* Fix inertias
* Merge branch 'tpe/fix_joint_6' into 'humble-devel'
  Inverse joint 6 rotation + update motions accordingly
  See merge request robots/triago_robot!15
* Change joint 3 limits to match real configuration
* Modify coupler path
* Revert hand to not be bothered by the wrist while grasping objects
* Add missing coupler link for the allegro hand
* add material + fix 7th joint
* Flip 1st joint for the head + adapt motions
* Inverse joint 6 rotation + update motions accordingly
* Merge branch 'feat/multiple_hardware_components' into 'humble-devel'
  Split ros2_control hardware into two RobotControl components
  See merge request robots/triago_robot!13
* Split ros2_control hardware into two RobotControl components
* Merge branch 'fix/arm_head_offset' into 'humble-devel'
  Use arm_head_offset for arm_head
  See merge request robots/triago_robot!12
* Use arm_head_offset for arm_head
* Contributors: Aina, Noel Jimenez, thomas.peyrucain, thomaspeyrucain, vivianamorlando

0.0.6 (2024-10-02)
------------------

0.0.3 (2024-09-30)
------------------
* Merge branch 'vmo/adapting_arm' into 'humble-devel'
  Vmo/adapting arm
  See merge request robots/triago_robot!7
* Adapting to the arm!
* Contributors: vivianamorlando

0.0.2 (2024-09-27)
------------------
