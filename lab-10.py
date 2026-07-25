cipher = input("Enter Ciphertext: ")

print("\nPossible Plaintexts")

for key in range(2, 9):
    print("Key Length", key, ":", cipher[::-1])
