from PIL import Image

def getpix():
    # Open an image file
    image = Image.open('greyscale_image.jpg')
    # Load the image's pixel data
    pixels = image.load()
    # Print the pixel values
    for y in range(image.height):
        for x in range(image.width):
            print(f"Pixel at ({x},{y}): {pixels[x, y]}")
def changepix():
    # Open an image file
    msg_to_insert = "note to myself: username is: HA!CK#R_GAZA"
    base_image = Image.open('greyscale_image.jpg')
    # Load the image's pixel data
    pixels = base_image.load()
    for i in range(len(msg_to_insert)):
        pixels[i,0] = ord(msg_to_insert[i])
    for i in range(len(msg_to_insert),200):
        pixels[i,0] = 255
    for i in range(200):
        pixels[i,1] = 255
        pixels[i, 2] = 255
    base_image.save("final_logo.png")
    base_image.show()
    # Print the pixel values
    for y in range(base_image.height):
        for x in range(base_image.width):
            print(f"Pixel at ({x},{y}): {pixels[x, y]}")

changepix()