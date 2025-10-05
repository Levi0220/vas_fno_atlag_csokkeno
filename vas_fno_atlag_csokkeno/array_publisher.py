import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class ArrayPublisher(Node):
    def __init__(self):
        super().__init__('array_publisher')
        self.pub = self.create_publisher(Int32MultiArray, 'unsorted_array', 10)
        self.declare_parameter('length', 8)
        self.declare_parameter('min_val', -50)
        self.declare_parameter('max_val', 50)
        self.timer = self.create_timer(1.0, self.tick)
        self.get_logger().info('array_publisher started → /unsorted_array')

    def tick(self):
        n  = int(self.get_parameter('length').value)
        lo = int(self.get_parameter('min_val').value)
        hi = int(self.get_parameter('max_val').value)
        data = [random.randint(lo, hi) for _ in range(n)]
        self.pub.publish(Int32MultiArray(data=data))
        self.get_logger().info(f'pub: {data}')

def main():
    rclpy.init()
    node = ArrayPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
