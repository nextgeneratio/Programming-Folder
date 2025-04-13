import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os
import numpy as np

# Global variables
recording = None
paused = False
fs = 44100  # Sample rate
file_name = None
duration = None
recorded_data = []

# Function to start recording
def start_recording():
    global recording, paused, file_name, duration, recorded_data
    try:
        # Ask the user for the file name
        file_name = simpledialog.askstring("Input", "Enter the file name (without extension):")
        if not file_name:
            messagebox.showerror("Error", "File name cannot be empty!")
            return

        # Ask the user for the duration
        duration = simpledialog.askinteger("Input", "Enter the recording duration (in seconds):")
        if not duration or duration <= 0:
            messagebox.showerror("Error", "Duration must be a positive integer!")
            return

        paused = False
        recorded_data = []
        messagebox.showinfo("Recording", "Recording started...")
        recording = sd.InputStream(samplerate=fs, channels=2, callback=audio_callback)
        recording.start()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to pause/resume recording
def pause_recording():
    global paused
    if recording:
        paused = not paused
        if paused:
            messagebox.showinfo("Paused", "Recording paused.")
        else:
            messagebox.showinfo("Resumed", "Recording resumed.")

# Function to stop recording
def stop_recording():
    global recording, recorded_data, file_name
    if recording:
        recording.stop()
        recording.close()
        recording = None
        messagebox.showinfo("Recording", "Recording stopped!")

        # Save the recordings
        wav_file = f"{file_name}.wav"
        wavio_file = f"{file_name}_wavio.wav"

        if os.path.exists(wav_file):
            os.remove(wav_file)  # Remove the file if it exists
        if os.path.exists(wavio_file):
            os.remove(wavio_file)  # Remove the file if it exists

        final_recording = np.concatenate(recorded_data, axis=0)
        write(wav_file, fs, final_recording)  # Save as WAV file
        wv.write(wavio_file, final_recording, fs, sampwidth=2)  # Save using wavio

        messagebox.showinfo("Success", f"Recording saved as {wav_file} and {wavio_file}!")

# Audio callback function
def audio_callback(indata, frames, time, status):
    global paused, recorded_data
    if not paused:
        recorded_data.append(indata.copy())

# Create the GUI
root = tk.Tk()
root.title("Sound Recorder")

# Set the window size
root.geometry("400x250")

# Add a label
label = tk.Label(root, text="Sound Recorder", font=("Arial", 16))
label.pack(pady=10)

# Add a button to start recording
start_button = tk.Button(root, text="Start Recording", command=start_recording, font=("Arial", 12), bg="green", fg="white")
start_button.pack(pady=10)

# Add a button to pause/resume recording
pause_button = tk.Button(root, text="Pause/Resume Recording", command=pause_recording, font=("Arial", 12), bg="orange", fg="white")
pause_button.pack(pady=10)

# Add a button to stop recording
stop_button = tk.Button(root, text="Stop Recording", command=stop_recording, font=("Arial", 12), bg="red", fg="white")
stop_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
