import rclpy
from rclpy.node import Node
from annex_msgs.msg import Vcu2ai, Ai2vcu


class PathPlanner(Node):
    def __init__(self):
        super().__init__('path_planning')


# main method
def main(args=None):
    rclpy.init(args=args)

    path_planner = PathPlanner()

    rclpy.spin(path_planner)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    path_planner.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


