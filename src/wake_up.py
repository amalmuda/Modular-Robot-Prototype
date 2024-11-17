import time
from dynamixel_sdk import *  # Dynamixel SDK library

# Control table addresses
ADDR_TORQUE_ENABLE = 24
ADDR_GOAL_POSITION = 30
ADDR_PRESENT_POSITION = 36
ADDR_MOVING_SPEED = 32

# Servo configuration
PROTOCOL_VERSION = 1.0
BAUDRATE = 1000000
DEVICENAME = 'COM3'  # Adjust to your setup

# Servo IDs
TRIPOD_1 = [1, 4, 7]  # Tripod 1: 1 (front-left), 4 (back), 7 (front-right)
TRIPOD_2 = [2, 5, 8]  # Tripod 2: 2 (front-right), 5 (back), 8 (front-left)

# Conversion function for angle to Dynamixel position
def angle_to_position(angle):
    return int((angle + 150) / 300 * 1023)

# Initialize PortHandler and PacketHandler
port_handler = PortHandler(DEVICENAME)
packet_handler = PacketHandler(PROTOCOL_VERSION)

if not port_handler.openPort():
    print("Failed to open port!")
    exit()
if not port_handler.setBaudRate(BAUDRATE):
    print("Failed to set baudrate!")
    exit()

# Function to move servos
def move_servos(ids, positions, delay=0.5):
    for i, servo_id in enumerate(ids):
        position = positions[i]
        packet_handler.write2ByteTxRx(port_handler, servo_id, ADDR_GOAL_POSITION, position)
    time.sleep(delay)

# Enable torque
for servo_id in range(1, 9):
    packet_handler.write1ByteTxRx(port_handler, servo_id, ADDR_TORQUE_ENABLE, 1)

try:
    # 1. Starting Standing Position (ensure hips at 0°, knees at -90°)
    stand_hip_positions = angle_to_position(0)
    stand_knee_positions = angle_to_position(-90)
    move_servos(range(1, 9), [stand_hip_positions] * 4 + [stand_knee_positions] * 4)

    # 2. Lift Tripod 1 (1, 4, 7)
    lift_knee_positions = angle_to_position(-60)
    move_servos(TRIPOD_1, [lift_knee_positions] * 3)

    # 3. Swing Tripod 1 Forward
    move_servos([1, 7], [angle_to_position(30), angle_to_position(30)])  # Hips swing forward
    move_servos([4], [angle_to_position(-30)])  # Back leg swings forward

    # 4. Place Tripod 1 Down
    move_servos(TRIPOD_1, [stand_knee_positions] * 3)

    # 5. Lift Tripod 2 (2, 5, 8)
    move_servos(TRIPOD_2, [lift_knee_positions] * 3)

    # 6. Swing Tripod 2 Forward
    move_servos([2, 8], [angle_to_position(30), angle_to_position(30)])  # Hips swing forward
    move_servos([5], [angle_to_position(-30)])  # Back leg swings forward

    # 7. Place Tripod 2 Down
    move_servos(TRIPOD_2, [stand_knee_positions] * 3)

finally:
    # Disable torque
    for servo_id in range(1, 9):
        packet_handler.write1ByteTxRx(port_handler, servo_id, ADDR_TORQUE_ENABLE, 0)
    port_handler.closePort()
