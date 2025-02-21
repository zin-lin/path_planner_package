"""
Author: Zin Lin Htun
Description: Formula Student Association England (FSAE) defines acceleration as a 100 meters track with a straight line
Modifications: since the adsmt is using cm instead of m scale and is walk a smaller 50 cm track will be added
"""

from ..mode import Mode
from nav_msgs.msg import Odometry
from annex_msgs.msg import Con2vcu


# Acceleration Walk Class
class AccelerationWalk(Mode):
    def __init__(self, parent,mode_args):
        super().__init__(parent,mode_args,'acceleration_walk')
        self.current_x = 0
        self.current_y = 0
        self.current_z = 0

        # create publish timer
        msg = Con2vcu()
        msg.deg = 1.0 # degree turn proportion
        msg.mode = 1.0
        msg.dir = 1.0 # drive forward
        self.msg = msg
        self.time = 180 # 3 minutes
        self._sub_pub()
        self.publish_con2vcu()
        # competition equivalents
        self.x_limit = 10 # 10 meters
        self.logger.info('Acceleration Walk Started')


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

        # end event mode
        if self.x_limit-0.5 < self.current_x < self.x_limit+0.5:
            # stop command
            self.msg.dir = 20.0
            self.publish_con2vcu()
            self.shutdown()

