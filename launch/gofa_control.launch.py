from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription,ExecuteProcess, DeclareLaunchArgument 
from launch_ros.substitutions import FindPackageShare
from launch.actions import GroupAction, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
import os
import xacro

def generate_launch_description():

    declared_arguments = []

    declared_arguments.append(
        DeclareLaunchArgument(
            "use_fake_hardware",
            default_value="false",
            description="use simulated or real robot. ",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "rws_ip",
            default_value="192.168.125.1",
            description="use simulated or real robot. ",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "rws_port",
            default_value="443",
            description="use simulated or real robot. ",
        )
    )

    use_fake_hardware = LaunchConfiguration("use_fake_hardware")
    rws_ip = LaunchConfiguration("rws_ip")
    rws_port = LaunchConfiguration("rws_port")


    include_launcher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('abb_bringup'),'launch', 'abb_control.launch.py')),
        launch_arguments = {
            'description_package': 'abb_crb15000_support',
            'description_file': 'crb15000_5_95.xacro',
            'launch_rviz': 'false',
            'use_fake_hardware': use_fake_hardware,
            'rws_ip': rws_ip,
            'rws_port': rws_port,
            'moveit_config_package': 'none', # not necessary if launch_rviz=false
            'configure_via_rws': 'false' # must be false for omnicore controllers
        }.items()
    )

#    description_include= IncludeLaunchDescription(
#        PythonLaunchDescriptionSource(simbot_description_pkg_path + '/launch/description.launch.py'),
#        launch_arguments = {
#            'use_sim_time': use_sim,
#            'model': LaunchConfiguration('model'),
#            'use_state_pub_gui' : 'false'
#        }.items()
#    )

    return LaunchDescription(declared_arguments + [include_launcher])
