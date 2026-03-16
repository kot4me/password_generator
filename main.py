# main.py - Главный файл генератора паролей
import utils
import config

def main():
    print("=" * 50)
    print("           ГЕНЕРАТОР ПАРОЛЕЙ")
    print("=" * 50)
    
    while True:
        print("\n" + "-" * 30)
        print("1 - Простой пароль (буквы + цифры)")
        print("2 - Сложный пароль (со спецсимволами)")
        print("3 - Выход")
        print("-" * 30)
        
        choice = input("\nВаш выбор (1-3): ")
        
        if choice == "1":
            # Сначала генерируем пароль
            password = utils.simple_password()
            print(f"\n✅ Простой пароль: {password}")
            
            # ПОСЛЕ генерации проверяем сложность
            strength_info = utils.check_password_strength(password)
            score = strength_info['score']
            
            print(f"📊 Оценка сложности: {score}/5")
            
        elif choice == "2":
            # Генерируем сложный пароль
            password = utils.complex_password()
            print(f"\n✅ Сложный пароль: {password}")
            
            # Проверяем сложность
            strength_info = utils.check_password_strength(password)
            score = strength_info['score']
            
            print(f"📊 Оценка сложности: {score}/5")
            
        elif choice == "3":
            print("\nДо свидания!")
            break
        else:
            print("\n❌ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()