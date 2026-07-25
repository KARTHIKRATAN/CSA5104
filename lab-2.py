import random
import string
from collections import Counter

alphabet = string.ascii_uppercase
shuffled = list(alphabet)
random.shuffle(shuffled)
key = ''.join(shuffled)

enc_map = dict(zip(alphabet, key))

text = input('Enter plaintext: ').upper()

cipher = ''
for ch in text:
    cipher += enc_map.get(ch, ch)

print('Random Key:', key)
print('Ciphertext:', cipher)

freq = Counter(ch for ch in cipher if ch.isalpha())

print('\nLetter Frequencies:')
for ch, count in freq.items():
    print(ch, ':', count)

print('\nTop 3 Frequent Letters:')
for ch, count in freq.most_common(3):
    print(ch, ':', count)
