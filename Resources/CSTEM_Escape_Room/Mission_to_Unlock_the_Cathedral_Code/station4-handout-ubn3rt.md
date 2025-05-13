# Station 4 Handout: Scratch + GarageBand Hymn Creation

<img src="https://raw.githubusercontent.com/bonJoeV/C-STEM-Curriculum/refs/heads/main/logo.jpg" width="150" height="150" alt="Our Lady of the Prairie Catholic School Logo">

**Mr. Vandermark's C-STEM Escape Room 2025**  
*Our Lady of the Prairie Catholic School*

## Objective
Code a hymn-like tune in Scratch with a cross animation, then record it in GarageBand to earn the QR code.

## Instructions
- **Scratch (Chromebook, https://scratch.mit.edu/):**
  - Draw a cross sprite (two bars forming a cross).
  - Code the tune: C-E-G-C-E-G (MIDI 60-64-67-60-64-67).
  - Rhythm: Quarter, quarter, half, quarter, quarter, whole.
  - Animate the cross to grow with each note.
- **GarageBand (iPad):**
  - Select Grand Piano, record: C4 (quarter), E4 (quarter), G4 (half), C4 (quarter), E4 (quarter), G4 (whole).
- Show both to the teacher.

## Sample Scratch Code
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

## MIDI Note Chart
- C4 = 60
- E4 = 64
- G4 = 67

## Catholic Connection
Your hymn echoes St. Francis’ Canticle of the Sun, praising God’s creation.