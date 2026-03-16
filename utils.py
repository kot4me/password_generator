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

def simple_password(length=8):
    simple_charset = config.LOWERCASE + config.UPPERCASE + config.DIGITS
    password = ''.join(random.choice(simple_charset) for _ in range(length))
    return password

def complex_password(length=config.RECOMMENDED_COMPLEX_LENGTH):
    complex_charset = (config.LOWERCASE + config.UPPERCASE + 
                       config.DIGITS + config.SPECIAL)
    
    if config.REQUIRE_ALL_CHAR_TYPES:
        password = [
            random.choice(config.LOWERCASE),
            random.choice(config.UPPERCASE),
            random.choice(config.DIGITS),
            random.choice(config.SPECIAL)
        ]
        
        for _ in range(length - 4):
            password.append(random.choice(complex_charset))
        
        random.shuffle(password)
        return ''.join(password)
    else:
        return ''.join(random.choice(complex_charset) for _ in range(length))