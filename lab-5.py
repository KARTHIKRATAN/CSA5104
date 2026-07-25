import time

text = input("Enter Plaintext: ").upper()

# Caesar Cipher
t = time.time()
caesar = "".join(chr((ord(i)-65+3)%26+65) if i.isalpha() else i for i in text)
t1 = time.time()-t

# Monoalphabetic Cipher
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
mono = ""
t = time.time()
for i in text:
    mono += key[alpha.index(i)] if i.isalpha() else i
t2 = time.time()-t

# Vigenere Cipher
keyword = "KEY"
vig = ""
t = time.time()
j = 0
for i in text:
    if i.isalpha():
        vig += chr((ord(i)-65+ord(keyword[j%len(keyword)])-65)%26+65)
        j += 1
    else:
        vig += i
t3 = time.time()-t

# Hill Cipher (Fixed Key)
hill = "Simple Demo"

print("\nCipher\t\tCiphertext\t\tTime")
print("-----------------------------------------------")
print("Caesar\t\t", caesar, "\t", round(t1,6))
print("Mono\t\t", mono, "\t", round(t2,6))
print("Vigenere\t", vig, "\t", round(t3,6))
print("Hill\t\t", hill)
