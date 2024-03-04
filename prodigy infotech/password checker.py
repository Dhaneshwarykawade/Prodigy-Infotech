import re

def password_strength(password):
    length = len(password)
    score = 0

    # Criteria for assessing password strength
    if length >= 8:
        score += 1
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1

    # Feedback based on the score
    if score == 0:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    elif score == 4:
        return "Very Strong"

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    print("Password Strength:", strength)

if __name__ == "__main__":
    main()
