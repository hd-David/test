import re

regex = r"^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[a-z\d@$!%*?&]{8,}$"

test_passwords = [
    "password@1",   # ✅ Valid
    "myp@ssword3",  # ✅ Valid
    "onlyletters",  # ❌ No digit
    "12345678",     # ❌ No letter
    "mypassword"    # ❌ No digit & special char
]

for password in test_passwords:
    if re.match(regex, password):
        print(f"✅ '{password}' is VALID")
    else:
        print(f"❌ '{password}' is INVALID")
