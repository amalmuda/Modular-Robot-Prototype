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

# Final standing positions for each servo
STANDING_POSITIONS = {
    1: 350,  # Hip angle for Leg 1
    5: 650,  # Knee angle for Leg 1
    2: 670,  # Hip angle for Leg 2
    6: 370,  # Knee angle for Leg 2
    3: 350,  # Hip angle for Leg 3
    7: 650,  # Knee angle for Leg 3
    4: 670,  # Hip angle for Leg 4
    8: 370,  # Knee angle for Leg 4
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

# Enable torque for each servo
for dxl_id in DXL_ID:
    packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)

# Step 1: Gradually stand up by incrementally moving to each standing position
def gradual_stand_up():
    increments = 10  # Number of steps to reach the final position
    for step in range(1, increments + 1):
        for dxl_id, final_position in STANDING_POSITIONS.items():
            # Calculate intermediate position
            initial_position = GOAL_POSITION_ZERO  # Starting position (0 degrees)
            intermediate_position = initial_position + (final_position - initial_position) * step // increments
            # Set the servo to the intermediate position
            packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_PRO_GOAL_POSITION, intermediate_position)
        
        # Short delay for servos to move in each step
        time.sleep(0.2)

# Execute the gradual stand-up sequence
gradual_stand_up()

# Wait for a moment in the standing position
time.sleep(1)

# Step 2: Set all servos back to 0 degrees (flat position)
for dxl_id in DXL_ID:
    packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_PRO_GOAL_POSITION, GOAL_POSITION_ZERO)

# Wait for servos to reach 0 degrees
time.sleep(2)

# Close port
portHandler.closePort()

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

# Standing position angles for each servo
# These values are estimated for a basic standing position
STANDING_POSITIONS = {
    1: 350,  # Hip angle for Leg 1 (servo 1)
    5: 650,  # Knee angle for Leg 1 (servo 5)
    2: 670,  # Hip angle for Leg 2 (servo 2)
    6: 370,  # Knee angle for Leg 2 (servo 6)
    3: 350,  # Hip angle for Leg 3 (servo 3)
    7: 650,  # Knee angle for Leg 3 (servo 7)
    4: 670,  # Hip angle for Leg 4 (servo 4)
    8: 370,  # Knee angle for Leg 4 (servo 8)
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

# Enable torque for each servo
for dxl_id in DXL_ID:
    packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)

# Stand up function
def stand_up():
    # Set each servo to its respective standing position
    for dxl_id, goal_position in STANDING_POSITIONS.items():
        packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_PRO_GOAL_POSITION, goal_position)

    # Wait for servos to reach position
    time.sleep(2)

# Execute the stand-up sequence
stand_up()

# Close port
portHandler.closePort()

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

# Enable torque for each servo
for dxl_id in DXL_ID:
    packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)

# Set all servos to 0 degrees
for dxl_id in DXL_ID:
    packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_PRO_GOAL_POSITION, GOAL_POSITION_ZERO)

# Wait for servos to reach position
time.sleep(2)

# Close port
portHandler.closePort()
