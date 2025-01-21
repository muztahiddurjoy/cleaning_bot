import serial
import rclpy
from rclpy.node import Node

class cleaning_bot(Node):
    def __init__(self):
        super().__init__('cleaning_bot')  
        
        try:
            self.ser=serial.Serial('/dev/ttyACM0',115200,timeout=2)
        except:
            self.get_logger().error("could not connect")
        self.ser.write(f'a'.encode())   
        self.get_logger().info("Connected with arduino")
     




def main(args=None):
    rclpy.init(args=args)   
    node = cleaning_bot()    
    rclpy.spin(node)       
    node.destroy_node()   
    rclpy.shutdown()     


