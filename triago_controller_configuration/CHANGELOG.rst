^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package triago_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.4 (2024-10-02)
------------------
* Merge branch 'vmo/fix_modules' into 'humble-devel'
  Checking all modules
  See merge request robots/triago_robot!10
* Checking all modules
* Merge branch 'vmo/fix_pro_gripper' into 'humble-devel'
  Adding pro gripper control
  See merge request robots/triago_robot!9
* Adding pro gripper control
* Contributors: thomaspeyrucain, vivianamorlando

Forthcoming
-----------
* Fix relative pose in ee control
* Contributors: vivianamorlando

0.17.1 (2025-09-05)
-------------------
* Merge branch 'vmo/remove_tolerance' into 'humble-devel'
  Removing tolerance for torso
  See merge request robots/triago_robot!96
* Removing tolerance for torso
* Contributors: ileniaperrella, vivianamorlando

0.17.0 (2025-07-10)
-------------------
* Add diagnostic analyzers
* Contributors: Noel Jimenez

0.16.0 (2025-07-09)
-------------------

0.15.0 (2025-06-18)
-------------------

0.14.0 (2025-06-05)
-------------------

0.13.3 (2025-06-05)
-------------------

0.13.2 (2025-06-05)
-------------------

0.13.1 (2025-06-04)
-------------------
* Adding conditions to launch the broadcaster properly
* Contributors: oscarmartinez

0.13.0 (2025-05-29)
-------------------
* Launching sea broadcaster controller
* Contributors: oscarmartinez

0.12.7 (2025-05-28)
-------------------
* reduce torso trajectory tolerance to 1cm
* update torso controller with trajectory constraint
* Contributors: ileniaperrella

0.12.6 (2025-05-21)
-------------------
* Adding config file for cartesian vel in local frame
* Contributors: vivianamorlando

0.12.5 (2025-05-08)
-------------------

0.12.4 (2025-04-30)
-------------------
* force controllers spawned inactive
* fixed condition and names
* added cartesian force controllers for left and right
* Contributors: Daniel Costanzi

0.12.3 (2025-04-25)
-------------------
* Merge branch 'dtk/tsid' into 'humble-devel'
  Dtk/tsid
  See merge request robots/triago_robot!78
* set ad default the cube for each arm
* update common cube
* update manipulation cube
* Contributors: ileniaperrella

0.12.2 (2025-04-23)
-------------------

0.12.1 (2025-04-11)
-------------------
* increase manipulation cube for the cartesian vel
* Contributors: ileniaperrella

0.12.0 (2025-04-11)
-------------------

0.11.0 (2025-04-10)
-------------------
* fix default launch file for tsid
* fix gains and add manipulation cube
* update x of the manipulation cube
* update gains for joint_space_controller_vel
* update gains for cartesian_vel_controller
* remove torso_lift_joint for cartesian controller
* update manipulation cube
* update cartesian gains
* fix gains and launch file for torso controller
* add manipulation cube in the yaml files
* fix cartesian gain
* Fixing controller names
* Fix gain for cartesian controller
* Fixing gains
* set string for use_sim_time as true
* add torso spawn controller + fix gains / sim gains
* add cartesian_controllers for ee frame and robot frame
* fix namespaces
* update gains for tsid controllers
* Fix typo in module
* Add tsid controllers dependency
* Rename torso param files
* Add tsid controllers module
* Add launch file to load tsid controllers
* Add tsid controller param files, templated
* Contributors: David ter Kuile, ileniaperrella, vivianamorlando

0.10.0 (2025-04-10)
-------------------
* Added mechanism to also launch the torque gravity compensation
* Launching the inertia shaping controllers if torque_estimation enabled
* Contributors: oscarmartinez

0.9.0 (2025-04-10)
------------------
* Update controller name in launchfile
* Add torso_imu_link
* Add imu_sensor_broadcaster dependency
* Revert "Remove unused imu and broadcaster"
  This reverts commit 6e49701ec3db1b9231af05d5c39953453b1441e0.
* Contributors: Jordan Palacios, Noel Jimenez, thomas.peyrucain

0.8.3 (2025-04-08)
------------------
* Add use sim time for allegro controller on simulation
* Contributors: Aina

0.8.2 (2025-04-04)
------------------
* remove unused files and change gravity compensation
* restructure default controllers
* Contributors: David ter Kuile

0.8.1 (2025-04-03)
------------------
* Add has_torque_estimation
* Contributors: David ter Kuile

0.8.0 (2025-03-25)
------------------

0.7.1 (2025-03-19)
------------------
* Remove unused imu and broadcaster
* Contributors: Noel Jimenez

0.7.0 (2025-03-12)
------------------
* Adding separate gravity controller for each arm
* Contributors: vivianamorlando

0.6.1 (2025-03-11)
------------------
* Add xela and allegro controller dependencies
* Contributors: Aina

0.6.0 (2025-03-10)
------------------
* Remove TODO for handling optional xela
* Xela controller simplification
* Add xela configuration dependency
* Preparation fot using xela condition
* Pass the cfg to the xela package
* Add xela broadcaster configuration
* Contributors: Isaac Acevedo

0.5.0 (2025-03-04)
------------------

0.4.0 (2025-02-26)
------------------
* Use libhand as default controller
* Contributors: Aina

0.3.2 (2025-02-05)
------------------
* Fix capital letter
* Contributors: Aina

0.3.1 (2025-01-23)
------------------

0.3.0 (2025-01-22)
------------------

0.2.2 (2025-01-21)
------------------
* Merge branch 'air/feat/allegro_ros2control' into 'humble-devel'
  Allegro ros2control
  See merge request robots/triago_robot!43
* Add head arguments for controllers
* Add allegro hand ros2 control macro for simulation
* Contributors: Aina, vivianamorlando

0.2.1 (2025-01-20)
------------------

0.2.0 (2025-01-13)
------------------
* Add allegro hand as different system
* Contributors: Aina

0.1.1 (2024-11-20)
------------------
* Merge branch 'abr/fix/triago-cmd-vel' into 'humble-devel'
  passing is_public_sim to mobile_base_controller
  See merge request robots/triago_robot!36
* passing is_public_sim to mobile_base_controller
* Contributors: antoniobrandi, vivianamorlando

0.1.0 (2024-11-04)
------------------
* Set update_rate for joint_state_broadcaster
* Contributors: Noel Jimenez

0.0.9 (2024-10-24)
------------------

0.0.8 (2024-10-21)
------------------
* Merge branch 'tpe/fix_joint_limit' into 'humble-devel'
  fix joint limit deleting the safety threshold
  See merge request robots/triago_robot!31
* Remove print for end_effector
* Add camera position as an argument
* Contributors: Aina, thomaspeyrucain

0.0.7 (2024-10-10)
------------------
* Merge branch 'vmo/add_open_loop' into 'humble-devel'
  Adding open loop control to jt
  See merge request robots/triago_robot!27
* Adding open loop control to jt
* Merge branch 'air/feat/merge_arm_controllers' into 'humble-devel'
  Air/feat/merge arm controllers
  See merge request robots/triago_robot!23
* Fix flake8
* Merge the 3 arm controllers
* Merge branch 'ipe/add-gravity' into 'humble-devel'
  Ipe/add gravity
  See merge request robots/triago_robot!18
* Fix flake 8
* delete condition on the gravity controller
* fix typo for use_sim_time
* add gravity compensation as default (only loaded)
* update motor torque constants with datasheet values
* Add gravity dependency
* add gravity compensation controller
* Merge branch 'ipe/fix/module-arms' into 'humble-devel'
  Ipe/fix/module arms
  See merge request robots/triago_robot!16
* Fix flake8 for launch file
* delete if sim condition on the arm position ctrl
* Update triago_controller_configuration/module/20_default_controllers.yaml
* Merge branch 'vmo/add_depend' into 'humble-devel'
  Adding dependency
  See merge request robots/triago_robot!20
* Adding dependency
* Merge branch 'abr/fix/use-omni-base-controller' into 'humble-devel'
  Use omni_base mobile_base_controller
  See merge request robots/triago_robot!17
* removed unused variables
* suggestions
* remove public_sim
* Use omni_base mobile_base_controller
* Contributors: Aina, antoniobrandi, ileniaperrella, martinaannicelli, thomas.peyrucain, thomaspeyrucain, vivianamorlando

0.0.6 (2024-10-02)
------------------

0.0.3 (2024-09-30)
------------------
* Merge branch 'vmo/adapting_arm' into 'humble-devel'
  Vmo/adapting arm
  See merge request robots/triago_robot!7
* Fix indent
* Adapting to the arm!
* Contributors: vivianamorlando

0.0.2 (2024-09-27)
------------------
