import random
import config

def generate_password(length=config.DEFAULT_PASSWORD_LENGTH, 
                     charset=config.DEFAULT_CHARSET):
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def check_password_strength(password):
    strength = 0
    
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in config.SPECIAL for char in password):
        strength += 1
    
    if len(password) >= 12:
        strength += 1
    
    return strength