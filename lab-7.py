import math

text = input("Enter Text: ")
key = int(input("Enter Key Length: "))
pad = input("Padding Character: ")

while len(text) % key != 0:
    text += pad

rows = math.ceil(len(text) / key)

print("\nMatrix:")
for i in range(rows):
    print(text[i*key:(i+1)*key])

cipher = ""
for c in range(key):
    for r in range(rows):
        cipher += text[r*key+c]

print("Cipher Text:", cipher)
