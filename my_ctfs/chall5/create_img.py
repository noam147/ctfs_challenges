from PIL import Image
import numpy as np

# Example: Create a 3x3 RGB image
pixel_array = np.array([
    [[255, 255, 255], [0, 255, 0], [0, 0, 255]]*500,   # Red, Green, Blue
    [[255, 255, 0], [0, 255, 255], [255, 0, 255]]*500,  # Yellow, Cyan, Magenta
    [[255, 255, 255], [128, 128, 128], [0, 255, 0]]*500   # White, Gray, Black
]*500, dtype=np.uint8)

# Convert to image
image = Image.fromarray(pixel_array, 'RGB')

# Save or show
image.show()  # or image.save("output.png")
