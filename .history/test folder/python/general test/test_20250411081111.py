import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os

# Function to start recording
def start_recording():
    try:
        # Ask the user for the file name
        file_name = simpledialog.askstring("Input", "Enter the file name (without extension):")
        if not file_name:
            messagebox.showerror("Error", "File name cannot be empty!")
            return

        duration = 5  # seconds
        fs = 44100  # Sample rate

        # Start recording
        messagebox.showinfo("Recording", "Recording started for 5 seconds...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
        sd.wait()  # Wait until recording is finished
        messagebox.showinfo("Recording", "Recording finished!")

        # Save the recordings
        wav_file = f"{file_name}.wav"
        wavio_file = f"{file_name}_wavio.wav"

        if os.path.exists(wav_file):
            os.remove(wav_file)  # Remove the file if it exists
        if os.path.exists(wavio_file):
            os.remove(wavio_file)  # Remove the file if it exists

        write(wav_file, fs, recording)  # Save as WAV file
        wv.write(wavio_file, recording, fs, sampwidth=2)  # Save using wavio

        messagebox.showinfo("Success", f"Recording saved as {wav_file} and {wavio_file}!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the GUI
root = tk.Tk()
root.title("Sound Recorder")

# Set the window size
root.geometry("300x150")

# Add a label
label = tk.Label(root, text="Sound Recorder", font=("Arial", 16))
label.pack(pady=10)

# Add a button to start recording
record_button = tk.Button(root, text="Start Recording", command=start_recording, font=("Arial", 12), bg="green", fg="white")
record_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
