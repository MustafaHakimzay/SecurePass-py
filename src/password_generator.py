import secrets
import string

def generate_password(length:int =16) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digit = string.digits
    special = string.punctuation
    all_chars = lowercase + uppercase + digit + special

    password = [
        secrets.choice(lowercase), 
        secrets.choice(uppercase), 
        secrets.choice(digit), 
        secrets.choice(special)]
    
    for _ in range(length - 4):
        password += secrets.choice(all_chars)

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)