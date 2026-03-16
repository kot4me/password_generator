import utils
import config

def main():
    print("Генератор паролей")
 
    password = utils.generate_password()
    strength = utils.check_password_strength(password)
    
    print(f"\n Сгенерированный пароль: {password}")
    print(f"Сила пароля (1-5): {strength}")
    
    if strength <= 2:
        print("Слабый пароль")
    elif strength <= 4:
        print("Средний пароль")
    else:
        print("Сильный пароль")
    

if __name__ == "__main__":
    main()