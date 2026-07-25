def transpose(text, key):
    cols = len(key)
    rows = -(-len(text)//cols)

    while len(text) < rows*cols:
        text += "X"

    mat = [text[i*cols:(i+1)*cols] for i in range(rows)]
    order = sorted(range(cols), key=lambda x: key[x])

    out = ""
    for c in order:
        for r in mat:
            out += r[c]
    return out

text = input("Enter Text: ")
key1 = input("Key1: ")
key2 = input("Key2: ")

c1 = transpose(text, key1)
c2 = transpose(c1, key2)

print("After First:", c1)
print("After Second:", c2)
