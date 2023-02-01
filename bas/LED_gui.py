import tkinter as tk
from tkinter import ttk
import LED_control

root = tk.Tk()
root.title("LED Control")
root.geometry("320x240")

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
btn_start_stop = ttk.Button(root, text="Start", command=toggle_pattern)
btn_start_stop.pack()

def start_pattern():
    LED_control.slide_wait = slide_wait_slider.get()
    LED_control.blink_wait = blink_wait_slider.get()
    LED_control.block_size = block_size_slider.get()
    LED_control.brightness = brightness_slider.get()
    
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
slide_pattern_rb.pack()

blink_pattern_rb = tk.Radiobutton(root, text="Blink Pattern", variable=pattern_var, value=2)
blink_pattern_rb.pack()

slide_wait_label = tk.Label(root, text="Slide Wait")
slide_wait_label.pack()

slide_wait_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL)
slide_wait_slider.pack()

blink_wait_label = tk.Label(root, text="Blink Wait")
blink_wait_label.pack()

blink_wait_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL)
blink_wait_slider.pack()

block_size_label = tk.Label(root, text="Block Size")
block_size_label.pack()

block_size_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
block_size_slider.pack()

brightness_label = tk.Label(root, text="Brightness")
brightness_label.pack()

brightness_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL)
brightness_slider.pack()

root.mainloop()
