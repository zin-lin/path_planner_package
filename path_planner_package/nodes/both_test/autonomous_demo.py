"""
Author: Zin Lin Htun
Description: Create a planned autonomous path for the robot to follow, operate autonomously without any manual controls
"""

from nav_msgs.msg import Odometry
from annex_msgs.msg import Con2vcu
from ..mode import Mode
import time

# Acceleration Walk Class
class AutonomousDemo(Mode):
    def __init__(self, parent, mode_args):
        super().__init__(parent,  mode_args, 'autonomous')
        self.current_x = 0
        self.current_y = 0
        self.current_z = 0

        # create publish timer
        msg = Con2vcu()
        msg.deg = 1.0  # degree turn proportion
        msg.mode = 0.5
        msg.dir = 2.0  # drive forward
        self.msg = msg

        self._sub_pub()
        # competition equivalents
        self.x_limit = 10  # 10 meters
        self.mode_args = 2 # force time mode
        # override time taken
        self.time = 60 # a minute
        self.seg = 12
        self.cycle = 1
        self.kill_check_timer.cancel()
        msg = Con2vcu()
        msg.deg = 1.0
        msg.mode = 0.5
        msg.dir = 6.0  # drive forward
        self.msg = msg
        self.publish_con2vcu()
        self.kill_check_timer = self.create_timer(12.01, self.kill_check)

    # subscription and publications
    def _sub_pub(self):
        self.create_subscription(Odometry, 'model/adsmt/odometry', self.odom_callback, 10)

    # do nothing
    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y

    # @override kill_check()
    def kill_check(self):
        # cycle completed stop
        if self.cycle >= 6:
            # kill
            self.msg.dir = 20.0
            self.publish_con2vcu()
            self.shutdown()
        current_time = time.time()
        lapsed_time = current_time - self.record_time
        if lapsed_time > self.seg:
            self.cycle += 1
            self.seg += 20

        match self.cycle:
            case 1:
                msg = Con2vcu()
                msg.deg = 1.0
                msg.mode = 0.5
                msg.dir = 6.0  # drive forward
                self.msg = msg
                self.publish_con2vcu()

            case 2:
                msg = Con2vcu()
                msg.deg = 0.5
                msg.mode = 1.0
                msg.dir = 7.0 # drive right
                self.msg = msg
                self.publish_con2vcu()

            case 3:
                msg = Con2vcu()
                msg.deg = 0.5
                msg.mode = 1.0
                msg.dir = 8.0 # drive left
                self.msg = msg
                self.publish_con2vcu()

            case 4:
                msg = Con2vcu()
                msg.deg = 0.5
                msg.mode = 1.0
                msg.dir = 2.0 # walk left
                self.msg = msg
                self.publish_con2vcu()

            case 5:
                msg = Con2vcu()
                msg.deg = 1.0
                msg.mode = 1.0
                msg.dir = 1.0 # walk straight forward
                self.msg = msg
                self.publish_con2vcu()
            case _:
                # do abs nth
                pass
