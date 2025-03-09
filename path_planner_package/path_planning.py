import rclpy
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from annex_msgs.msg import Vcu2ai, Ai2vcu
from .nodes.both_test.acceleration import Acceleration
from .nodes.both_test.acceleration_walk import AccelerationWalk
from .nodes.both_test.drive_turn import DriveTurn
from .nodes.both_test.walk_turn import WalkTurn
from .nodes.both_test.autonomous_demo import AutonomousDemo
from .nodes.sim_only_test.kinematic_inspection import KinematicsInspection

PATH_PLANNING_MODES = {
    'ACCELERATION':1,
    'ACCELERATION_WALK':2,
    'WALK_TURN':3,
    'DRIVE_TURN':4,
    'SKID_PAD':7,
    'JUMP':5,
    'AUTONOMOUS':6,
    'KINEMATICS':8
}

MODE_ARGS = {
    'TIME':2,
    'FIX':1
}

# multithreaded class
class PathPlanner(Node):
    def __init__(self):
        super().__init__('path_planning')
        self.declare_parameter('mode', PATH_PLANNING_MODES['ACCELERATION'])
        self.declare_parameter('mode_args', MODE_ARGS['FIX'])
        self.mode= self.get_parameter('mode').value
        self.mode_args = self.get_parameter('mode_args').value
        self.mh_executor = MultiThreadedExecutor() # mh -> mode handler

        # adding self
        self.mh_executor.add_node(self)
        self.logger = self.get_logger() # set up logger

        self.logger.info('Path planning started.')
        self.logger.info('Mode: {}'.format(self.mode))
        self.logger.info('Mode-Args: {}'.format(self.mode_args))
        self.current_mode = None
        self._setup_mode()

    def _setup_mode(self):
        match self.mode:
            case 1:
                acc = Acceleration(self, self.mode_args)
                self.current_mode = acc
            case 2:
                acc = AccelerationWalk(self, self.mode_args)
                self.current_mode = acc
            case 3:
                walk_turn = WalkTurn(self, self.mode_args)
                self.current_mode = walk_turn
            case 4:
                drive_turn = DriveTurn(self, self.mode_args)
                self.current_mode = drive_turn
            case 6:
                auto = AutonomousDemo(self, self.mode_args)
                self.current_mode = auto

            case 8:
                kinematics = KinematicsInspection(self, self.mode_args)
                self.current_mode = kinematics

            case _:
                acc = Acceleration(self, self.mode_args)
                self.current_mode = acc

        self.mh_executor.add_node(self.current_mode)

# main method
def main(args=None):
    rclpy.init(args=args)

    path_planner = PathPlanner()

    # spin executor
    path_planner.mh_executor.spin()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    path_planner.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
