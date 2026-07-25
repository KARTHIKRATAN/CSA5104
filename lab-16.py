from PIL import Image

END_MARKER = "1111111111111110"


def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)


def binary_to_text(binary):
    chars = []

    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]

        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))

    return ''.join(chars)


def hide_message(input_image, output_image, message):
    image = Image.open(input_image).convert("RGB")

    binary_message = text_to_binary(message) + END_MARKER

    capacity = image.width * image.height * 3

    if len(binary_message) > capacity:
        print("Error: Message is too large for this image.")
        return False

    pixels = list(image.getdata())
    new_pixels = []

    data_index = 0

    for pixel in pixels:
        new_pixel = list(pixel)

        for channel in range(3):
            if data_index < len(binary_message):
                new_pixel[channel] = (
                    new_pixel[channel] & 254
                ) | int(binary_message[data_index])

                data_index += 1

        new_pixels.append(tuple(new_pixel))

    image.putdata(new_pixels)
    image.save(output_image)

    return True


def extract_message(stego_image):
    image = Image.open(stego_image).convert("RGB")

    binary_data = ""

    for pixel in image.getdata():
        for channel in pixel:
            binary_data += str(channel & 1)

    marker_position = binary_data.find(END_MARKER)

    if marker_position == -1:
        return "No hidden message found."

    message_binary = binary_data[:marker_position]

    return binary_to_text(message_binary)


if __name__ == "__main__":

    message = input("Enter secret message: ")

    if hide_message("cover.png", "stego.png", message):
        print("Message successfully hidden.")
        print("Stego image created: stego.png")

        recovered_message = extract_message("stego.png")

        print("\nExtracted message:")
        print(recovered_message)
