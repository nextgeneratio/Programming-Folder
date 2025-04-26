import pyscreenshot
import time


image = pyscreenshot.grab(b)
time.sleep(3)
image.show()
image.save('screenshot.png')
