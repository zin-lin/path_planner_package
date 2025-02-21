import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from annex_msgs.msg import Con2vcu
import time

class Mode(Node):
    def __init__(self, parent_node,mode_args, node_name):
        super().__init__(node_name)
        # create autonomous mode publisher
        self.publisher = self.create_publisher(Con2vcu,'adsmt/autonomous_control', 10)
        self.mode_args = mode_args
        self.time = 20.0
        self.record_time = time.time()
        self.kill_check_timer = self.create_timer(0.1, self.kill_check )
        self.logger = self.get_logger()
        self.msg = Con2vcu()
        self.parent_node = parent_node

    # publish Con2Vcu messages
    def publish_con2vcu(self):
        # publishes message
        self.publisher.publish(self.msg)

    def shutdown(self):
        self.destroy_node()
        self.parent_node.destroy_node()


    # kill if time exceeds
    def kill_check(self):
        # if time mode
        if self.mode_args == 2:
            current_time = time.time()
            lapsed_time = current_time - self.record_time
            if lapsed_time > self.time:
                # kill powers
                self.msg.dir = 20.0
                self.publish_con2vcu()
                self.shutdown()
        else:
            # cancel after first call if not time mode to save resources
            self.kill_check_timer.cancel()
