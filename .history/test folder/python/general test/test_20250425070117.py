import pyscreenshot
import time


image = pyscreenshot.grab()
time.sleep(3)
image.show()
image.save('screenshot.png')
