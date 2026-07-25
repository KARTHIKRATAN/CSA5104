from PIL import Image

END_MARKER = "1111111111111110"


def text_to_binary(text):

    return ''.join(
        format(ord(c), '08b')
        for c in text
    )


def binary_to_text(binary):

    result = ""

    for i in range(
        0,
        len(binary),
        8
    ):

        byte = binary[i:i + 8]

        if len(byte) == 8:

            result += chr(
                int(byte, 2)
            )

    return result


def hide_part(
    input_image,
    output_image,
    message
):

    image = Image.open(
        input_image
    ).convert("RGB")

    binary = text_to_binary(
        message
    ) + END_MARKER

    pixels = list(
        image.getdata()
    )

    capacity = len(pixels) * 3

    if len(binary) > capacity:

        print(
            input_image,
            "is too small."
        )

        return False

    new_pixels = []

    index = 0

    for pixel in pixels:

        new_pixel = list(pixel)

        for i in range(3):

            if index < len(binary):

                new_pixel[i] = (
                    new_pixel[i] & 254
                ) | int(
                    binary[index]
                )

                index += 1

        new_pixels.append(
            tuple(new_pixel)
        )

    image.putdata(
        new_pixels
    )

    image.save(
        output_image
    )

    return True


def extract_part(
    image_name
):

    image = Image.open(
        image_name
    ).convert("RGB")

    binary = ""

    for pixel in image.getdata():

        for value in pixel:

            binary += str(
                value & 1
            )

            if binary.endswith(
                END_MARKER
            ):

                return binary_to_text(
                    binary[
                        :-len(END_MARKER)
                    ]
                )

    return ""


message = input(
    "Enter long secret message: "
)

parts = [
    message[:len(message)//3],
    message[len(message)//3:
           2*len(message)//3],
    message[2*len(message)//3:]
]

images = [
    "cover1.png",
    "cover2.png",
    "cover3.png"
]

stego_images = [
    "stego1.png",
    "stego2.png",
    "stego3.png"
]

for i in range(3):

    hide_part(
        images[i],
        stego_images[i],
        parts[i]
    )

print(
    "Message divided and hidden."
)

recovered = ""

for image in stego_images:

    recovered += extract_part(
        image
    )

print(
    "\nReconstructed message:"
)

print(recovered)
