from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("abb_crb15000_5_95", package_name="crb15000_5_95_moveit_config").planning_pipelines(pipelines=["ompl", "pilz_industrial_motion_planner"]).trajectory_execution(file_path="config/moveit_controllers.yaml").to_moveit_configs()
    return generate_move_group_launch(moveit_config)
