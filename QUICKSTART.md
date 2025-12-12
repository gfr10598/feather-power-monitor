# Quick Start Guide

## What This Program Does

This CircuitPython program creates an animated display with two main elements:

1. **"Hello World" Text** - Static white text displayed at the top of the screen in large font
2. **Scrolling Sine Wave** - A green sine wave that continuously scrolls from right to left with a blue center reference line

## Visual Preview

```
┌─────────────────────────────────────────┐
│                                          │
│   Hello World                            │  <- Large white text
│                                          │
├─────────────────────────────────────────┤
│           ╱╲         ╱╲         ╱╲       │
│          ╱  ╲       ╱  ╲       ╱  ╲      │
│         ╱    ╲     ╱    ╲     ╱    ╲     │  <- Green sine wave
│        ╱      ╲   ╱      ╲   ╱      ╲    │     (animated, scrolling)
│───────────────────────────────────────────│  <- Blue center line
│               ╲ ╱        ╲ ╱        ╲ ╱  │
│                ╲          ╲          ╲    │
│                 ╲          ╲          ╲   │
│                                          │
│                                          │
└─────────────────────────────────────────┘
   240 pixels wide x 320 pixels tall
```

## Hardware Setup

### Required Components:
1. **Adafruit Feather ESP32-S2** board
2. **2.4" TFT FeatherWing Display** (ST7789 driver, 240x320 resolution)
3. USB cable for power and programming

### Assembly:
Simply plug the TFT FeatherWing onto the Feather ESP32-S2 headers - no wiring required!

## Software Setup

### Step 1: Install CircuitPython
1. Download CircuitPython 8.x for Feather ESP32-S2 from circuitpython.org
2. Put the board in bootloader mode (double-press the RESET button)
3. Drag the .UF2 file to the FTHRS2BOOT drive
4. The board will reboot and appear as CIRCUITPY drive

### Step 2: Install Libraries
Download the CircuitPython library bundle and copy these to the `lib` folder:
- `adafruit_st7789.mpy`
- `adafruit_display_text/` (entire folder)

### Step 3: Upload Code
Copy `code.py` to the root of the CIRCUITPY drive. The program starts automatically!

## Customization Tips

### Change the Text
Line 60: `text="Hello World"` → Change to any text you like

### Adjust Wave Appearance
- Line 90: `amplitude = 80` → Change wave height (10-90 recommended)
- Line 91: `frequency = 2` → Change number of waves shown (1-4 works well)

### Adjust Animation Speed
- Line 20: `SCROLL_SPEED = 2` → Change scroll speed (1-5 recommended)
- Line 21: `FRAME_DELAY = 0.05` → Change frame rate (0.02-0.1 recommended)

### Change Colors
- Line 61: `color=0xFFFFFF` → Text color (white by default)
- Line 74: `0x00FF00` → Wave color (green by default)
- Line 75: `0x0000FF` → Grid color (blue by default)

Common color codes:
- Red: `0xFF0000`
- Green: `0x00FF00`
- Blue: `0x0000FF`
- Yellow: `0xFFFF00`
- Cyan: `0x00FFFF`
- Magenta: `0xFF00FF`
- White: `0xFFFFFF`

## Troubleshooting

**Display is blank:**
- Check that the FeatherWing is fully seated in the headers
- Verify CircuitPython is installed (check for CIRCUITPY drive)
- Look for errors in the serial console

**"ImportError" message:**
- Ensure all required libraries are in the `lib` folder
- Check that you have the correct version of the libraries for your CircuitPython version

**Display shows garbage/incorrect image:**
- Try adjusting the `DISPLAY_ROWSTART` value (line 17)
- Some display variants may need different offset values (try 0, 40, or 80)

**Wave is too fast/slow:**
- Adjust `SCROLL_SPEED` for horizontal speed
- Adjust `FRAME_DELAY` to change frame rate

## Technical Details

- **Display Resolution:** 240x320 pixels
- **Display Driver:** ST7789 (SPI interface)
- **Frame Rate:** ~20 FPS (adjustable)
- **Wave Cycles:** 2 complete sine waves
- **Wave Amplitude:** ±80 pixels from center
- **Scroll Speed:** 2 pixels per frame (40 pixels/second at 20 FPS)

## Next Steps

Once you have this working, you can extend it to:
- Display sensor data instead of a static sine wave
- Add multiple waveforms (e.g., square wave, triangle wave)
- Display real-time power monitoring data
- Add buttons for user interaction
- Connect to WiFi to display network data
