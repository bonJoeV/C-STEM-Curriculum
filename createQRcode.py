# Project for Mr. Vandermark's OLP C-STEM Class
# Date: April 11, 2025
# Description: This project makes a special picture called a QR code (like a secret puzzle you can scan with your phone).
# We put a cross on the QR code with a carved picture of Jesus, because this is for our Catholic school.
# The QR code takes you to a website when you scan it: https://www.tinkercad.com/things/cPaAjXNjvQ8/edit?returnTo=%2Fclassrooms%2FctHSRICnzpW%2Factivities%2F5oRDx05TFcL&sharecode=1lBvNmMZ9gku40enbZl6CP_VF-42vqPU4iJVznwGtQc
# Tools Used: We used Python (a computer language) with special helpers called Pillow (to draw pictures) and qrcode (to make the QR code).
# How to Run: You need Python on your computer, and you need to install Pillow and qrcode (ask a grown-up to help with "pip install Pillow qrcode").
# Then, run this code, and it will make a picture called "qr_code_with_realistic_crucifix.png". You can scan it with your phone!
# Note for Mr. Vandermark: We made the cross look real with wood lines and knots, and we used a fancy font called Garamond for the "INRI" sign.
# We also made Jesus' hands and feet look more real with fingers and toes, and we picked colors to look like carved wood.

# We need these tools to draw pictures and make a QR code (like a secret code you can scan with your phone)
import qrcode  # This makes the QR code
from PIL import Image, ImageDraw, ImageFont  # These help us draw pictures
import math  # This helps us with some math to make wavy lines

# This is the secret message we want to hide in the QR code (it's a website link)
data = "https://www.tinkercad.com/things/cPaAjXNjvQ8/edit?returnTo=%2Fclassrooms%2FctHSRICnzpW%2Factivities%2F5oRDx05TFcL&sharecode=1lBvNmMZ9gku40enbZl6CP_VF-42vqPU4iJVznwGtQc"

# Let's make the QR code (it's like a black-and-white puzzle)
qr = qrcode.QRCode(
    version=None,  # Let the computer decide the size of the puzzle
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # This makes the puzzle strong so it still works if we draw on it
    box_size=10,  # This makes the puzzle pieces bigger
    border=4  # This adds a white border around the puzzle
)
qr.add_data(data)  # Put the secret message in the puzzle
qr.make(fit=True)  # Finish making the puzzle
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")  # Turn the puzzle into a picture
qr_width, qr_height = qr_img.size  # Find out how big the puzzle picture is

# Let's make a cross to put on the QR code (it will be 1/3 the size of the puzzle)
crucifix_size = qr_width // 3  # This makes the cross smaller than the puzzle
crucifix_img = Image.new("RGBA", (crucifix_size, crucifix_size), (0, 0, 0, 0))  # Make a blank picture for the cross
draw = ImageDraw.Draw(crucifix_img)  # This is like picking up a pencil to draw on the blank picture

# Let's pick colors for the wood (like choosing crayons)
wood_color_main = (139, 69, 19, 255)  # Main wood color (like a brown crayon)
wood_color_highlight = (160, 82, 45, 200)  # Lighter wood color for lines (a lighter brown)
wood_color_shadow = (90, 45, 15, 200)  # Darker wood color for shadows (a darker brown)
wood_color_knot = (100, 50, 20, 255)  # Color for wood knots (like little circles in the wood)
figure_color = (80, 40, 10, 255)  # Color for the carved figure (back to the darker brown)
figure_shadow = (60, 30, 5, 255)  # Color for shadows on the figure (a bit darker)
arm_thickness = (crucifix_size // 5) * 3 // 4  # How thick the cross beams are (we made it 25% smaller)

# Draw the tall part of the cross (the vertical beam)
vertical_rect = [
    (crucifix_size // 2 - arm_thickness // 2, 0),  # Start point (left side of the beam)
    (crucifix_size // 2 + arm_thickness // 2, crucifix_size)  # End point (right side, bottom of the picture)
]
draw.rectangle(vertical_rect, fill=wood_color_main)  # Fill the tall part with the main wood color
draw.line(
    [(crucifix_size // 2 + arm_thickness // 2, 0), (crucifix_size // 2 + arm_thickness // 2, crucifix_size)],
    fill=wood_color_shadow, width=2  # Add a shadow line on the right side to make it look 3D
)

# Draw the wide part of the cross (the horizontal beam)
horizontal_rect = [
    (crucifix_size // 2 - crucifix_size // 3, crucifix_size // 4 - arm_thickness // 2),  # Start point (left side)
    (crucifix_size // 2 + crucifix_size // 3, crucifix_size // 4 + arm_thickness // 2)  # End point (right side)
]
draw.rectangle(horizontal_rect, fill=wood_color_main)  # Fill the wide part with the main wood color
draw.line(
    [(crucifix_size // 2 - crucifix_size // 3, crucifix_size // 4 + arm_thickness // 2),
     (crucifix_size // 2 + crucifix_size // 3, crucifix_size // 4 + arm_thickness // 2)],
    fill=wood_color_shadow, width=2  # Add a shadow line on the bottom to make it look 3D
)

# This function makes wavy lines to look like wood grain (like the lines you see in a tree trunk)
def draw_wavy_grain(start_x, start_y, end_x, end_y, color, width, wave_amplitude=3, wave_frequency=0.05):
    points = []  # This will hold all the points for our wavy line
    length = math.hypot(end_x - start_x, end_y - start_y)  # Find out how long the line is
    steps = int(length)  # How many little steps to draw the line
    # Add some randomness to make each line look different
    wave_amplitude = wave_amplitude + random.uniform(-1, 1)  # Change how big the waves are a little
    wave_frequency = wave_frequency + random.uniform(-0.02, 0.02)  # Change how fast the waves wiggle
    shift = random.uniform(-2, 2)  # Move the line up or down a tiny bit
    for i in range(steps):
        t = i / steps  # This tells us how far along the line we are (0 to 1)
        x = start_x + t * (end_x - start_x)  # Move from start_x to end_x
        y = start_y + t * (end_y - start_y)  # Move from start_y to end_y
        # Make the line wavy like a snake
        offset = math.sin(i * wave_frequency + random.uniform(-0.3, 0.3)) * wave_amplitude
        if end_x != start_x:  # If the line is going side to side
            y += offset + shift  # Wiggle up and down
        else:  # If the line is going up and down
            x += offset + shift  # Wiggle side to side
        points.append((x, y))  # Add this point to our line
    draw.line(points, fill=color, width=width)  # Draw the wavy line

# Add wood grain to the wide part of the cross (horizontal beam)
for i in range(crucifix_size // 4 - arm_thickness // 2, crucifix_size // 4 + arm_thickness // 2, 2):
    draw_wavy_grain(
        crucifix_size // 2 - crucifix_size // 3 + 2, i,  # Start point
        crucifix_size // 2 + crucifix_size // 3 - 2, i,  # End point
        wood_color_highlight if random.random() > 0.3 else wood_color_shadow,  # Pick a light or dark color
        width=1,  # Make the line thin
        wave_amplitude=2 + random.uniform(-0.5, 0.5),  # How big the waves are
        wave_frequency=0.1  # How fast the waves wiggle
    )

# Add wood grain to the tall part of the cross (vertical beam)
for i in range(0, crucifix_size, 2):
    if not (crucifix_size // 4 - arm_thickness // 2 <= i <= crucifix_size // 4 + arm_thickness // 2):  # Skip the part where the beams cross
        draw_wavy_grain(
            crucifix_size // 2 - arm_thickness // 2 + 2, i,  # Start point
            crucifix_size // 2 + arm_thickness // 2 - 2, i,  # End point
            wood_color_highlight if random.random() > 0.3 else wood_color_shadow,  # Pick a light or dark color
            width=1,  # Make the line thin
            wave_amplitude=2 + random.uniform(-0.5, 0.5),  # How big the waves are
            wave_frequency=0.1  # How fast the waves wiggle
        )

# Add little circles to look like knots in the wood (like little bumps on a tree)
for _ in range(3):
    knot_x = random.randint(crucifix_size // 2 - arm_thickness // 2 + 5, crucifix_size // 2 + arm_thickness // 2 - 5)  # Pick a random spot on the tall part
    knot_y = random.randint(arm_thickness, crucifix_size - arm_thickness)  # Pick a random height
    if not (crucifix_size // 4 - arm_thickness // 2 <= knot_y <= crucifix_size // 4 + arm_thickness // 2):  # Skip the crossing part
        draw.ellipse(
            [(knot_x - 3, knot_y - 3), (knot_x + 3, knot_y + 3)],  # Draw a small circle
            fill=wood_color_knot  # Color it like a knot
        )
    knot_x = random.randint(crucifix_size // 2 - crucifix_size // 3 + 5, crucifix_size // 2 + crucifix_size // 3 - 5)  # Pick a random spot on the wide part
    knot_y = random.randint(crucifix_size // 4 - arm_thickness // 2 + 5, crucifix_size // 4 + arm_thickness // 2 - 5)  # Pick a random height
    draw.ellipse(
        [(knot_x - 3, knot_y - 3), (knot_x + 3, knot_y + 3)],  # Draw a small circle
        fill=wood_color_knot  # Color it like a knot
    )

# Let's draw the figure on the cross (like a carved statue)
center_x = crucifix_size // 2  # This is the middle of the picture
figure_width = arm_thickness // 2  # How wide the body parts are
figure_height = crucifix_size // 1.5  # How tall the body is

# Draw the head (like a small circle)
head_y = crucifix_size // 4 + arm_thickness // 4  # Where the head goes
head_radius = figure_width // 2  # How big the head is
draw.ellipse(
    [(center_x - head_radius, head_y - head_radius),
     (center_x + head_radius, head_y + head_radius)],
    fill=figure_color  # Color the head with the darker color
)
# Add a crown of thorns (like a spiky hat)
for angle in range(0, 360, 15):  # Draw little spikes all around the head
    rad = math.radians(angle)  # Turn the angle into a math number
    inner_x = center_x + head_radius * math.cos(rad)  # Start point on the head
    inner_y = head_y + head_radius * math.sin(rad)
    outer_x = center_x + (head_radius + 3 + random.uniform(-1, 1)) * math.cos(rad)  # End point a bit outside
    outer_y = head_y + (head_radius + 3 + random.uniform(-1, 1)) * math.sin(rad)
    draw.line([(inner_x, inner_y), (outer_x, outer_y)], fill=figure_shadow, width=1)  # Draw a spike
for angle in range(0, 360, 30):  # Add crisscross lines to make it look woven
    rad1 = math.radians(angle)
    rad2 = math.radians(angle + 15)
    x1 = center_x + (head_radius + 1) * math.cos(rad1)
    y1 = head_y + (head_radius + 1) * math.sin(rad1)
    x2 = center_x + (head_radius + 1) * math.cos(rad2)
    y2 = head_y + (head_radius + 1) * math.sin(rad2)
    draw.line([(x1, y1), (x2, y2)], fill=figure_shadow, width=1)

# Draw the arms (they go from the shoulders to the middle of the wide beam)
arm_y = crucifix_size // 4  # Where the wide beam is
shoulder_y = head_y + head_radius + 5  # Where the shoulders are
arm_length = crucifix_size // 6  # How long the arms are
arm_thickness_fig = figure_width // 2  # How thick the arms are
arm_end_y = arm_y  # The arms end right in the middle of the wide beam
# Left arm with a little curve
left_arm_points = [
    (center_x - figure_width // 2, shoulder_y),  # Start at the left shoulder
    (center_x - arm_length // 2, (shoulder_y + arm_end_y) // 2),  # Middle point to make a curve
    (center_x - arm_length, arm_end_y)  # End at the middle of the wide beam
]
draw.line(left_arm_points, fill=figure_color, width=arm_thickness_fig)  # Draw the left arm
# Right arm with a little curve
right_arm_points = [
    (center_x + figure_width // 2, shoulder_y),  # Start at the right shoulder
    (center_x + arm_length // 2, (shoulder_y + arm_end_y) // 2),  # Middle point to make a curve
    (center_x + arm_length, arm_end_y)  # End at the middle of the wide beam
]
draw.line(right_arm_points, fill=figure_color, width=arm_thickness_fig)  # Draw the right arm
# Add hands (like little hands with fingers)
# Left hand
draw.polygon(
    [(center_x - arm_length - arm_thickness_fig // 2, arm_end_y - arm_thickness_fig // 2),
     (center_x - arm_length + arm_thickness_fig // 2, arm_end_y - arm_thickness_fig // 2),
     (center_x - arm_length + arm_thickness_fig // 4, arm_end_y + arm_thickness_fig // 2),
     (center_x - arm_length - arm_thickness_fig // 4, arm_end_y + arm_thickness_fig // 2)],
    fill=figure_color  # Draw the palm with a slight curve
)
draw.line(
    [(center_x - arm_length - arm_thickness_fig // 2, arm_end_y - arm_thickness_fig // 4),
     (center_x - arm_length - arm_thickness_fig, arm_end_y - arm_thickness_fig // 4)],
    fill=figure_color, width=1  # Draw a finger
)
draw.line(
    [(center_x - arm_length - arm_thickness_fig // 2, arm_end_y),
     (center_x - arm_length - arm_thickness_fig, arm_end_y)],
    fill=figure_color, width=1  # Draw another finger
)
# Right hand
draw.polygon(
    [(center_x + arm_length - arm_thickness_fig // 2, arm_end_y - arm_thickness_fig // 2),
     (center_x + arm_length + arm_thickness_fig // 2, arm_end_y - arm_thickness_fig // 2),
     (center_x + arm_length + arm_thickness_fig // 4, arm_end_y + arm_thickness_fig // 2),
     (center_x + arm_length - arm_thickness_fig // 4, arm_end_y + arm_thickness_fig // 2)],
    fill=figure_color  # Draw the palm with a slight curve
)
draw.line(
    [(center_x + arm_length + arm_thickness_fig // 2, arm_end_y - arm_thickness_fig // 4),
     (center_x + arm_length + arm_thickness_fig, arm_end_y - arm_thickness_fig // 4)],
    fill=figure_color, width=1  # Draw a finger
)
draw.line(
    [(center_x + arm_length + arm_thickness_fig // 2, arm_end_y),
     (center_x + arm_length + arm_thickness_fig, arm_end_y)],
    fill=figure_color, width=1  # Draw another finger
)

# Draw the body (the torso)
torso_y_start = head_y + head_radius  # Start below the head
torso_y_end = torso_y_start + figure_height // 3  # End a bit lower
draw.polygon(
    [(center_x - figure_width // 2, torso_y_start),  # Top left
     (center_x + figure_width // 2, torso_y_start),  # Top right
     (center_x + figure_width // 3, torso_y_end),  # Bottom right
     (center_x - figure_width // 3, torso_y_end)],  # Bottom left
    fill=figure_color  # Color the body with the darker color
)

# Draw a cloth around the waist (like a little skirt)
loincloth_y = torso_y_end  # Where the cloth starts
loincloth_width = figure_width * 1.5  # How wide the cloth is
draw.polygon(
    [(center_x - loincloth_width // 2, loincloth_y),  # Top left
     (center_x + loincloth_width // 2, loincloth_y),  # Top right
     (center_x + loincloth_width // 3, loincloth_y + figure_width // 2),  # Bottom right
     (center_x - loincloth_width // 3, loincloth_y + figure_width // 2)],  # Bottom left
    fill=figure_color  # Color the cloth with the darker color
)

# Draw the legs (they bend at the knees and the feet cross)
leg_y_knee = loincloth_y + figure_height // 4  # Where the knees are
leg_y_feet = loincloth_y + figure_height // 2  # Where the feet are
draw.line(
    [(center_x - figure_width // 3, loincloth_y + figure_width // 2),  # Start at the cloth
     (center_x - figure_width // 4, leg_y_knee)],  # End at the knee
    fill=figure_color, width=arm_thickness_fig  # Draw the left upper leg
)
draw.line(
    [(center_x + figure_width // 3, loincloth_y + figure_width // 2),  # Start at the cloth
     (center_x + figure_width // 4, leg_y_knee)],  # End at the knee
    fill=figure_color, width=arm_thickness_fig  # Draw the right upper leg
)
draw.line(
    [(center_x - figure_width // 4, leg_y_knee),  # Start at the knee
     (center_x + 2, leg_y_feet)],  # End at the feet
    fill=figure_color, width=arm_thickness_fig  # Draw the left lower leg
)
draw.line(
    [(center_x + figure_width // 4, leg_y_knee),  # Start at the knee
     (center_x - 2, leg_y_feet)],  # End at the feet
    fill=figure_color, width=arm_thickness_fig  # Draw the right lower leg
)
# Add feet (two little shapes that cross with toes)
draw.polygon(
    [(center_x - arm_thickness_fig // 2, leg_y_feet - arm_thickness_fig // 4),
     (center_x, leg_y_feet - arm_thickness_fig // 4),
     (center_x - arm_thickness_fig // 4, leg_y_feet + arm_thickness_fig // 4),
     (center_x - arm_thickness_fig // 2 - 2, leg_y_feet + arm_thickness_fig // 4)],
    fill=figure_color  # Draw the left foot with a slight curve
)
draw.polygon(
    [(center_x, leg_y_feet - arm_thickness_fig // 4),
     (center_x + arm_thickness_fig // 2, leg_y_feet - arm_thickness_fig // 4),
     (center_x + arm_thickness_fig // 2 + 2, leg_y_feet + arm_thickness_fig // 4),
     (center_x + arm_thickness_fig // 4, leg_y_feet + arm_thickness_fig // 4)],
    fill=figure_color  # Draw the right foot (overlapping) with a slight curve
)
# Add toes to the feet
draw.line(
    [(center_x - arm_thickness_fig // 2, leg_y_feet - arm_thickness_fig // 8),
     (center_x - arm_thickness_fig // 2 - 2, leg_y_feet - arm_thickness_fig // 8)],
    fill=figure_color, width=1  # Draw a toe on the left foot
)
draw.line(
    [(center_x + arm_thickness_fig // 2, leg_y_feet - arm_thickness_fig // 8),
     (center_x + arm_thickness_fig // 2 + 2, leg_y_feet - arm_thickness_fig // 8)],
    fill=figure_color, width=1  # Draw a toe on the right foot
)
draw.ellipse(
    [(center_x - 2, leg_y_feet - 2), (center_x + 2, leg_y_feet + 2)],
    fill=figure_shadow  # Add a little nail in the middle
)

# Add a sign that says "INRI" above the head
font_size = arm_thickness // 4  # How big the letters are
try:
    font = ImageFont.truetype("garamond.ttf", font_size)  # Use a fancy font called Garamond
except IOError:
    try:
        font = ImageFont.truetype("ebgaramond.ttf", font_size)  # If Garamond isn't there, try EB Garamond
    except IOError:
        font = ImageFont.load_default()  # If that doesn't work, use a simple font

text = "INRI"  # The word to write
text_bbox = draw.textbbox((0, 0), text, font=font)  # Find out how big the word is
text_width = text_bbox[2] - text_bbox[0]  # How wide the word is
text_height = text_bbox[3] - text_bbox[1]  # How tall the word is

plaque_margin = 4  # A little space around the word
plaque_y = crucifix_size // 6  # Where the sign goes
plaque_width = text_width + 2 * plaque_margin  # How wide the sign is
plaque_height = text_height + 2 * plaque_margin  # How tall the sign is
plaque_rect = [
    (center_x - plaque_width // 2, plaque_y - plaque_height // 2),  # Top left of the sign
    (center_x + plaque_width // 2, plaque_y + plaque_height // 2)  # Bottom right of the sign
]
draw.rectangle(plaque_rect, fill=(240, 235, 210, 255))  # Make the sign off-white
draw.rectangle(plaque_rect, outline=wood_color_shadow, width=1)  # Add a border to the sign

text_position = (
    center_x - text_width // 2,  # Put the word in the middle
    plaque_y - text_height // 2
)
draw.text(text_position, text, fill=(0, 0, 0, 255), font=font)  # Write "INRI" in black

# Put the cross on the QR code (like sticking a sticker on the puzzle)
pos = ((qr_width - crucifix_size) // 2, (qr_height - crucifix_size) // 2)  # Put it in the middle
qr_img.paste(crucifix_img, pos, crucifix_img)  # Stick the cross on the QR code

# Save the picture so we can look at it
output_path = "qr_code_with_realistic_crucifix.png"
qr_img.save(output_path)
print(f"Image saved as {output_path}")  # Tell us where the picture is