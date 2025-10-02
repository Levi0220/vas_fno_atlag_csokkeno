import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray, Float32

class ArrayAverager(Node):
    def __init__(self):
        super().__init__('array_averager')
        self.sub = self.create_subscription(Int32MultiArray, 'unsorted_array', self.cb, 10)
        self.pub = self.create_publisher(Float32, 'array_average', 10)
        self.get_logger().info('array_averager started')

    def cb(self, msg: Int32MultiArray):
        data = list(msg.data)
        if not data:
            return
        avg = float(sum(data)) / float(len(data))
        self.pub.publish(Float32(data=avg))
        self.get_logger().info(f'avg: {avg:.2f}')

def main():
    rclpy.init()
    node = ArrayAverager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
