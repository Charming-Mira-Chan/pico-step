from machine import Pin
import utime
utime.sleep(0.1) # Wait for USB to become ready

# Define pins
pins = [
  Pin(2, Pin.OUT),
  Pin(3, Pin.OUT),
]

# Create a sequence
step_sequence = [
  [1,0],
  [0,1],
]

# Use loops to set pins in sequence
while True:
  for step in step_sequence:
    for i in range(len(pins)):
      pins[i].value(step[i])
      utime.sleep(0.01)
