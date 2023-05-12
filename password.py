def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) >= 6
    cond2 = any(map(str.isdigit, password))
    if password == "1234567":
        return False
    return all([cond1, cond2])

print(is_acceptable_password("short"))

