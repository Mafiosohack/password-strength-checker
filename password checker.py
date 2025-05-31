import re

common_words = ['password', '123456', 'qwerty', 'letmein', 'welcome', 'abc123']

def password_strength(password):
    if len(password) < 8:
        return "Weak: Password must have atleast 8 characters long."
    if not re.search(r'[A-z]',password) :
        return "Weak: Password must contain atleast one uppercase letter."
    if not re.search(r'[a-z]',password):
        return  "Weak: Password must contain atleast one lowercase letter. "
    if not re.search(r'[0-9]',password):
        return "Weak: Password must contain atleast one digit."
    if not re.search(r'[!@#$%^&*]',password):
        return "Weak: Password must contain atleast one special character"

    for words in common_words:
        if words in password.lower():
            return " Weak: Password contains a common dictionary word"
    if ' ' in password:
        return " Weak: Password must not contain spaces."

    return " Strong: Password is strong."

while True:
    password = input("Enter a password: ")
    strength = password_strength(password)
    print(strength)

    again = input("Check another password? (y/n): ").strip().lower()
    if again != 'y':
        print("Exiting Password Checker. Goodbye!")
        break
