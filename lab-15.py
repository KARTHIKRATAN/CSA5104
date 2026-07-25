# Security Risk Level Calculator

likelihood = int(input("Likelihood (1-5) : "))
impact = int(input("Impact (1-5) : "))

if 1 <= likelihood <= 5 and 1 <= impact <= 5:

    risk = likelihood * impact

    print("Risk Score :", risk)

    if risk <= 6:
        print("Risk Level : Low")
    elif risk <= 14:
        print("Risk Level : Medium")
    else:
        print("Risk Level : High")

else:
    print("Please enter values between 1 and 5.")
