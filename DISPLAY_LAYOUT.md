# Display Layout

This document describes the layout of the 2.4" TFT display (240x320 pixels).

## Screen Layout

```
┌────────────────────────────────┐
│  Hello World (White, Large)    │ Y: 0-80
├────────────────────────────────┤
│                                 │
│    ╱╲        ╱╲        ╱╲       │
│   ╱  ╲      ╱  ╲      ╱  ╲      │ Y: 100-300
│  ╱    ╲    ╱    ╲    ╱    ╲     │ (Wave Area)
│ ╱      ╲  ╱      ╲  ╱      ╲    │
│───────────────────────────────── │ Center line (Blue)
│        ╲╱        ╲╱        ╲╱   │
│                                 │
└────────────────────────────────┘
```

## Display Elements

### 1. "Hello World" Text
- **Position**: Top of screen (X: 20, Y: 20)
- **Font**: Terminal (Built-in)
- **Scale**: 3x (Large)
- **Color**: White (0xFFFFFF)

### 2. Sine Wave Display
- **Position**: Y: 100-300 (200 pixels high)
- **Width**: Full width (240 pixels)
- **Wave Color**: Green (0x00FF00)
- **Grid Color**: Blue (0x0000FF)
- **Background**: Black (0x000000)

### 3. Wave Animation
- **Type**: Scrolling from right to left
- **Frequency**: 2 complete waves visible at once
- **Amplitude**: 80 pixels (±80 from center)
- **Scroll Speed**: Updates every 0.05 seconds
- **Scroll Distance**: 2 pixels per frame

## Technical Specifications

- **Display Driver**: ST7789
- **Resolution**: 240x320 pixels
- **Interface**: SPI
- **Control Pins**:
  - CS (Chip Select): D5
  - DC (Data/Command): D6
- **Row Start Offset**: 80 (specific to 2.4" display panel)

## Color Codes

- Background: `0x000000` (Black)
- Text: `0xFFFFFF` (White)
- Sine Wave: `0x00FF00` (Green)
- Grid Lines: `0x0000FF` (Blue)

## Performance Notes

- The wave is redrawn every 50ms (20 FPS)
- Each frame clears the previous wave and draws a new one
- The center grid line provides a visual reference point
