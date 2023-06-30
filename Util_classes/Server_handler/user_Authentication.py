

def check_token(username: str, user_ID: int, user_token) -> bool:
    users_data = {"ana": (123, "A"),
                  "mike": (1337, "M"),
                  "abobus228": (228, "AB"),
                  "john": (456, "J"),
                  "ivan": (208, "I")}
    if username in users_data:
        return users_data[username] == (user_ID, user_token)
    return False


def gen_token():
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(10))