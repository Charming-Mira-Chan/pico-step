from machine import Pin
import utime

def movethething():
  print("called thing")
  for x in range(0,20):
    for step in step_sequence:
      for i in range(len(pins)):
        pins[i].value(step[i])
        utime.sleep(0.01)

utime.sleep(0.1) # Wait for USB to become ready


# Define pins
pins = [
  Pin(2, Pin.OUT),
  Pin(3, Pin.OUT),
]
BUTTON = Pin(26, Pin.IN,Pin.PULL_DOWN)

# Create a sequence
step_sequence = [
  [1,0],
  [0,1],
]

# Use loops to set pins in sequence
while True:
  print("waiting", BUTTON.value())
  if BUTTON.value() == 1:
    print("pressed")
    movethething()
  utime.sleep(0.1)
