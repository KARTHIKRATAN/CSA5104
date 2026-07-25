# Bell-LaPadula Access Checker

levels = {
    "public": 1,
    "confidential": 2,
    "secret": 3,
    "top secret": 4
}

user = input("User Level : ").strip().lower()
file = input("File Level : ").strip().lower()
operation = input("Operation (Read/Write) : ").strip().lower()

if user not in levels or file not in levels:
    print("Invalid Security Level")

elif operation == "read":
    # No Read Up
    if levels[user] >= levels[file]:
        print("Access Allowed")
    else:
        print("Access Denied")
        print("Reason : No Read Up")

elif operation == "write":
    # No Write Down
    if levels[user] <= levels[file]:
        print("Access Allowed")
    else:
        print("Access Denied")
        print("Reason : No Write Down")

else:
    print("Invalid Operation")
