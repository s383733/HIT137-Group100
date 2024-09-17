# Code by Mafuja Akhtar for HIT137 groups assignment2 
# Question2 > Chapter 1: The Gatekeeper

import time
from PIL import Image

# Generate the number 'n' based on the current time (as instructed)
def generate_number():
    current_time = int(time.time())
    n = (current_time % 100) + 50
    if n % 2 == 0:
        n += 10  #
    return n

# Function to modify the image and sum the red channel values
def modify_image(image_path, output_image_path, n):
    # Open the image
    image = Image.open(image_path)
    image = image.convert('RGB')  # Ensure it's in RGB mode
    width, height = image.size
    
    # Create a new blank image for the modified RGB values
    new_image = Image.new('RGB', (width, height))
    
    # Initialize variable to store the sum of red channel values
    red_channel_sum = 0

    # Loop through each pixel and modify the RGB values
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            
            # Add n to each RGB value, ensuring it's within 0-255
            new_r = min(255, max(0, r + n))
            new_g = min(255, max(0, g + n))
            new_b = min(255, max(0, b + n))
            
            # Set the new pixel in the new image
            new_image.putpixel((x, y), (new_r, new_g, new_b))
            
            # Add to the red channel sum
            red_channel_sum += new_r

    # Save the new image
    new_image.save(output_image_path)

    return new_image, red_channel_sum

# Step 1: Generate the number
n = generate_number()

# Print the generated number
print(f"Generated number (n): {n}")

# Step 2: Path to the input image ('chapter1.jpg') and output image ('chapter1out.jpg')
image_path = 'chapter1.jpg'  # Original image
output_image_path = 'chapter1out.jpg'  # New modified image

# Step 3: Modify the image and get the red channel sum
new_image, red_sum = modify_image(image_path, output_image_path, n)

# Step 4: Display the sum of red channel values
print(f"Sum of all red channel values: {red_sum}")

# Step 5: Display the original and modified images
original_image = Image.open(image_path)
original_image.show()  # This will display the original image
new_image.show()  # This will display the modified image
