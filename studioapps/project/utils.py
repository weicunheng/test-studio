import secrets


def gen_project_code():
    """
    return: str
    """
    return secrets.token_hex(10)
