from PIL import Image
import numpy as np


def analyze_image(image_name):

    image = Image.open(
        image_name
    ).convert("RGB")

    pixels = np.array(
        image
    )

    lsb_values = pixels & 1

    zeros = np.sum(
        lsb_values == 0
    )

    ones = np.sum(
        lsb_values == 1
    )

    total = zeros + ones

    zero_ratio = (
        zeros / total
    )

    one_ratio = (
        ones / total
    )

    print(
        "\nImage:",
        image_name
    )

    print(
        "Total LSB values:",
        total
    )

    print(
        "LSB 0 ratio:",
        zero_ratio
    )

    print(
        "LSB 1 ratio:",
        one_ratio
    )


analyze_image(
    "cover.png"
)

analyze_image(
    "stego.png"
)
