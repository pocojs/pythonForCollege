import re

def is_strong_password(pswrd: str) -> bool:
  if len(pswrd) < 8:
    return False

  if not re.search("[A-Z]", pswrd):
    return False

  if not re.search("[a-z]", pswrd):
    return False

  if not re.search("[0-9]", pswrd):
    return False

  if not re.search("[@#$%&]", pswrd):
    return False

  return True


pswrd1 = "P@ssw0rd123"
pswrd2 = "Password"
pswrd3 = "12345678"

print(f"Пароль {pswrd1} - {"сильный" if is_strong_password(pswrd1) else "слабый"}")
print(f"Пароль {pswrd2} - {"сильный" if is_strong_password(pswrd2) else "слабый"}")
print(f"Пароль {pswrd3} - {"сильный" if is_strong_password(pswrd3) else "слабый"}")

