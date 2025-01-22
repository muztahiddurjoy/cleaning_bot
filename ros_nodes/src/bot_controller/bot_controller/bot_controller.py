import serial
import rclpy
from rclpy.node import Node
import geometry_msgs.msg._twist as Twist

class cleaning_bot(Node):
    def __init__(self):
        super().__init__('cleaning_bot')  
        
        try:
            #trying to connect with arduino
            self.ser=serial.Serial('/dev/ttyACM0',115200,timeout=2)
        except:
            self.get_logger().error("could not connect")
        self.ser.write(f'a'.encode())   
        self.get_logger().info("Connected with arduino")

        self.create_timer(0.0000000000000001,self.read_data)

        #new twist message
        twist = Twist.Twist()
        twist.linear.x = 0.5
        twist.angular.z = 0.5
        self.subscription = self.create_subscription(Twist.Twist, 'acb_cmd_vel', self.send_motor_data_to_arduino, 10)


    def send_motor_data_to_arduino(self,msg):
        throttle = msg.linear.x
        steering = msg.angular.z
        self.get_logger().info(f"throttle: {throttle} steering: {steering}")
        # command = f"L{throttle:.2f} A{steering:.2f} B{15} R{16.5} M{7.2}\n"
        # self.ser.write(command.encode())

    def read_data(self):
        data=self.ser.readline().decode()
        if data:
            self.get_logger().info(data)
        

def main(args=None):
    rclpy.init(args=args)   
    node = cleaning_bot()    
    rclpy.spin(node)       
    node.destroy_node()   
    rclpy.shutdown()     


