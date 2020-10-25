#!/usr/bin/env python

"""Launch Webots e-puck driver."""

import os
from launch.substitutions.path_join_substitution import PathJoinSubstitution
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    package_dir = get_package_share_directory('webots_ros2_epuck')
    # # Webots
    # webots = WebotsLauncher(
    #     world=os.path.join(package_dir, 'worlds', 'epuck_with_custom.wbt')
    # )

    webots = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('webots_ros2_core'), 'launch', 'robot_launch.py')
        ),
        launch_arguments=[
            ('package', 'webots_ros2_epuck'),
            ('executable', 'enable_sensor'),
            ('world', PathJoinSubstitution([package_dir, 'worlds', 'epuck_with_custom.wbt'])),
        ]
    )
   
   
    return LaunchDescription([
        webots,
        Node(
            package='webots_ros2_epuck',
            executable='controller_custom_robot',
            name='controller_custom_robot'
        )
    ])
