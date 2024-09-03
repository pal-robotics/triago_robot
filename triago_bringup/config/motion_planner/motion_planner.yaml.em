/play_motion2:
  ros__parameters:
    motion_planner:
      disable_motion_planning: false
      planning_groups: # Sorted by order of preference
@[if has_arm_left]@
        - arm_left_torso
        - arm_left
@[end if]@
@[if has_arm_right]@
        - arm_right_torso
        - arm_right
@[end if]@
@[if has_arm_head]@
        - arm_head_torso
        - arm_head
@[end if]@
@[if has_arm_left and has_arm_right and has_arm_head]@
        - all_arms_torso
@[end if]@
        - torso
      joint_tolerance: 0.01

      # Parameters for non-planned approach
      approach_velocity: 0.5
      approach_min_duration: 0.5
