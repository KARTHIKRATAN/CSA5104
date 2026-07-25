# File Access Permission Simulation

role = input("Enter Role: ").strip().lower()

if role == "admin":
    print("Permissions:")
    print("Read, Write, Delete")

elif role == "faculty":
    print("Permissions:")
    print("Read, Write")

elif role == "student":
    print("Permissions:")
    print("Read Only")

else:
    print("Invalid Role")
