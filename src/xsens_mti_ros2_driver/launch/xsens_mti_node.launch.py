from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path

def generate_launch_description():

    # Default parameter file path
    default_param_file = Path(
        get_package_share_directory('xsens_mti_ros2_driver'),
        'param',
        'xsens_mti_node.yaml'
    )

    # Declare launch argument
    param_file_arg = DeclareLaunchArgument(
        'param_file',
        default_value=str(default_param_file),
        description='Path to the xsens_mti_node parameter file'
    )

    param_file = LaunchConfiguration('param_file')

    ld = LaunchDescription()

    # Add launch argument
    ld.add_action(param_file_arg)

    # Set environment variables to control logging behavior
    ld.add_action(SetEnvironmentVariable('RCUTILS_LOGGING_USE_STDOUT', '1'))
    ld.add_action(SetEnvironmentVariable('RCUTILS_LOGGING_BUFFERED_STREAM', '1'))

    xsens_mti_node = Node(
        package='xsens_mti_ros2_driver',
        executable='xsens_mti_node',
        name='xsens_mti_node',
        output='screen',
        parameters=[param_file],
        arguments=[]
    )

    ld.add_action(xsens_mti_node)

    return ld
