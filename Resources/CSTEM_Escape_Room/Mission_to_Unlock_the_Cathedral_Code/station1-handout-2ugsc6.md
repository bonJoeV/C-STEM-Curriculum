# Station 1 Handout: Sphero BOLT+ Sensor Maze

<img src="https://raw.githubusercontent.com/bonJoeV/C-STEM-Curriculum/refs/heads/main/logo.jpg" width="150" height="150" alt="Our Lady of the Prairie Catholic School Logo">

**Mr. Vandermark's C-STEM Escape Room 2025**  
*Our Lady of the Prairie Catholic School*

## Objective
Program your Sphero BOLT+ to navigate a Keva plank maze using its light sensor, displaying "FOUND" on the LCD when reaching the QR code.

## Instructions
- Setup a simple maze 3x3 ft with at least 4 turns and one dark section
- Use the Sphero Edu app on the iPad to code the BOLT+.
- Navigate the maze (~150 cm): 50 cm forward, right 90°, 40 cm forward, left 45°, 30 cm through narrow passage (8 cm), pause in dark section, 30 cm to QR.
- Use the light sensor to pause in the dark section (luminosity < 100 lux) for 1 second.
- Use Roll to Distance for precise moves.
- Display "FOUND" on the LCD at the end.
- Scan the QR code with Google Lens for the next clue.

## Sample Code (Sphero Edu Blocks)
```
Start
Set Speed to 40
Set LCD Text "START" for 2s
Loop Until Distance > 150 cm:
  If Light Sensor < 100 lux:
    Pause 1s
    Set LCD Text "DARK" for 1s
  Else:
    Roll to Distance 10 cm
  If Infrared Sensor < 10 cm:
    Turn Left 45 degrees
Set LCD Text "FOUND" for 5s
Play Sound "Victory"
Stop
```

## Catholic Connection
Like St. Francis trusting God in dark times, guide your Sphero with faith and precision.

