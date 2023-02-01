import time
import board
import neopixel
import signal
import sys

def handle_keyboard_interrupt(signum, frame):
    pixels.fill((0, 0, 0,))
    pixels.show()
    print("exiting")
    sys.exit(0)
    
signal.signal(signal.SIGINT, handle_keyboard_interrupt)
                              
pixel_pin = board.D18
num_pixels = 60
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

color = (0, 255, 0)
slide_wait = 0.05
blink_wait = 0.5
block_size = 2

def slide_pattern():
    for i in range(0, num_pixels, block_size):
        pixels.fill((0, 0, 0))
        for j in range(block_size):
            if i + j < num_pixels:
                pixels[i + j] = color
        pixels.show()
        time.sleep(slide_wait)
    for i in range(num_pixels - block_size, -block_size, -block_size):
        pixels.fill((0, 0, 0))
        for j in range(block_size):
            if i + j < num_pixels:
                pixels[i + j] = color
        pixels.show()
        time.sleep(slide_wait)

def blink_pattern():
    while True:
        pixels.fill((0, 0, 0))
        for i in range(block_size):
            pixels[i] = color
        pixels.show()
        time.sleep(blink_wait)
        pixels.fill((0, 0, 0))
        for i in range(num_pixels - block_size, num_pixels):
            pixels[i] = color
        pixels.show()
        time.sleep(blink_wait)
        pixels.fill((0, 0, 0))
        pixels[0] = color
        pixels.show()
        time.sleep(blink_wait)
        pixels.fill((0, 0, 0))
        pixels[num_pixels - 1] = color
        pixels.show()
        time.sleep(blink_wait)
