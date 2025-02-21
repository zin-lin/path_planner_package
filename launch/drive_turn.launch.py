"""
Author: Zin Lin Htun
class: Launch
"""

# import necessaries
from launch import LaunchDescription

# import descriptions
from launch_ros.actions import Node

# constants
PKG_SRC = 'path_planner_package'

def generate_launch_description():

    pp_node = Node(
        package=PKG_SRC,
        executable='path_planning',
        output='both', # both means both log files and terminal
        parameters=[
            {'mode': 4, 'mode_args': 2}
        ],
    )

    # empty launch_des
    launch_description = LaunchDescription()

    # launch extra components
    launch_description.add_action(pp_node) # adding path planner node to the launch description


    return launch_description
