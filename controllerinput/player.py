from controllerinput.keyboardcontroller import keyDown, keyUp,keyPress
from controllerinput.mousecontroller import Mouse
from controllerinput.keyboard_keys import keys
import time

# If we decide to use the mouse, but I think all keyboard controls is easierwawa
# mouse = Mouse()
# while(1):
#     time.sleep(4)
#     mouse.click((500,50), "left")

#Let the man run in a square a bit
while(1):
    keyPress(keys['w'], 1)
    time.sleep(0.5)
    keyPress(keys['a'], 1)
    time.sleep(0.5)
    keyPress(keys['s'], 1)
    time.sleep(0.5)
    keyPress(keys['d'], 1)
    time.sleep(0.5)
