"""
Author: Zin Lin Htun
Description: Formula Student Association England (FSAE) defines acceleration as a 100 meters track with a straight line
Modifications: since the adsmt is using cm instead of m scale, it will be a 10 meters track
"""
from ..mode import Mode
from nav_msgs.msg import Odometry
from annex_msgs.msg import Con2vcu

# Acceleration Class
class DriveTurn(Mode):
    def __init__(self, parent,mode_args):
        super().__init__(parent, mode_args, 'drive_turn')
        self.current_x = 0
        self.current_y = 0
        self.current_z = 0

        # competition equivalents
        self.x_limit = 10 # 10 meters
        msg = Con2vcu()
        msg.deg = 0.5 # degree turn proportion 1 is default
        msg.mode = 1.0
        msg.dir = 7.0 # drive right
        self.msg = msg

        self._sub_pub()
        self.create_timer(0.1, self.publish_con2vcu )

    # subscription and publications
    def _sub_pub(self):
        self.create_subscription(Odometry, 'model/adsmt/odometry', self.odom_callback, 10)

    # odometry callback
    def odom_callback(self, msg:Odometry):
        # setting odometry
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        self.current_z = msg.pose.pose.position.z

        self.current_x = abs(self.current_x) # sign does nae matter
        self.current_y = abs(self.current_y) # sign does nae matter
        self.current_z = abs(self.current_z)
        # for turn methods use timer