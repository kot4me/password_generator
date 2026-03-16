import random
import config

def generate_password(length=config.DEFAULT_PASSWORD_LENGTH, 
                     charset=config.DEFAULT_CHARSET):
    password = ''.join(random.choice(charset) for _ in range(length))
    return password


def check_password_strength(password):
    strength = 0
    missing_types = []

    # Проверяем разные типы символов
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in config.SPECIAL for char in password)

    # Подсчет баллов и сбор отсутствующих типов
    if has_lower:
        strength += 1
    else:
        missing_types.append("строчные буквы")

    if has_upper:
        strength += 1
    else:
        missing_types.append("заглавные буквы")

    if has_digit:
        strength += 1
    else:
        missing_types.append("цифры")

    if has_special:
        strength += 1
    else:
        missing_types.append("спецсимволы")

    # Бонус за длинный пароль
    if len(password) >= 12:
        strength += 1
    elif len(password) < 8:
        missing_types.append("увеличить длину (минимум 8 символов)")

    return {
        'score': strength,
        'has_lower': has_lower,
        'has_upper': has_upper,
        'has_digit': has_digit,
        'has_special': has_special,
        'length': len(password),
        'missing': missing_types
    }

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