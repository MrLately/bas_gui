import time
import board
import neopixel
import signal
import sys
import LED_gui

color, slide_wait, blink_wait, block_size, brightness = LED_gui.get_parameters()

pixel_pin = board.D18
num_pixels = 60
ORDER = neopixel.GRB
global pixels
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER)


def handle_keyboard_interrupt(signum, frame):
    pixels.fill((0, 0, 0,))
    pixels.show()
    print("exiting")
    sys.exit(0)
    
signal.signal(signal.SIGINT, handle_keyboard_interrupt)


def slide_pattern(color, slide_wait, block_size):
    for i in range(0, num_pixels, block_size):
        pixels.fill((0, 0, 0))
        for j in range(block_size):
            if i + j < num_pixels:
                pixels[i + j] = color
        pixels.show()
        time.sleep(slide_wait)
    for i in range(num_pixels - block_size, -1, -block_size):
        pixels.fill((0, 0, 0))
        for j in range(block_size):
            if i + j < num_pixels:
                pixels[i + j] = color
        pixels.show()
        time.sleep(slide_wait)

def blink_pattern(color, blink_wait, block_size):
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

