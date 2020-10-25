import sys
import rclpy
from rclpy.node import Node
from webots_ros2_msgs.srv import SetDifferentialWheelSpeed
from math import pi
import rclpy
from rclpy.time import Time
from tf2_ros import StaticTransformBroadcaster
from webots_ros2_core.math_utils import interpolate_lookup_table
from webots_ros2_core.webots_node import WebotsNode
from std_msgs.msg import Float64

class service_node_vel(WebotsNode):

    def __init__(self,args):
        super().__init__('sensor_enable_node',args)

        self.sensorTimer = self.create_timer(0.001 * self.timestep,
                                             self.sensor_callback)
        self.timestep=16
        self.right_sensor = self.robot.getDistanceSensor('ls_right')
        self.right_sensor.enable(self.timestep)
        self.mid_sensor = self.robot.getDistanceSensor('ls_mid')
        self.mid_sensor.enable(self.timestep)
        self.left_sensor = self.robot.getDistanceSensor('ls_left')
        self.left_sensor.enable(self.timestep)
        
        self.sensorPublisher_right = self.create_publisher(Float64, 'right_IR', 10)
        self.sensorPublisher_mid = self.create_publisher(Float64, 'mid_IR', 10)
        self.sensorPublisher_left = self.create_publisher(Float64, 'left_IR', 10)
        self.get_logger().info('Sensor enabled')



    def sensor_callback(self):
        # Publish distance sensor value
        msg_right = Float64()
        msg_mid = Float64()
        msg_left = Float64()

        msg_right.data = self.right_sensor.getValue()
        msg_mid.data = self.mid_sensor.getValue()
        msg_left.data = self.left_sensor.getValue()

        self.sensorPublisher_right.publish(msg_right)
        self.sensorPublisher_mid.publish(msg_mid)
        self.sensorPublisher_left.publish(msg_left)

def main(args=None):
    rclpy.init(args=args)
    client_vel = service_node_vel(args=args)

    while rclpy.ok():
        rclpy.spin_once(client_vel)

    
    client_vel.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
