"""
Author: Zin Lin Htun
Description: Formula Student Association England (FSAE) defines acceleration as a 100 meters track with a straight line
Modifications: since the adsmt is using cm instead of m scale and is walk a smaller 50 cm track will be added
"""

from ..mode import Mode
from nav_msgs.msg import Odometry
from annex_msgs.msg import Con2vcu


# Acceleration Walk Class
class WalkTurn(Mode):
    def __init__(self,parent, mode_args):
        super().__init__(parent,mode_args, 'walk_turn')
        self.current_x = 0
        self.current_y = 0
        self.current_z = 0

        # create publish timer
        msg = Con2vcu()
        msg.deg = 1.0 # degree turn proportion
        msg.mode = 0.5
        msg.dir = 2.0 # drive forward
        self.msg = msg
        self.time = 180 # 3 minutes

        self._sub_pub()
        self.publish_con2vcu()
        # competition equivalents
        self.x_limit = 10 # 10 meters


    # subscription and publications
    def _sub_pub(self):
        self.create_subscription(Odometry, 'model/adsmt/odometry', self.odom_callback, 10)


    # odometry callback
    def odom_callback(self, msg:Odometry):
        # setting odometry
        # for turn methods do nothing, work with timer
        pass

