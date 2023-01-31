import tkinter as tk
from tkinter import ttk
import LED_control

def toggle_pattern():
    global is_running
    if is_running:
        LED_control.stop()
        btn_start_stop.config(text="Start")
        is_running = False
    else:
        LED_control.start(pattern_var.get())
        btn_start_stop.config(text="Stop")
        is_running = True

root = tk.Tk()
root.title("LED Control")

pattern_var = tk.StringVar()
pattern_var.set("slide")

lbl_pattern = ttk.Label(root, text="Pattern:")
lbl_pattern.grid(row=0, column=0, sticky="W")

rb_slide = ttk.Radiobutton(root, text="Slide", variable=pattern_var, value="slide")
rb_slide.grid(row=1, column=0, sticky="W")

rb_blink = ttk.Radiobutton(root, text="Blink", variable=pattern_var, value="blink")
rb_blink.grid(row=2, column=0, sticky="W")

btn_start_stop = ttk.Button(root, text="Start", command=toggle_pattern)
btn_start_stop.grid(row=3, column=0)

is_running = False

root.mainloop()

