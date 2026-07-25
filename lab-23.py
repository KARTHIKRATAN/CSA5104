from PIL import Image
import base64

END_MARKER = "1111111111111110"


def bytes_to_binary(data):

    return ''.join(
        format(byte, '08b')
        for byte in data
    )


def binary_to_bytes(binary):

    result = bytearray()

    for i in range(
        0,
        len(binary),
        8
    ):

        byte = binary[i:i + 8]

        if len(byte) == 8:

            result.append(
                int(byte, 2)
            )

    return bytes(result)


def hide_file(
    image_name,
    output_name,
    file_name
):

    with open(
        file_name,
        "rb"
    ) as file:

        file_data = file.read()

    encoded_data = base64.b64encode(
        file_data
    )

    payload = (
        file_name
        + "|"
        + encoded_data.decode()
    )

    binary = (
        bytes_to_binary(
            payload.encode()
        )
        + END_MARKER
    )

    image = Image.open(
        image_name
    ).convert("RGB")

    capacity = (
        image.width
        * image.height
        * 3
    )

    if len(binary) > capacity:

        print(
            "File is too large."
        )

        return

    pixels = list(
        image.getdata()
    )

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
        output_name
    )

    print(
        "File hidden successfully."
    )


def extract_file(
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

                binary = binary[
                    :-len(END_MARKER)
                ]

                data = binary_to_bytes(
                    binary
                )

                text = data.decode()

                file_name, encoded = (
                    text.split("|", 1)
                )

                original_data = (
                    base64.b64decode(
                        encoded
                    )
                )

                with open(
                    "recovered_" + file_name,
                    "wb"
                ) as file:

                    file.write(
                        original_data
                    )

                print(
                    "File recovered:",
                    "recovered_" + file_name
                )

                return

    print(
        "No hidden file found."
    )


if __name__ == "__main__":

    hide_file(
        "cover.png",
        "file_stego.png",
        "sample.txt"
    )

    extract_file(
        "file_stego.png"
    )
