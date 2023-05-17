def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    cond2 = any(char.isdigit() for char in password)
    cond3 = any(char.isalpha() for char in password)
    if len(password) > 9:  # cond4
        cond2 = cond3 = True

    cond4 = 'password' not in password.lower()
    cond5 = 'PASSWORD' not in password.upper()

    return all([cond1, cond2, cond3, cond4])


print("Example:")
print(is_acceptable_password("short"))

