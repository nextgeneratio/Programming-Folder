import pyautogui
import cv2
import numpy as np
import time

# Screen resolution
resolution = (1920, 1080)

# Codec and filename
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 60.0

# VideoWriter
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create window safely
cv2.resizeWindow("Live", 480, 270)

# Start time
start_time = time.time()

try:
    while True:
        current_time = time.time()
        if current_time - start_time > 20:
            break

        # Screenshot
        img = pyautogui.screenshot()
        frame = np.array(img)

        # Convert color
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Save frame
        out.write(frame)

        # Show frame
        cv2.imshow("Live", frame)

        # Check if user closed window or pressed 'q'
        if cv2.getWindowProperty("Live", cv2.WND_PROP_VISIBLE) < 1:
            break
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
except Exception as e:
    print("Error:", e)
finally:
    out.release()
    cv2.destroyAllWindows()
