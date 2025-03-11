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
