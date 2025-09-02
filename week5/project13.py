import re

def slice_email(email):
    # Normalize input: remove whitespace and convert to lowercase
    email = ''.join(email.split()).lower()

    # Define regex for basic email validation
    pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'

    if re.match(pattern, email):
        username, domain = email.split('@', 1)
        return username, domain
    else:
        return None, None

# Get user input
email = input("Enter your email: ")
username, domain = slice_email(email)

# Output result
if username and domain:
    print(f"Username: {username}\nDomain: {domain}")
else:
    print("Invalid email format. Please enter a valid email address.")

