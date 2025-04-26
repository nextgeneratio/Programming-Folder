import pyscreenshot
import time


image = pyscreenshot.grab(bbox=(0, 0, 800, 600))  # x1, y1, x2, y2
time.sleep(3)
image.show()
image.save('screenshot.png')
