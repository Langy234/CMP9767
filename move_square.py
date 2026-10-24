import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class MoveSquare(Node):

    def __init__(self):
        super().__init__('move_square')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.i = 0
        self.side = 0

    def timer_callback(self):
        msg = Twist()

        if self.side >= 8:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            self.timer.cancel()
            return

        if self.side % 2 == 0:
            msg.linear.x = 0.2
            msg.angular.z = 0.0
            duration = 50
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
            duration = 31

        self.publisher_.publish(msg)
        self.i += 1

        if self.i >= duration:
            self.i = 0
            self.side += 1


def main(args=None):
    rclpy.init(args=args)

    move_square = MoveSquare()

    rclpy.spin(move_square)

    # Destroy the node explicitly
    move_square.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
