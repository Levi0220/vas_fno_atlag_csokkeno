import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class ArrayRange(Node):
    def __init__(self):
        super().__init__('array_range')
        self.sub = self.create_subscription(Int32MultiArray, 'unsorted_array', self.cb, 10)
        self.get_logger().info('array_range started (max - min)')

    def cb(self, msg: Int32MultiArray):
        data = list(msg.data)
        diff = max(data) - min(data)
        self.get_logger().info(f'range: {max(data)} - {min(data)} = {diff}')

def main():
    rclpy.init()
    node = ArrayRange()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
