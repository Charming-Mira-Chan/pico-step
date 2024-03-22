# pico-step

Use this code base to operate a step motor on a Pico Pi W. The idea is to simulate an industrial IOT gate type device.

![image](https://github.com/zebra-acrobatic/pico-step/assets/158549190/a9123f53-85ba-4b44-bd78-528c4cd40d80)

This code (and diagram.json) is intended to be used with [wokwi](https://wokwi.com/)

## Task 1: Configure basic project

1. Go to the wokwi.com page and click **Pi-Pico** > **Micropython** to start a new project using a template.

2. Copy the contents of the **diagram.json** from this repo to the project.

3. Examine the diagram and observe the connections between pins and devices.

4. Use the code from **step.py** to move the motor in one direction.

## Step 2: Building a gate

1. Modify the code to simulate closing a gate on start. Change the scrip to start by moving to a position of -90 degrees.

2. Then you will need to create a function to simulate making the motor open and closs the gate. Your function should make the motor:
  2b. Move back to a position of 0 degrees.
  2c. Wait 30 seconds, then move the motor position back to -90 degrees.
  2d. Optionally, you could simulate warning lights by adding an LED that will blink while the gate is moving.
  2e. Optionally, you could simulate a safety mechanism by adding a distance sensor to stop the gate moving if an object is below the gate.

## Task 3: Adding a button

1. Add a button to the system:
  1a. Click **+** and add a **pushbutton**.
  1b. Connect the push button (**btn 1:1:l** to**3V** and  **btn 1:2:r** to **Pico GP:26**)

3. Modify the code to call your function when the button is pressed (you may find some ideas in **hint.py**).

## Task 4: Network capable

1. Configure the device to join a WiFi network (any should work in the simulator).
   
2. Configure the device to send UDP messages to any IP when the gate is opened and closed.
