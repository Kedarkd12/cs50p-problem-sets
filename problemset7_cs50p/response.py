import validators

email=input("Whats Your Email Address?:").strip()

if validators.email(email) is True:
    print("Valid")
else:
    print("Invalid")