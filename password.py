def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False

print(is_acceptable_password("short"))

