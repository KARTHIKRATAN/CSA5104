text = input("Enter Text: ")
key = input("Keyword: ")

cols = len(key)
rows = -(-len(text)//cols)

while len(text) < rows*cols:
    text += "X"

matrix = [text[i*cols:(i+1)*cols] for i in range(rows)]

order = sorted(range(len(key)), key=lambda k: key[k])

cipher = ""
for i in order:
    for row in matrix:
        cipher += row[i]

print("Cipher Text:", cipher)
