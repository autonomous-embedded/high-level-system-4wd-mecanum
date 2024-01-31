# Jetson tests
Directory containing tests to be run on the Jetson Orin NX platform.
It contains the following tests:
- `sending_control_request.py`

## sending_control_request.py
This Python script sends a control request to the Omni4WD Nexus platform via a serial connection. It uses the `mecanum_pb2` module generated from the `mecanum.proto` file located in the `mecanum-if/protobuf` directory. To generate `mecanum_pb2` module refer to the section - `Generating Python Sources` in [mecanum-if/README.md](https://github.com/autonomous-embedded/mecanum-if/blob/master/README.md).

### Usage
1. Navigate to the `tests` directory.
2. Run the script with the desired parameters.  
   For example:
```bash
python3 sending_control_request.py 100 1.5 0 --port /dev/ttyUSB0 --baudrate 19200 --time 5
```
  - `speed`: Speed in mm/s.
  - `rad`: Radius in meters.
  - `omega`: Angular velocity in rad/s.
  - `--time`: Time in seconds for which the control request messages will be sent (default: 2).
  - `--port`: Serial port (default: /dev/ttyUSB0).
  - `--baudrate`: Baudrate (default: 19200).
3. The script will send control request messages with the specified parameters for the specified time. After that, it will send a stop command to the robot (speeds = 0).
4. Check your robot to see if it responds appropriately to the control commands.

#### Notes
- Ensure that the serial port (--port) and baudrate (--baudrate) match your robot's configuration.
- Make sure your robot is ready to receive and interpret the control request messages.
- Adjust the parameters according to your specific testing requirements.
- If you encounter any issues, check the serial connection and make sure that the required libraries are installed.


