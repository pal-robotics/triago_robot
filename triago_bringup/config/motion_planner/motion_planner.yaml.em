/**:
  ros__parameters:
    motion_planner:
      disable_motion_planning: false
      planning_groups: # Sorted by order of preference
        - all_arms_torso

      joint_tolerance: 0.01

      #TO DO: Add exclude_from_planning_joints for end effectors


      # Parameters for non-planned approach
      approach_velocity: 0.5
      approach_min_duration: 0.5
