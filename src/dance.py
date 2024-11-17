import time
from dynamixel_sdk import *  # Dynamixel SDK library

# Control table addresses
ADDR_PRO_GOAL_POSITION = 30
ADDR_PRO_TORQUE_ENABLE = 24

# Protocol version
PROTOCOL_VERSION = 1.0

# Default settings
DXL_ID = [1, 2, 3, 4, 5, 6, 7, 8]  # Servo IDs 1 to 8
BAUDRATE = 1000000
DEVICENAME = 'COM3'
TORQUE_ENABLE = 1
GOAL_POSITION_ZERO = 512  # 512 corresponds to 0 degrees in Dynamixel

# Standing position angles for each servo
STANDING_POSITIONS = {
    1: 350,  # Hip angle for Leg 1
    5: 650,  # Knee angle for Leg 1
    2: 670,  # Hip angle for Leg 2
    6: 370,  # Knee angle for Leg 2
    3: 350,  # Hip angle for Leg 3
    7: 650,  # Knee angle for Leg 3
    4: 670,  # Hip angle for Leg 4
    8: 370,  # Knee angle for Leg 4,
}

# Initialize PortHandler and PacketHandler
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if not portHandler.openPort():
    print("Failed to open the port")
    exit()

# Set port baudrate
if not portHandler.setBaudRate(BAUDRATE):
    print("Failed to set the baudrate")
    exit()

# Enable torque for all servos
for dxl_id in DXL_ID:
    packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)

# Gradual stand-up function
def gradual_stand_up():
    increments = 10  # Number of steps to reach the final position
    for step in range(1, increments + 1):
        for dxl_id, final_position in STANDING_POSITIONS.items():
            # Calculate intermediate position
            initial_position = GOAL_POSITION_ZERO  # Starting position (flat, 0 degrees)
            intermediate_position = initial_position + (final_position - initial_position) * step // increments
            # Set the servo to the intermediate position
            packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_PRO_GOAL_POSITION, intermediate_position)
        time.sleep(0.2)  # Short delay for servos to move in each step

# Stand up function
def stand_up():
    for dxl_id, goal_position in STANDING_POSITIONS.items():
        packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_PRO_GOAL_POSITION, goal_position)
    time.sleep(2)  # Allow time for the robot to reach the standing position

# Reset to flat position (0 degrees for all servos)
def reset_to_flat():
    for dxl_id in DXL_ID:
        packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_PRO_GOAL_POSITION, GOAL_POSITION_ZERO)
    time.sleep(2)  # Allow time for servos to reach the flat position

# Main sequence
try:
    print("Executing gradual stand-up...")
    gradual_stand_up()
    time.sleep(1)

    print("Resetting to flat position...")
    reset_to_flat()

finally:
    # Disable torque for all servos
    for dxl_id in DXL_ID:
        packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_PRO_TORQUE_ENABLE, 0)
    # Close port
    portHandler.closePort()
    print("Port closed. Torque disabled.")
