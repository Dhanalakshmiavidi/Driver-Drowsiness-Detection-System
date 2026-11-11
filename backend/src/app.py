"""import tkinter as tk
import subprocess

def start():
    subprocess.Popen(["python", "main.py"])

def stop():
    root.destroy()

root = tk.Tk()
root.title("Driver Drowsiness System")
root.geometry("300x200")

label = tk.Label(root, text="Drowsiness Detection", font=("Arial", 14))
label.pack(pady=20)

start_btn = tk.Button(root, text="Start", command=start, bg="green", fg="white")
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Exit", command=stop, bg="red", fg="white")
stop_btn.pack(pady=10)

root.mainloop()"""

"""import tkinter as tk
import subprocess

def start():
    subprocess.Popen(["python", "main.py"])

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("DriveSafe AI 🚗")
root.geometry("300x200")

label = tk.Label(root, text="Drowsiness Detection System", font=("Arial", 12))
label.pack(pady=20)

start_btn = tk.Button(root, text="Start", command=start, bg="green", fg="white")
start_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=exit_app, bg="red", fg="white")
exit_btn.pack(pady=10)

root.mainloop()"""




import tkinter as tk
import subprocess

def start():
    subprocess.Popen(["python", "main.py"])

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("DriveSafe AI 🚗")
root.geometry("300x200")

label = tk.Label(root, text="Drowsiness Detection System", font=("Arial", 12))
label.pack(pady=20)

start_btn = tk.Button(root, text="Start", command=start, bg="green", fg="white")
start_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=exit_app, bg="red", fg="white")
exit_btn.pack(pady=10)

root.mainloop()