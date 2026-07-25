# Login Authentication

correct_username = "admin"
correct_password = "admin123"

username = input("Username : ")
password = input("Password : ")

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")
