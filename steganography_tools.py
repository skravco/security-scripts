from PIL import Image

def hide_message(image_path, message):
    # Open the image using PIL (Python Imaging Library)
    image = Image.open(image_path)

    # Convert the message characters to binary and concatenate with a sentinel value
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Adding a sentinel value

    # Get the pixel data from the image
    pixels = list(image.getdata())

    # Create a list to store the new pixel data
    new_pixels = []
    data_index = 0

    # Iterate through each pixel in the image
    for pixel in pixels:
        new_pixel = []
        for value in pixel:
            if data_index < len(binary_message):
                # Embed the message data into the least significant bit of the pixel value
                new_value = int(format(value, '08b')[:-1] + binary_message[data_index], 2)
                data_index += 1
            else:
                # If all message data has been embedded, keep the pixel value unchanged
                new_value = value
            new_pixel.append(new_value)
        new_pixels.append(tuple(new_pixel))

    # Update the image with the new pixel data
    image.putdata(new_pixels)

    # Save the modified image with the hidden message
    image.save('hidden_message.png')

# Message to hide in the image
message = 'success!'

# Path to the input image
image_path = 'example.png'

# Call the hide_message function with the provided image and message
hide_message(image_path, message)
