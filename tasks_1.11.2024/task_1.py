import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.(com|org|ru)$"
    return bool(re.match(pattern, email))

print(is_valid_email("example.email@gmail.com"))
print(is_valid_email("wrong_email@domain"))
print(is_valid_email("user_name@domain.org"))