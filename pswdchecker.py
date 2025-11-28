pswd = input("Enter your password:")

strength = 0

# Check length
if len(pswd) >= 8:
    strength += 1
else:
    print("Password atleast have 8 characters")

# Check for lowercase letters
if any(ch.islower() for ch in pswd):
    strength += 1
else:
    print("Add minimum one lowercase letter.")

# Check for uppercase letters
if any(ch.isupper() for ch in pswd):
    strength += 1
else:
    print("Add minimum one uppercase letter.")

# Check for digits
if any(ch.isdigit() for ch in pswd):
    strength += 1
else:
    print("Add at least one number.")

# Check for special characters
special = "~!@#$%^&*()_-+={}[]|\\;'<>,.?/"

if any(ch in special for ch in pswd):
    strength += 1
else:
    print("Add one special character.")

# Final strength result
if strength <= 2:
    print("Password Strength is WEAK")
elif strength == 3 or strength == 4:
    print("Password Strength is MEDIUM")
else:
    print("Password Strength is STRONG")
