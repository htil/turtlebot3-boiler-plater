import rclpy
from rclpy.node import Node
from std_msgs.msg import String
#from sensor_msgs.msg import LaserScan
#from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile


class Locomotion(Node):

    def __init__(self):
        super().__init__('turtlebot3_locomotion')
        self.subscription = self.create_subscription(
            String,
            '/front_state',
            self.listener_callback,
            10)
        qos = QoSProfile(depth=10)
        self.pub = self.create_publisher(Twist, 'cmd_vel', 1)
        self.subscription  # prevent unused variable warning

    def create_twist_msg(self, x, z):
        t = Twist()
        t.linear.x = x
        t.angular.z = z
        return t

    def log_message(self, msg):
        self.get_logger().info(str(msg))
    
    def listener_callback(self, msg):
        if msg.data == "unblocked":
           _twist = self.create_twist_msg(0.1, 0.0)
           self.pub.publish(_twist)
           self.log_message("Forward")
        else: 
           _twist = self.create_twist_msg(0.0, 0.5)
           self.pub.publish(_twist)
           self.log_message("Turn")

def main(args=None):
    rclpy.init(args=args)

    tb3_locomotion = Locomotion()

    rclpy.spin(tb3_locomotion)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
