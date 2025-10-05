from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='vas_fno_atlag_csokkeno', executable='array_publisher', name='array_publisher', output='screen'),
        Node(package='vas_fno_atlag_csokkeno', executable='array_sorter',    name='array_sorter',    output='screen'),
        Node(package='vas_fno_atlag_csokkeno', executable='array_averager',  name='array_averager',  output='screen'),
        Node(package='vas_fno_atlag_csokkeno', executable='array_range',  name='array_range',  output='screen'),
    ])
