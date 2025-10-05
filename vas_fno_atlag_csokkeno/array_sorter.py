import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class ArraySorter(Node):
    def __init__(self):
        super().__init__('array_sorter')
        self.sub = self.create_subscription(Int32MultiArray, 'unsorted_array', self.cb, 10)
        self.pub = self.create_publisher(Int32MultiArray, 'sorted_array', 10)
        self.get_logger().info('array_sorter started (descending)')

    def cb(self, msg: Int32MultiArray):
        sorted_desc = sorted(list(msg.data), reverse=True)
        self.pub.publish(Int32MultiArray(data=sorted_desc))
        self.get_logger().info(f'sorted: {sorted_desc}')

def main():
    rclpy.init()
    node = ArraySorter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

