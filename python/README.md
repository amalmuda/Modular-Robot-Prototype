## Firmware/software for the robot/prototype

Set up the environment:
```
$ conda create --name mats_env --file requirements.txt
$ conda activate mats_env
```
After installation, make sure:
- U2D2 Power Hub Board is turned ON and connected to the robot
- USB from the U2D2 is connected to your computer to the right port

Then you can run your Python files from the src folder with examples:
```
python breakdance.py
python wake_up.py
python dance.py
```
