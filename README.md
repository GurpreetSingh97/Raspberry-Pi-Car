# Raspberry Pi Car with Ultrasonic Sensor, Camera, and Keyboard Control

This project is a Python script designed to control a raspberry pi car using keyboard input via a Tkinter GUI while monitoring the environment using an ultrasonic sensor and displaying the camera feed with FPS overlay.

## Demo
![carDemo](https://github.com/GurpreetSingh97/Raspberry-Pi-Car/assets/36395745/5415aa4a-6aba-48f6-ae4d-8b6b5c18ac01)



## Requirements

- Raspberry Pi (tested on Raspberry Pi 3 Model B+)
- Ultrasonic sensor (HC-SR04 or similar)
- Raspberry Pi camera module
- 4-wheeled robot chassis with motor drivers compatible with GPIO pins
- Python 3
- OpenCV (`opencv-python`)
- Tkinter
- gpiozero

## Setup

### Hardware Setup:

- Connect the ultrasonic sensor to GPIO pins according to the TRIG and ECHO pins defined in the script.
- Connect the robot chassis motors to GPIO pins specified for left and right motors in the `robot_control` function.
- Connect the Raspberry Pi camera module.

### Software Setup:

- Install the required Python libraries:

    ```bash
    pip install opencv-python gpiozero
    ```

## Usage

1. Run the Python script `robot.py` using the following command:

    ```bash
    python robot.py
    ```

2. Use the keyboard arrow keys for controlling the robot:
   - Press `w` for forward movement (if it's safe based on ultrasonic sensor reading).
   - Press `s` for backward movement.
   - Press `a` for left turn.
   - Press `d` for right turn.

3. The ultrasonic sensor continuously monitors the distance in front of the robot. If the distance falls below 20cm, the robot stops moving forward to avoid obstacles.

4. The camera captures video frames and displays them in a window with FPS overlay. Press `q` to quit the camera feed window.

