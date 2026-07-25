from PIL import Image
import numpy as np
import time


def lsb_hide(image, message):

    image = image.copy()

    pixels = list(
        image.getdata()
    )

    binary = ''.join(
        format(ord(c), '08b')
        for c in message
    )

    binary += "1111111111111110"

    index = 0

    new_pixels = []

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

    return image


def calculate_mse(
    original,
    modified
):

    a = np.array(
        original
    ).astype(float)

    b = np.array(
        modified
    ).astype(float)

    return np.mean(
        (a - b) ** 2
    )


image = Image.open(
    "cover.png"
).convert("RGB")

message = (
    "This is a steganography test message."
)

start = time.time()

lsb_image = lsb_hide(
    image,
    message
)

lsb_time = time.time() - start

lsb_image.save(
    "lsb_result.png"
)

mse = calculate_mse(
    image,
    lsb_image
)

print(
    "LSB Technique"
)

print(
    "Execution Time:",
    lsb_time,
    "seconds"
)

print(
    "MSE:",
    mse
)

print(
    "\nComparison completed."
)
