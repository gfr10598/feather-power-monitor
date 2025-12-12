"""
CircuitPython program for Adafruit Feather ESP32-S2 with 2.4" TFT Display
Displays "Hello World" and a scrolling sine wave
"""

import board
import displayio
import terminalio
import time
import math
from adafruit_display_text import label
from adafruit_st7789 import ST7789

# Release any previously used displays
displayio.release_displays()

# Setup SPI for the display
spi = board.SPI()

# Display pins - typical for 2.4" TFT FeatherWing
tft_cs = board.D5
tft_dc = board.D6

# Create the display bus
display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs
)

# Create the ST7789 display (2.4" TFT, 240x320 pixels)
display = ST7789(
    display_bus,
    width=240,
    height=320,
    rotation=0,
    rowstart=80  # Offset for 2.4" display
)

# Create a display group
main_group = displayio.Group()

# Create a background color (black)
color_bitmap = displayio.Bitmap(240, 320, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000  # Black
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)

# Add "Hello World" text at the top
text_area = label.Label(
    terminalio.FONT,
    text="Hello World",
    color=0xFFFFFF,  # White
    scale=3
)
text_area.x = 20
text_area.y = 20
main_group.append(text_area)

# Create a bitmap for the sine wave (scrolling area)
wave_height = 200
wave_width = 240
wave_bitmap = displayio.Bitmap(wave_width, wave_height, 3)
wave_palette = displayio.Palette(3)
wave_palette[0] = 0x000000  # Black (background)
wave_palette[1] = 0x00FF00  # Green (sine wave)
wave_palette[2] = 0x0000FF  # Blue (grid lines)

wave_sprite = displayio.TileGrid(
    wave_bitmap,
    pixel_shader=wave_palette,
    x=0,
    y=100
)
main_group.append(wave_sprite)

# Show the display group
display.show(main_group)

# Sine wave parameters
x_offset = 0
amplitude = 80  # Amplitude of the sine wave
frequency = 2  # Frequency of the sine wave
center_y = wave_height // 2

def draw_grid():
    """Draw a simple grid on the wave area"""
    # Draw horizontal center line
    for x in range(wave_width):
        wave_bitmap[x, center_y] = 2

def clear_wave():
    """Clear the wave area"""
    for y in range(wave_height):
        for x in range(wave_width):
            wave_bitmap[x, y] = 0
    draw_grid()

def draw_sine_wave(offset):
    """Draw a sine wave across the display with given x offset"""
    for x in range(wave_width):
        # Calculate sine value
        angle = ((x + offset) % wave_width) * frequency * 2 * math.pi / wave_width
        y_value = int(center_y + amplitude * math.sin(angle))
        
        # Ensure y_value is within bounds
        if 0 <= y_value < wave_height:
            wave_bitmap[x, y_value] = 1

# Main loop - scroll the sine wave
print("Starting sine wave display...")

while True:
    # Clear and redraw the wave with updated offset
    clear_wave()
    draw_sine_wave(x_offset)
    
    # Update the offset to create scrolling effect
    x_offset = (x_offset + 2) % wave_width
    
    # Small delay to control scroll speed
    time.sleep(0.05)
