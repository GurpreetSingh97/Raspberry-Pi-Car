# Raspberry Pi Car with Ultrasonic Sensor, Camera, and Keyboard Control

This project enables you to control a Raspberry Pi-powered car using keyboard input, while using an ultrasonic sensor to avoid obstacles and a camera to monitor the environment. The camera feed displays an FPS overlay, providing a real-time visual feed of the car's surroundings.

## Demo
<!--![carDemo](https://github.com/GurpreetSingh97/Raspberry-Pi-Car/assets/36395745/5415aa4a-6aba-48f6-ae4d-8b6b5c18ac01)-->
<!-- ![IMG_9057 (2)](https://github.com/user-attachments/assets/2391f06e-3984-49a7-96db-09955cc34d18)-->
<!-- ![finalMat](https://github.com/user-attachments/assets/57674fba-e75e-41b3-ad5c-82216553862f)-->
<!-- ![upperw](https://github.com/user-attachments/assets/2c5f1392-0ccd-47c5-a845-2e85be1c935a) -->

<p align="center">
  <img src="https://github.com/user-attachments/assets/2391f06e-3984-49a7-96db-09955cc34d18" alt="IMG_9057 (2)">
</p>
<p align="center">Car in Motion</p>

<br> <!-- Add a line break -->

<p align="center">
  <img src="https://github.com/user-attachments/assets/57674fba-e75e-41b3-ad5c-82216553862f" alt="finalMat">
</p>
<p align="center">Ultrasonic Sensor Readings and Car's Perspective</p>

## Requirements

- Raspberry Pi (tested on Raspberry Pi 3 Model B+)
- Ultrasonic sensor (HC-SR04 or similar)
- Raspberry Pi camera
- 4-wheeled car chassis with motor drivers compatible with GPIO pins
- Python 3
- OpenCV (`opencv-python`)
- Tkinter
- gpiozero

## Setup

### Hardware Setup:

- Connect the ultrasonic sensor to GPIO pins according to the TRIG and ECHO pins defined in the script.
- Connect the car chassis motors to GPIO pins specified for left and right motors in the `robot_control` function.
- Connect the Raspberry Pi camera module.

### Software Setup:

- Install the required Python libraries:

    ```bash
    pip install opencv-python gpiozero
    ```

## Usage

1. Run the Python script `rasPiCar.py` using the following command:

    ```bash
    python rasPiCar.py
    ```

2. Use the keyboard arrow keys for controlling the car:
   - Press `w` for forward movement (if it's safe based on ultrasonic sensor reading).
   - Press `s` for backward movement.
   - Press `a` for left turn.
   - Press `d` for right turn.

3. The ultrasonic sensor continuously monitors the distance in front of the car. If the distance falls below 20cm, the car stops moving forward to avoid obstacles.

4. The camera captures video frames and displays them in a window with FPS overlay. Press `q` to quit the camera feed window.

