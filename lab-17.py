from PIL import Image
import hashlib
import base64

END_MARKER = "1111111111111110"


def encrypt_message(message, password):
    key = hashlib.sha256(password.encode()).digest()

    encrypted = bytearray()

    for i, byte in enumerate(message.encode()):
        encrypted.append(byte ^ key[i % len(key)])

    return base64.b64encode(encrypted).decode()


def decrypt_message(encrypted_text, password):
    key = hashlib.sha256(password.encode()).digest()

    encrypted = base64.b64decode(encrypted_text)

    decrypted = bytearray()

    for i, byte in enumerate(encrypted):
        decrypted.append(byte ^ key[i % len(key)])

    return decrypted.decode()


def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_text(binary):
    result = ""

    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]

        if len(byte) == 8:
            result += chr(int(byte, 2))

    return result


def hide_message(image_name, output_name, message):

    image = Image.open(image_name).convert("RGB")

    binary = text_to_binary(message) + END_MARKER

    capacity = image.width * image.height * 3

    if len(binary) > capacity:
        print("Message too large.")
        return False

    pixels = list(image.getdata())
    new_pixels = []

    index = 0

    for pixel in pixels:

        new_pixel = list(pixel)

        for i in range(3):

            if index < len(binary):

                new_pixel[i] = (
                    new_pixel[i] & 254
                ) | int(binary[index])

                index += 1

        new_pixels.append(tuple(new_pixel))

    image.putdata(new_pixels)

    image.save(output_name)

    return True


def extract_message(image_name):

    image = Image.open(image_name).convert("RGB")

    binary = ""

    for pixel in image.getdata():

        for value in pixel:

            binary += str(value & 1)

    position = binary.find(END_MARKER)

    if position == -1:
        return None

    return binary_to_text(binary[:position])


if __name__ == "__main__":

    message = input("Enter secret message: ")

    password = input("Enter password: ")

    encrypted = encrypt_message(message, password)

    hide_message(
        "cover.png",
        "password_stego.png",
        encrypted
    )

    print("\nMessage hidden successfully.")

    extracted = extract_message("password_stego.png")

    try:

        recovered = decrypt_message(
            extracted,
            password
        )

        print("Recovered message:")
        print(recovered)

    except Exception:

        print("Wrong password or corrupted data.")
