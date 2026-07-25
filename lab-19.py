import cv2

END_MARKER = "1111111111111110"


def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_text(binary):
    result = ""

    for i in range(0, len(binary), 8):

        byte = binary[i:i + 8]

        if len(byte) == 8:
            result += chr(int(byte, 2))

    return result


def hide_message(input_video, output_video, message):

    cap = cv2.VideoCapture(input_video)

    width = int(
        cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    )

    height = int(
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    )

    fps = cap.get(
        cv2.CAP_PROP_FPS
    )

    fourcc = cv2.VideoWriter_fourcc(
        *"mp4v"
    )

    out = cv2.VideoWriter(
        output_video,
        fourcc,
        fps,
        (width, height)
    )

    ret, frame = cap.read()

    if not ret:

        print("Could not read video.")

        return

    binary = text_to_binary(
        message
    ) + END_MARKER

    capacity = (
        frame.shape[0]
        * frame.shape[1]
        * 3
    )

    if len(binary) > capacity:

        print("Message is too large.")

        cap.release()
        out.release()

        return

    index = 0

    for y in range(height):

        for x in range(width):

            for c in range(3):

                if index < len(binary):

                    frame[y, x, c] = (
                        frame[y, x, c] & 254
                    ) | int(binary[index])

                    index += 1

    out.write(frame)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        out.write(frame)

    cap.release()

    out.release()

    print(
        "Message hidden in first frame."
    )


def extract_message(video_file):

    cap = cv2.VideoCapture(
        video_file
    )

    ret, frame = cap.read()

    cap.release()

    if not ret:

        return "Video could not be read."

    binary = ""

    height, width, _ = frame.shape

    for y in range(height):

        for x in range(width):

            for c in range(3):

                binary += str(
                    frame[y, x, c] & 1
                )

                if binary.endswith(
                    END_MARKER
                ):

                    message_binary = binary[
                        :-len(END_MARKER)
                    ]

                    return binary_to_text(
                        message_binary
                    )

    return "No message found."


if __name__ == "__main__":

    message = input(
        "Enter secret message: "
    )

    hide_message(
        "input.mp4",
        "stego_video.mp4",
        message
    )

    print("\nExtracted message:")

    print(
        extract_message(
            "stego_video.mp4"
        )
    )
