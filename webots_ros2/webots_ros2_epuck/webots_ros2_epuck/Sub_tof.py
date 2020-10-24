import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Range



class Sub_tof(Node):

    def __init__(self):
        super().__init__('subscriber_tof')
        self.subscription = self.create_subscription(Range,'tof',self.listener_callback,10)
        # self.subscription  # prevent unused variable warning
        self.range=0

    def listener_callback(self, msg):
        self.range=msg.range
        self.get_logger().info('Sensor is seeing obstacle in distance: %f' % self.range)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = Sub_tof()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()