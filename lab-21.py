from PIL import Image
import numpy as np
import math


def calculate_mse(
    original,
    stego
):

    original = np.array(
        original
    ).astype(float)

    stego = np.array(
        stego
    ).astype(float)

    mse = np.mean(
        (original - stego) ** 2
    )

    return mse


def calculate_psnr(mse):

    if mse == 0:

        return float("inf")

    max_pixel = 255.0

    return 10 * math.log10(
        (max_pixel ** 2) / mse
    )


original = Image.open(
    "cover.png"
).convert("RGB")

stego = Image.open(
    "stego.png"
).convert("RGB"
)

mse = calculate_mse(
    original,
    stego
)

psnr = calculate_psnr(
    mse
)

print(
    "Mean Squared Error (MSE):",
    mse
)

print(
    "Peak Signal-to-Noise Ratio (PSNR):",
    psnr,
    "dB"
)

if psnr > 40:

    print(
        "Image quality is very good."
    )

elif psnr > 30:

    print(
        "Image quality is acceptable."
    )

else:

    print(
        "Image quality may be significantly affected."
    )
