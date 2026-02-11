from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from pathlib import Path

def generate_launch_description():

    # Default parameter file path
    default_param_file = Path(
        get_package_share_directory('ntrip'),
        'config',
        'ntrip-param.yaml'
    )

    # Declare the log level argument
    log_level_arg = DeclareLaunchArgument(
        'log_level',
        default_value='info',
        description='Logging level (debug, info, warn, error, fatal)',
        choices=['debug', 'info', 'warn', 'error', 'fatal']
    )

    # Declare parameter file argument
    param_file_arg = DeclareLaunchArgument(
        'param_file',
        default_value=str(default_param_file),
        description='Path to the ntrip parameter file'
    )

    log_level = LaunchConfiguration('log_level')
    param_file = LaunchConfiguration('param_file')

    # Create the node configuration
    ntrip_node = Node(
        package='ntrip',
        executable='ntrip',
        name='ntrip_client',
        output='screen',
        parameters=[param_file],
        remappings=[
            ('nmea', 'nmea'),
            ('rtcm', 'rtcm')
        ],
        arguments=['--ros-args', '--log-level', log_level]
    )

    return LaunchDescription([
        log_level_arg,
        param_file_arg,
        ntrip_node
    ])
