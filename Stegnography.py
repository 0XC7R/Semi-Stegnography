# // bit examples
blue = 0
green = 1
red = 2

msg = "Lorem Ipsum!"

def encode(msg, bit):
    # Convert the message to binary string
    binary_msg = ''.join(format(ord(char), '08b') for char in msg)

    # Initialize an empty list to hold the encoded values
    encoded_msg = []
    
    # Prepare the binary message to fit the length of the message
    for b in binary_msg:
        # Create a pixel, let's say starting with (0, 0, 0)
        pixel = [0, 0, 0]
        # Set the appropriate bit based on our input 'bit'
        pixel[bit] = int(b)  # Set the specified bit to the message bit
        encoded_msg.append(tuple(pixel))  # Append the pixel as a tuple

    return encoded_msg

def decode(encoded_pixels):
    # Initialize an empty string for the decoded message
    binary_string = ''

    # Go through each encoded pixel
    for pixel in encoded_pixels:
        # Get the bit from the specified color channel
        binary_string += str(pixel[blue])  # Assuming we were using the blue channel

    # Convert the binary string to text
    decoded_msg = ''
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if byte:  # Make sure there's data to convert
            decoded_msg += chr(int(byte, 2))  # Convert each byte to character

    return decoded_msg

# Example of using encode and decode
encoded_pixels = encode(msg, blue)  # Encode the message using blue bit
decoded_message = decode(encoded_pixels)  # Decode the message
print("Encoded Pixels (for visualization):", encoded_pixels)
print("Decoded Message:", decoded_message)