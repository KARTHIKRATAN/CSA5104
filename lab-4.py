import math

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

K = [[3, 3], [2, 5]]

det = (K[0][0]*K[1][1] - K[0][1]*K[1][0]) % 26

if math.gcd(det, 26) != 1:
    print('Invalid key matrix')
    exit()

det_inv = mod_inverse(det, 26)

adj = [[K[1][1], -K[0][1]],
       [-K[1][0], K[0][0]]]

K_inv = [[(det_inv * adj[i][j]) % 26 for j in range(2)] for i in range(2)]

text = input('Enter plaintext (4 letters): ').upper().replace(' ', '')

nums = [ord(c) - 65 for c in text]

cipher_nums = []
for i in range(0, len(nums), 2):
    p1, p2 = nums[i], nums[i+1]
    c1 = (K[0][0]*p1 + K[0][1]*p2) % 26
    c2 = (K[1][0]*p1 + K[1][1]*p2) % 26
    cipher_nums.extend([c1, c2])

cipher = ''.join(chr(n + 65) for n in cipher_nums)
print('Ciphertext:', cipher)

plain_nums = []
for i in range(0, len(cipher_nums), 2):
    c1, c2 = cipher_nums[i], cipher_nums[i+1]
    p1 = (K_inv[0][0]*c1 + K_inv[0][1]*c2) % 26
    p2 = (K_inv[1][0]*c1 + K_inv[1][1]*c2) % 26
    plain_nums.extend([p1, p2])

plain = ''.join(chr(n + 65) for n in plain_nums)
print('Decrypted:', plain)
