import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class Publisher_vel(Node):

    def __init__(self):
        super().__init__('cmd_vel_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x=0.1
        msg.angular.z=0.5
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    publisher_obj = Publisher_vel()

    rclpy.spin(publisher_obj)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher_obj.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()