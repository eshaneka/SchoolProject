def get_random_code(length=8):
    """Generates a random string of letters and digits"""
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join((random.choice(characters) for _ in range(length)))
