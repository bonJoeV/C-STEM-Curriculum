# Advanced C-STEM Escape Room: Mission to Unlock the Cathedral Code

**Overview**: A 60-90 minute escape room for 3-5 advanced 5th/6th grade boys at a Catholic school, using Sphero BOLT+, Tinkercad, Snap Circuits, Scratch, GarageBand, Keva planks, and QR codes. The challenges are designed to be engaging and difficult but solvable, leveraging the boys’ prior experience. The goal is to unlock the "Cathedral Code" and retrieve the "Relic of St. Francis."

**Theme**: Recover the "Relic of St. Francis" from a cathedral vault by solving STEM puzzles inspired by his teachings.

## Setup

- **Room Layout**: 4 stations in a classroom, each with a challenge and hidden QR code. Stations are completed sequentially.
- **Team**: One team of 3-5 boys.
- **Total Time**: 60-90 minutes (15-18 minutes per station, plus intro and debrief).
- **Materials**:
  - 1 Sphero BOLT+ (with light sensor, LCD screen, Roll to Distance block)
  - 1 iPad (Sphero Edu app, GarageBand, QR scanner/Google Lens)
  - 2-3 Chromebooks (Tinkercad, Scratch, QR scanning)
  - Snap Circuits Extreme SC-750R kit
  - 100 Keva planks
  - 4 QR code printouts (2x2 inches)
  - Decorated box (vault) with combination lock or latch
  - Reward: St. Francis medal or cross, Catholic-themed stickers/bookmarks
  - Timer/countdown clock
  - Paper/pens for notes
  - Optional: Soft Gregorian chant music (e.g., YouTube playlist)
- **QR Codes**: Create 4 QR codes using [QRCodeMonkey](https://www.qrcode-monkey.com/), linking to Google Docs with clues (see QR Code Creation below).
- **Narrative**: "The Relic of St. Francis is locked in the cathedral vault, protected by ancient STEM challenges. Thieves are closing in! Use St. Francis’ clues to unlock the code and save the relic!"
- **Preparation**:
  - Pre-login Tinkercad accounts on Chromebooks.
  - Charge Sphero BOLT+ and iPad.
  - Test all QR codes and station setups.

## Stations and Challenges

### Station 1: Sphero BOLT+ Sensor Maze with LCD Feedback
- **Objective**: Program the Sphero BOLT+ to navigate a Keva plank maze using the light sensor and Roll to Distance block, displaying "FOUND" on the LCD when reaching the QR code.
- **Setup**:
  - Build a 3x3 ft maze with 40 Keva planks (4 turns, 1 dead-end, 8 cm narrow passage, dark section covered by a book or cloth).
  - Place QR code at the end (taped to a plank).
  - Provide iPad with Sphero Edu app.
- **Challenge**:
  1. Use the light sensor to pause in the dark section (luminosity < 100 lux).
  2. Use Roll to Distance for precise navigation (e.g., 50 cm forward, 90° turn).
  3. Display "FOUND" on the 128x128 LCD after traveling ~150 cm.
  - **Path**: Roll 50 cm, right 90°, 40 cm, left 45°, 30 cm (narrow), pause in dark, 30 cm to QR.
- **Sample Code** (Sphero Edu Blocks):
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
- **QR Clue**: "Craft a sacred key to unlock divine wisdom." (Leads to Station 2.)
- **Catholic Tie**: Navigating darkness reflects St. Francis’ faith guiding him through trials.
- **Difficulty Check**: Challenging due to sensor use and precise distances, but achievable with sample code and a simplified maze (fewer turns than expert-level designs).
- **Frustration Prevention**: Provide a maze diagram and a manual coding option if sensors fail.

### Station 2: Tinkercad Complex Key Design
- **Objective**: Design a 3D key in Tinkercad with a cross handle and notched blade, matching a reference to earn the QR code.
- **Setup**:
  - Chromebook with Tinkercad logged in.
  - Reference image: Cylinder handle (2 cm diameter, 1 cm height), cross top (two 1x0.5x0.5 cm bars), blade (4 cm long, 1 cm wide, 0.5 cm thick), three 0.5 cm triangular notches.
  - Teacher holds QR code, given after design approval.
- **Challenge**:
  1. Create cylinder handle: 20 mm diameter, 10 mm height.
  2. Add cross: Two 10x5x5 mm boxes, rotated 90° apart.
  3. Attach blade: 40x10x5 mm box.
  4. Add three triangular notches: 5x5x5 mm holes, spaced 8 mm apart on blade.
  5. Group and show teacher.
- **Sample Instructions**:
  ```
  1. Start a new Tinkercad design.
  2. Drag a cylinder: Set diameter to 20 mm, height to 10 mm.
  3. Add cross: Two boxes (10x5x5 mm), place on top, rotate one 90°.
  4. Add blade: Box (40x10x5 mm), align with cylinder base.
  5. Create notches: Three triangular holes (5x5x5 mm), position at 8, 16, 24 mm along blade.
  6. Group all parts, show teacher.
  ```
- **QR Clue**: "Forge a circuit to illuminate the path to peace." (Leads to Station 3.)
- **Catholic Tie**: The cross handle symbolizes St. Francis’ devotion to Christ.
- **Difficulty Check**: Complex due to precise notch placement and 3D assembly, but manageable with step-by-step guidance.
- **Frustration Prevention**: Include a reference image and optional pre-built handle hint.

### Station 3: Snap Circuits OR Gate Circuit
- **Objective**: Build an OR gate circuit with Snap Circuits to light two LEDs, revealing the QR code.
- **Setup**:
  - Snap Circuits Extreme SC-750R kit.
  - Diagram for OR gate (similar to Project #176): Two switches, OR gate (U2), two LEDs (red D1, green D2), resistors (R1, R2).
  - QR code hidden under paper, visible when both LEDs light (use a dark corner or flashlight).
- **Challenge**:
  - Build circuit where either or both switches light the LEDs.
  - Debug if LEDs don’t light.
- **Sample Circuit Diagram**:
  ```
  Components: 3V Battery, Switch (S1), Switch (S2), OR Gate (U2), LED Red (D1), LED Green (D2), Resistor 100Ω (R1, R2)
  Connections:
  - Battery (+) to S1 and S2
  - S1 to OR Gate Input 1
  - S2 to OR Gate Input 2
  - OR Gate Output to R1 and R2
  - R1 to D1 (+), R2 to D2 (+)
  - D1 (-) and D2 (-) to Battery (-)
  ```
- **QR Clue**: "Compose a hymn to echo divine praise." (Leads to Station 4.)
- **Catholic Tie**: The OR gate’s inclusivity mirrors St. Francis’ love for all creation.
- **Difficulty Check**: Challenging due to logic gate use and debugging, but familiar components keep it doable.
- **Frustration Prevention**: Provide a labeled diagram and troubleshooting tips (e.g., check switch connections).

### Station 4: Scratch + GarageBand Hymn Creation
- **Objective**: Code a hymn-like tune in Scratch with a cross animation, then recreate it in GarageBand to earn the QR code.
- **Setup**:
  - Chromebook with Scratch (https://scratch.mit.edu/).
  - iPad with GarageBand.
  - Tune: C-E-G-C-E-G (MIDI 60-64-67-60-64-67, start of "Amazing Grace"), rhythm: quarter, quarter, half, quarter, quarter, whole.
  - Teacher holds QR code, given after verifying both Scratch and GarageBand outputs.
- **Challenge**:
  1. In Scratch: Code the tune and animate a drawn cross sprite growing with each note.
  2. In GarageBand: Record the tune using the piano.
- **Sample Scratch Code**:
  ```
  When Green Flag Clicked
  Set Instrument to Piano
  Set Size to 50%
  Repeat 6:
    If Note = 1 or 2 or 4 or 5:
      Play Note [60,64,60,64] for 0.5 beats
      Change Size by 10
    If Note = 3:
      Play Note 67 for 1.0 beats
      Change Size by 20
    If Note = 6:
      Play Note 67 for 2.0 beats
      Change Size by 30
  ```
- **GarageBand Instructions**:
  ```
  1. Open GarageBand, select Keyboard (Grand Piano).
  2. Record: C4 (quarter), E4 (quarter), G4 (half), C4 (quarter), E4 (quarter), G4 (whole).
  3. Play back, show teacher.
  ```
- **QR Clue**: "The Cathedral Code is FRANCIS. Enter it to save the relic!"
- **Catholic Tie**: The hymn echoes St. Francis’ Canticle of the Sun.
- **Difficulty Check**: Coding and animation are advanced, but the familiar tune and MIDI chart make it approachable.
- **Frustration Prevention**: Provide a MIDI note chart (C4=60, E4=64, G4=67) and allow skipping GarageBand if time runs short.

## Final Challenge
- **Objective**: Enter the code "FRANCIS" to open the vault.
- **Setup**:
  - Decorated box with a latch or simple combination lock (set to "FRANCIS" if possible).
  - Inside: St. Francis medal or cross, plus stickers/bookmarks.
- **Task**: Submit "FRANCIS" via Google Form on iPad or write it for the teacher to unlock the box.
- **Debrief**: Reflect on STEM skills, teamwork, and St. Francis’ values (e.g., "All the darkness in the world cannot extinguish the light of a single candle.").

## Timing
- **Intro/Story**: 5 minutes
- **Stations**: 15-18 minutes each (4 x 15-18 = 60-72 minutes)
- **Final Challenge + Debrief**: 10 minutes
- **Total**: ~75-87 minutes

## QR Code Creation
- **Steps**:
  1. Create 4 Google Docs (teacher account, "view only") with these clues:
     - Station 1: "Craft a sacred key to unlock divine wisdom."
     - Station 2: "Forge a circuit to illuminate the path to peace."
     - Station 3: "Compose a hymn to echo divine praise."
     - Station 4: "The Cathedral Code is FRANCIS. Enter it to save the relic!"
  2. Get shareable links for each Doc.
  3. Generate QR codes at [QRCodeMonkey](https://www.qrcode-monkey.com/), download as PNGs.
  4. Print 2x2 inches, hide at stations (e.g., taped to plank, under paper).
- **Test**: Scan with Google Lens to confirm links work.

## Everything You Need
### Materials Checklist
- **Hardware**:
  - Sphero BOLT+ (charged)
  - iPad (Sphero Edu, GarageBand, Google Lens)
  - 2-3 Chromebooks (Tinkercad, Scratch)
  - Snap Circuits Extreme SC-750R kit
  - 100 Keva planks
  - Decorated box (vault)
  - St. Francis medal/cross, stickers/bookmarks
- **Printouts**:
  - 4 QR codes (2x2 inches)
  - Maze diagram (Station 1)
  - Key reference image (Station 2)
  - OR gate diagram (Station 3)
  - MIDI note chart (Station 4)
- **Other**:
  - Timer/clock
  - Paper/pens
  - Optional: Book/cloth for maze dark section, flashlight

### Instructions Handout
```
**Mission to Unlock the Cathedral Code**
1. Station 1 (Sphero BOLT+): Code BOLT+ to navigate the maze with light sensor and LCD. Scan QR at end.
2. Station 2 (Tinkercad): Design a notched key with a cross handle. Show teacher for QR.
3. Station 3 (Snap Circuits): Build an OR gate circuit to light two LEDs. Find QR under paper.
4. Station 4 (Scratch + GarageBand): Code a hymn in Scratch with a cross animation, record in GarageBand. Show both for QR.
5. Final Challenge: Enter the Cathedral Code to open the vault!
Hints: Two hint cards available—use wisely!
```

### Additional Tips
- **Test Run**: Complete each station in 15-18 minutes to verify pacing.
- **Hints** (on cards):
  - Station 1: "Check light sensor threshold (<100 lux) or use manual distances."
  - Station 2: "Align notches at 8, 16, 24 mm on blade."
  - Station 3: "Ensure OR gate (U2) connects to both LEDs."
  - Station 4: "Use MIDI chart: C4=60, E4=64, G4=67."
- **Roles for 5 Boys**: Lead coder (Sphero/Scratch), builder (Keva/Snap Circuits), designer (Tinkercad), debugger, note-taker.
- **Safety**:
  - Secure Keva maze to prevent tipping.
  - Check Snap Circuits for loose connections.
  - Use a flat surface for BOLT+.
- **Adjustments**:
  - Extra Challenge: Add a fourth Tinkercad notch or BOLT+ LCD animation.
  - Time Saver: Skip GarageBand, use Scratch tune only.

## Resources
- [Sphero Edu](https://edu.sphero.com/)
- [Tinkercad](https://www.tinkercad.com/)
- [Scratch](https://scratch.mit.edu/)
- [Snap Circuits Manuals](https://www.elenco.com/manuals/)
- [QRCodeMonkey](https://www.qrcode-monkey.com/)
- Google Lens (pre-installed on iPad)

## Final Notes
The challenges are tuned for advanced students: Sphero sensor coding, Tinkercad precision, logic circuits, and multimedia coding. Clear instructions, sample code, and hints ensure they’re not frustrating. The Catholic theme ties it together, making it a rewarding experience. Test the full setup beforehand to confirm timing and functionality!
