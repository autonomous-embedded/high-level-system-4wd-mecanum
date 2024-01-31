# Import the mecanum_pb2 module
from mecanum_if import mecanum_pb2
import serial

import time
import argparse

def send_command(serial_output, speed, rad, omega):
    # Create a ControlRequest message
    control_request = mecanum_pb2.ControlRequest()
    control_request.speed_mmps = speed
    control_request.rad = rad
    control_request.omega = omega
    
    # Serialize the message into a byte array
    data = control_request.SerializeToString()
    
    # Send the message
    serial_output.write(data)

def main():
    parser = argparse.ArgumentParser(description='Send a control request to the robot')
    parser.add_argument('speed', type=int, help='Speed in mm/s')
    parser.add_argument('rad', type=float, help='Radius in m')
    parser.add_argument('omega', type=float, help='Angular velocity in rad/s')
    parser.add_argument('--time', type=float, default=2, help=' Time in seconds for which the control request messages will be sent (default: 2)')
    parser.add_argument('--port', type=str, default='/dev/ttyUSB0', help='Serial port (default: /dev/ttyUSB0)')
    parser.add_argument('--baudrate', type=int, default=19200, help='Baudrate (default: 19200)')
    
    args = parser.parse_args()
    
    # Open the serial port
    serial_output = serial.Serial(args.port, args.baudrate)

    # Sending commands for a specified time
    start_time = time.time()
    while time.time() - start_time < args.time:
        send_command(serial_output, args.speed, args.rad, args.omega)
        time.sleep(0.1)

    # Stop the robot - send command few times to make sure it is received
    for i in range(5):
        send_command(serial_output, 0, 0, 0)
        time.sleep(0.1)

    serial_output.close()

if __name__ == '__main__':
    main()
