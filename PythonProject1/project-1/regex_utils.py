import re

def validate_name(name):
    pattern = r"^[A-Za-z\s]+$"
    return bool(re.match(pattern, name))
