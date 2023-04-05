# minWSG
Minimal code for controlling schunk wsg grippers. [wsg.py](wsg.py) contains the following functionalities:
- Move fingers to home (fully open) state
- Move fingers to desired position
- Grip (grasp) with desired force
- Release

The controller communicates with a WSG gripper via its text-based interface. It is required to enable Settings -> Command Interface -> Use text based interface through your gripper's web interface.

For demo, connect the wsg gripper and simply run:
```
python demo.py
```

To extend this library for more functionalities, please checkout the "GCL Gripper Control Language Reference Manual" by clicking Help -> Documentation -> GCL Reference Manual on your gripper's web interface.
