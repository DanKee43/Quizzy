import requests


def check_connection() -> bool:
    try:
        requests.head("http://www.google.com/", timeout=1)
        return True
    except requests.ConnectionError:
        return False


def register(username: str):
    taken_names = ["ana", "mike", "alex"]  # EXAMPLE
    if check_connection():
        if username in taken_names:
            return "USERNAME_TAKEN"
        else:
            return "OK"
