def encrypt(text, rails):
    fence = [''] * rails
    rail, down = 0, True

    for ch in text:
        fence[rail] += ch
        if rail == 0:
            down = True
        elif rail == rails - 1:
            down = False
        rail += 1 if down else -1

    return ''.join(fence)

text = input("Enter Text: ")
rails = int(input("Enter Rails: "))

cipher = encrypt(text, rails)

print("Cipher Text:", cipher)
print("Time Complexity: O(n)")
