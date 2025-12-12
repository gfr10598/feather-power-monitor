# feather-power-monitor
Adafruit based power monitoring device code.

## Hardware Requirements

- **Adafruit Feather ESP32-S2** - Main microcontroller board
- **2.4" TFT FeatherWing** - ST7789 display (240x320 pixels)

## Features

This CircuitPython program displays:
- "Hello World" text at the top of the screen
- A scrolling sine wave animation in the main display area

## Setup Instructions

### 1. Install CircuitPython

1. Download the latest CircuitPython firmware for the Feather ESP32-S2 from [circuitpython.org](https://circuitpython.org/board/adafruit_feather_esp32s2/)
2. Follow the installation instructions to flash CircuitPython onto your Feather ESP32-S2

### 2. Install Required Libraries

Download the latest CircuitPython library bundle from [circuitpython.org/libraries](https://circuitpython.org/libraries) and copy the following libraries to the `lib` folder on your CIRCUITPY drive:

- `adafruit_st7789.mpy` - Display driver for ST7789
- `adafruit_display_text/` - Text display library

### 3. Upload the Code

1. Connect your Feather ESP32-S2 to your computer via USB
2. Copy `code.py` to the root of the CIRCUITPY drive
3. The program will automatically start running

### 4. Hardware Connections

The 2.4" TFT FeatherWing plugs directly onto the Feather ESP32-S2 headers. The code uses the standard connections:
- **CS**: D5
- **DC**: D6
- **SPI**: Standard SPI pins (MOSI, MISO, SCK)

## Customization

You can modify the following parameters in `code.py`:

- **Wave amplitude**: Change `amplitude = 80` to adjust the height of the sine wave
- **Wave frequency**: Change `frequency = 2` to adjust how many complete waves are shown
- **Scroll speed**: Adjust `time.sleep(0.05)` to change the animation speed
- **Text**: Modify `text="Hello World"` to display different text
- **Colors**: Update the palette values to change colors (e.g., `0x00FF00` for green)

## Troubleshooting

- **Display shows nothing**: Check that the FeatherWing is properly seated on the headers
- **ImportError**: Ensure all required libraries are in the `lib` folder
- **Wrong display driver**: If using a different TFT display, you may need to change the driver (e.g., from ST7789 to ILI9341)

## License

This project is open source and available for modification and distribution.
