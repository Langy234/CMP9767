import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class MoveCircle(Node):

    def __init__(self):
        super().__init__('move_circle')

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.25
        msg.angular.z = 0.5

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    move_circle = MoveCircle()

    rclpy.spin(move_circle)

    move_circle.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
