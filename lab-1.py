def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += ch

    return result


def decrypt(text, key):
    return encrypt(text, -key)


def brute_force(cipher):
    print("\nAll Possible Decryptions:\n")

    for key in range(1, 26):
        print("Key", key, ":", decrypt(cipher, key))


# ---------------- Main Program ----------------

plaintext = input("Enter Plaintext : ")
key = int(input("Enter Key (1-25) : "))

ciphertext = encrypt(plaintext, key)

print("\nEncrypted Text :", ciphertext)

decrypted = decrypt(ciphertext, key)

print("Decrypted Text :", decrypted)

brute_force(ciphertext)
