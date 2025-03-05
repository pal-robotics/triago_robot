# TSID controllers

## Prerequisites

The following packages and branches are required to load the TSID controllers on the TIAGo Pro or TRIAGo.
They are universal for simulation and the real robot. They need to be deployed on the robot.

- tsid_framework: branch dtk/release-tsid
- triago_robot: dtk/tsid
- tiago_pro_robot: branch dtk/tsid



## How to load

The launch ``tsid_default_controllers`` loads the TSID controllers. The parameter files of the controllers are equal
for each arm, using variables inside the yaml file, such as ``${ARM_SIDE_PREFIX}``, to reduce boilerplate. The ``use_sim_time``
arg is used when the gains of the joints are different between simulation and the robot.


```bash
# Tiago pro contains an identical launch file launching the TSID controllers
ros2 launch triago_controller_configuration tsid_default_controllers.launch.py [use_sim_time:=True]
```

After launching the file the TSID controllers are loaded and set to inactive, as shown below.

``` bash

$ ros2 control list_controllers
arm_left_sin_joint_controller      tsid_controllers/SinJointSpaceController               inactive
head_controller                    joint_trajectory_controller/JointTrajectoryController  active  
arm_right_joint_space_controller   tsid_controllers/JointSpaceTsidController              active  
imu_sensor_broadcaster             imu_sensor_broadcaster/IMUSensorBroadcaster            active  
gripper_left_controller            joint_trajectory_controller/JointTrajectoryController  active  
arm_left_controller                joint_trajectory_controller/JointTrajectoryController  active  
joint_state_broadcaster            joint_state_broadcaster/JointStateBroadcaster          active  
gravity_compensation_controller    pal_controllers/GravityCompensationController          inactive
torso_controller                   joint_trajectory_controller/JointTrajectoryController  active  
arm_right_cartesian_vel_controller tsid_controllers/CartesianVelocityController           inactive
arm_left_joint_space_controller    tsid_controllers/JointSpaceTsidController              inactive
arm_right_controller               joint_trajectory_controller/JointTrajectoryController  inactive
arm_left_cartesian_vel_controller  tsid_controllers/CartesianVelocityController           inactive
gripper_right_controller           joint_trajectory_controller/JointTrajectoryController  active  
arm_right_sin_joint_controller     tsid_controllers/SinJointSpaceController               inactive

```

Individual controllers can be activated with the following commands:

```bash
ros2 control switch_controllers --activate arm_right_joint_space_controller --deactivate arm_right_controller
```

Please note that this launch structure has only been tested in simulation, not all controllers are loaded properly yet.

## module

Both TIAGo Pro and TRIAGo will contain a module to load the TSID controllers.
However, the use of these modules still require testing.