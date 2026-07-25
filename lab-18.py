import wave
import numpy as np

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


def hide_message(input_audio, output_audio, message):

    audio = wave.open(input_audio, "rb")

    params = audio.getparams()

    frames = audio.readframes(audio.getnframes())

    audio.close()

    samples = np.frombuffer(
        frames,
        dtype=np.int16
    ).copy()

    binary = text_to_binary(message) + END_MARKER

    if len(binary) > len(samples):

        print("Message is too large.")

        return

    for i, bit in enumerate(binary):

        samples[i] = (
            samples[i] & ~1
        ) | int(bit)

    output = wave.open(
        output_audio,
        "wb"
    )

    output.setparams(params)

    output.writeframes(
        samples.tobytes()
    )

    output.close()

    print("Message hidden successfully.")


def extract_message(audio_file):

    audio = wave.open(
        audio_file,
        "rb"
    )

    frames = audio.readframes(
        audio.getnframes()
    )

    audio.close()

    samples = np.frombuffer(
        frames,
        dtype=np.int16
    )

    binary = ""

    for sample in samples:

        binary += str(sample & 1)

        if binary.endswith(END_MARKER):

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
        "audio.wav",
        "stego_audio.wav",
        message
    )

    print("\nExtracted message:")

    print(
        extract_message(
            "stego_audio.wav"
        )
    )
