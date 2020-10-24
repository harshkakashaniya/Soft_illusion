import sys
import rclpy
from rclpy.node import Node
from webots_ros2_msgs.srv import SetDifferentialWheelSpeed

class service_node_vel(Node):

    def __init__(self):
        super().__init__('service_node_vel')
        self.motorclient = self.create_client(SetDifferentialWheelSpeed,
                                                'motor')
        while not self.motorclient.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.value=SetDifferentialWheelSpeed.Request()

    def client_request(self):
        self.value.left_speed= float(sys.argv[1])
        self.value.right_speed= float(sys.argv[2])
        self.response=self.motorclient.call_async(self.value)

def main(args=None):
    rclpy.init(args=args)
    client_vel = service_node_vel()
    client_vel.client_request()

    while rclpy.ok():
        rclpy.spin_once(client_vel)
        if client_vel.response.done():
            try:
                response = client_vel.response.result()
            except Exception as e:
                client_vel.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                client_vel.get_logger().info(
                    ' Two wheel speeds set to %d , %d ' %
                    (client_vel.value.left_speed, client_vel.value.right_speed))
            break


    
    client_vel.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
