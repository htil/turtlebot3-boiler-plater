from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='auto_turtle',
            namespace='scanner',
            executable='scanner',
            name='scanner',
            output='screen',   # <<< important
            emulate_tty=True,  # <<< important for live flushing
            arguments=['--ros-args', '--log-level', 'INFO']
        ),
        Node(
            package='auto_turtle',
            namespace='locomotion',
            executable='locomotion',
            name='locomotion',
            output='screen',   # <<< important
            emulate_tty=True,  # <<< important for live flushing
            arguments=['--ros-args', '--log-level', 'INFO']
        ),
        Node(
            package='auto_turtle',
            namespace='tagdetector',
            executable='tagdetector',
            name='tagdetector',
            output='screen',   # <<< important
            emulate_tty=True,  # <<< important for live flushing
            arguments=['--ros-args', '--log-level', 'INFO']
        ),
    ])