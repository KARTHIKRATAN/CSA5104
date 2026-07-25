from collections import Counter
import string

plain_alphabets = string.ascii_lowercase
cipher_alphabets = "qwertyuiopasdfghjklzxcvbnm"

encrypt_dict = dict(zip(plain_alphabets, cipher_alphabets))
decrypt_dict = dict(zip(cipher_alphabets, plain_alphabets))

plaintext = input("Enter Plaintext: ").lower()

ciphertext = ''.join(encrypt_dict.get(ch, ch) for ch in plaintext)
decrypted_text = ''.join(decrypt_dict.get(ch, ch) for ch in ciphertext)

print("\nCiphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)

plain_freq = Counter(plaintext)
cipher_freq = Counter(ciphertext)

print("\nFrequency Analysis")
print("Alphabet\tPlain\tCipher")

for ch in string.ascii_lowercase:
    print(f"{ch}\t\t{plain_freq[ch]}\t{cipher_freq[ch]}")
