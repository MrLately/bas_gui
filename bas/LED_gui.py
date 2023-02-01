import tkinter as tk
from tkinter import ttk
import LED_control
from tkinter.colorchooser import askcolor

root = tk.Tk()
root.title("LED Control")
root.geometry("480x320")

def choose_color():
    global color
    color = askcolor()[0]

color = (255, 0, 0)

def toggle_pattern():
    global is_running
    if is_running:
        is_running = False
        btn_start_stop.config(text="Start")
        start_pattern()
    else:
        is_running = True
        btn_start_stop.config(text="Stop")
        stop_pattern()

is_running = False

def start_pattern():
    LED_control.slide_wait = slide_wait_slider.get()
    LED_control.blink_wait = blink_wait_slider.get()
    LED_control.block_size = block_size_slider.get()
    LED_control.brightness = brightness_slider.get()
    LED_control.color = color
    
    if pattern_var.get() == 1:
        LED_control.slide_pattern()
    else:
        LED_control.blink_pattern()
        
def stop_pattern():
    LED_control.pixels.fill((0, 0, 0,))
    LED_control.pixels.show()

pattern_var = tk.IntVar()
pattern_var.set(1)

slide_pattern_rb = tk.Radiobutton(root, text="Slide Pattern", variable=pattern_var, value=1)
slide_pattern_rb.grid(row=0, column=3, padx=10)

blink_pattern_rb = tk.Radiobutton(root, text="Blink Pattern", variable=pattern_var, value=2)
blink_pattern_rb.grid(row=1, column=3, padx=10)

slide_wait_label = tk.Label(root, text="Slide Speed")
slide_wait_label.grid(row=0, column=0, pady=5)

slide_wait_slider = tk.Scale(root, from_=0.0, to=5.0, resolution=0.01, orient=tk.HORIZONTAL)
slide_wait_slider.grid(row=1, column=0, pady=5)

blink_wait_label = tk.Label(root, text="Blink Speed")
blink_wait_label.grid(row=2, column=0, pady=5)

blink_wait_slider = tk.Scale(root, from_=0.0, to=5.0, resolution=0.01, orient=tk.HORIZONTAL)
blink_wait_slider.grid(row=3, column=0, pady=5)

block_size_label = tk.Label(root, text="Block Size")
block_size_label.grid(row=0, column=2, pady=5)

block_size_slider = tk.Scale(root, from_=1, to=30, orient=tk.HORIZONTAL)
block_size_slider.grid(row=1, column=2, pady=5)

brightness_label = tk.Label(root, text="Brightness")
brightness_label.grid(row=2, column=2, pady=5)

brightness_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL)
brightness_slider.grid(row=3, column=2, pady=5)

btn_start_stop = ttk.Button(root, text="Start", command=toggle_pattern)
btn_start_stop.grid(row=3, column=3, rowspan=8, pady=10)

btn_choose_color = ttk.Button(root, text="Choose Color", command=choose_color)
btn_choose_color.grid(row=2, column=3, sticky=tk.E)

root.mainloop()
