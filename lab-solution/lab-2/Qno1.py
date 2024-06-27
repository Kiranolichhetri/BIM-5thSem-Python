# 1. WAP to check validity of email using regular expression.

import re

def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

# Test the function
test_emails = [
    "valid.email@example.com",
    "invalid-email.com",
    "another.valid_email@example.co.in",
    "invalid@com",
    "yet.another.valid-email@example.org"
]

for email in test_emails:
    print(f"{email} is {'valid' if is_valid_email(email) else 'invalid'}")
