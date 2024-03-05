import cv2
import time
import numpy as np
import tkinter as tk
from gpiozero import Robot
from threading import Thread
import RPi.GPIO as GPIO

# Initialize GPIO for ultrasonic sensor
GPIO.setmode(GPIO.BCM)
TRIG1, ECHO1 = 23, 24
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.output(TRIG1, False)
print("Waiting For Sensor To Settle")
time.sleep(2)

# Camera settings
CAMERA_DEVICE_ID = 0
IMAGE_WIDTH = 320
IMAGE_HEIGHT = 240

# Shared variable for robot movement control
is_safe_to_move = True

def measure_distance(trig, echo):
    """Measure the distance using ultrasonic sensor."""
    GPIO.output(trig, True)
    time.sleep(0.001)
    GPIO.output(trig, False)
    start_time = time.time()
    while GPIO.input(echo) == 0:
        start_time = time.time()
    while GPIO.input(echo) == 1:
        stop_time = time.time()
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    return round(distance, 2)

def distance_monitoring():
    """
    Function to continuously monitor the distance using ultrasonic sensor and update the shared variable is_safe_to_move accordingly.
    """
    global is_safe_to_move
    try:
        while True:
            distance = measure_distance(TRIG1, ECHO1)
            print("Distance Sensor 1:", distance, "cm")
            if distance < 20:
                is_safe_to_move = False
            else:
                is_safe_to_move = True
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Distance measurement stopped by user")

def visualize_fps(image, fps: int):
    """
    Function to overlay FPS (Frames Per Second) on the captured video frame.
    """
    if len(np.shape(image)) < 3:
        text_color = (255, 255, 255)  # White color for grayscale images
    else:
        text_color = (0, 255, 0)  # Green color for color images
    cv2.putText(image, f'FPS = {fps:.1f}', (24, 20), cv2.FONT_HERSHEY_PLAIN, 1, text_color, 1)
    return image

def camera_capture():
    """
    Function to capture video frames from the camera, calculate FPS, and display the frame with FPS overlay.
    """
    cap = cv2.VideoCapture(CAMERA_DEVICE_ID)
    cap.set(3, IMAGE_WIDTH)
    cap.set(4, IMAGE_HEIGHT)
    while True:
        _, frame = cap.read()
        fps = 1.0 / (time.time() - time.time())  # Calculate FPS
        cv2.imshow('frame', visualize_fps(frame, fps))  # Display frame with FPS overlay
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def robot_control():
    """
    Function to control the robot movement based on keyboard input using Tkinter GUI.
    """
    robby = Robot(left=(7, 8), right=(9, 10))
    def keydown(e):
        global is_safe_to_move
        key = e.keysym
        if key == 'w' and is_safe_to_move:
            robby.forward()
        elif key == 's':  # Allow backward movement always
            robby.backward()
        elif key == 'a' :
            robby.left()
        elif key == 'd':
            robby.right()
    def keyup(e):
        robby.stop()
    root = tk.Tk()
    frame = tk.Frame(root, width=100, height=100)
    frame.bind("<KeyPress>", keydown)
    frame.bind("<KeyRelease>", keyup)
    frame.pack()
    frame.focus_set()
    root.mainloop()

# Start threads for each functionality
Thread(target=distance_monitoring).start()
Thread(target=camera_capture).start()
Thread(target=robot_control).start()

try:
    while True:  # Main loop
        time.sleep(10)  # Main loop sleeps for 10 seconds
except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    GPIO.cleanup()  # Cleanup GPIO resources when program exits
