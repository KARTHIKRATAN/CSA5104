from collections import Counter

def vigenere_encrypt(text, key):
    result = ''
    key = key.upper()
    j = 0
    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
            j += 1
        else:
            result += ch
    return result

def vigenere_decrypt(text, key):
    result = ''
    key = key.upper()
    j = 0
    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            result += chr((ord(ch) - 65 - shift) % 26 + 65)
            j += 1
        else:
            result += ch
    return result

plaintext = input('Enter plaintext: ')
keyword = input('Enter keyword: ')

cipher = vigenere_encrypt(plaintext, keyword)
print('Ciphertext:', cipher)

plain = vigenere_decrypt(cipher, keyword)
print('Decrypted:', plain)

print('\nRepeated sequences:')
for size in range(3, 6):
    seen = {}
    for i in range(len(cipher) - size + 1):
        seq = cipher[i:i+size]
        if seq in seen:
            print(seq, 'at positions', seen[seq], 'and', i)
        else:
            seen[seq] = i

print('Probable key length:', len(keyword))
