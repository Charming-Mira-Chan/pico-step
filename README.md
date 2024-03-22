# pico-step

Use this code base to operate a step motor on a Pico Pi W.

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

## Task 3: Adding a button

1. Add a button to the system:
  1a. Click **+** and add a **pushbutton**.
  1b. Connect the push button (**btn 1:1** to** Pico GP:26** and  **btn 1:2** to **Pico GP:22**)

3. Modify the code to call your function when the button is pressed (you may find some ideas in hint.py).
