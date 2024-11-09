# Assignment 5 - IN5590
*Part 2 of 4 of the main project*

In this assignment you will make the physical robot from assignment 4. 

On [October 25](https://www.uio.no/studier/emner/matnat/ifi/IN5590/h24/timeplan/index.html#FOR)
we arrange a **mandatory status update** for your projects. Each student will have 3 minutes for the 
demonstration. The content should be:

- What you are making.
- How is it meant to work.
- Where are you now.
- What do you have left.
- Which issues have you faced

Bring the prototype.

## 1) CAD files

All SolidWorks-files should be put in directory: `./solidworks/`, including part and assembly files.

An image with side-by-side assambled part and exploded view, should be added as `./output/1.png`
Create two snapshots that illustrates the robot/prototype:
 - One with the entire assembled robot.
 - One png using the [exploaded view feature in SolidWorks](https://help.solidworks.com/2022/english/SolidWorks/sldworks/c_Exploded_Views_in_Assemblies.htm).

![Assembled view of the robot](./output/1assembled.PNG)

![Exploaded view of the robot](./output/1exploded.PNG)

**Deliverables:** SolidWorks files including assembly and partfiles in `./solidworks/` directory. `./output/1assembled.PNG` and `./output/1exploded.PNG` snapshots.

## 2) 3D-print

3D-print all the parts and take a photo of the robot once it is assembled.

![](./output/2physical_prototype.jpg)

Make a table of 3D-printer material used, infill and layer hight for all your parts. 
If you use the same setting for everything, use one row.

| Part  | Material        | Quantity | Infill   | Layer hight
| ----- | --------------- | -------- | -------- | ------------
| Block module | ABS | 9  | 20 % | .15 mm      
| Servo holder | ABS | 16  | 20 % | .15 mm     
| Lid | PolyMaker PLA | 19  | 20 % | .15 mm     
| Power Hub Board base | PolyMaker PLA | 1  | 20 % | .15 mm     

**Deliverables:** Image of the physical prototype as `./output/2physical_prototype.jpg` and table with 3D-print instructions.

## 3) Bill of materials

Main components:
| Item | Description      | Quantity 
| ---- | ---------------- | -------- 
| 1    | Robotis U2D2 Power Hub Board | 1         
| 2    | Dynamixel AX-18A servo | 8     

Mounting components:
| Item | Description      | Quantity 
| ---- | ---------------- | -------- 
| 1    | Dynamixel-AX Bioloid FP04-F2 frame | 8     
| 2    | Dynamixel-AX Bioloid FP04-F3 frame | 8 
| 3    | RS PRO Neodym magnet 2.09 kg - 12 mm | 52

Connectors and wiring:
| Item | Description      | Quantity 
| ---- | ---------------- | -------- 
| 1    | Robotis 3P Extension PCB | 9 
| 2    | 3P Molex male to female adapter| 36 
| 3    | Self-assembled 3P Molex cables 4 cm | 36   
| 4    | Self-assembled 3P Molex cables 8 cm | 16   
| 5    | Self-assembled 3P Molex cables 18 cm | 16

Fasteners:
| Item | Description      | Quantity 
| ---- | ---------------- | -------- 
| 1    | Bioloid Plastic Busher BPF-BU| 8 
| 2    | Bioloid Plastic Washer BPF-WA| 8
| 3    | M3 bolts| 8
| 4    | M2 screws | 164
| 5    | M2 nuts | 32  


