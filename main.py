import utils
import config

def main():
    print("Генератор паролей")

    # Получаем детальную информацию о сложности
    strength_info = utils.check_password_strength(password)
    score = strength_info['score']

    # Цветной вывод в зависимости от сложности
    if score <= 2:
        status = "⚠️ СЛАБЫЙ"
        color_code = "\033[91m"  # Красный
    elif score <= 4:
        status = "👍 СРЕДНИЙ"
        color_code = "\033[93m"  # Желтый
    else:
        status = "💪 СИЛЬНЫЙ"
        color_code = "\033[92m"  # Зеленый

    reset_color = "\033[0m"  # Сброс цвета

    print(f"\n📊 Оценка сложности: {color_code}{status}{reset_color} ({score}/5)")

    # Показываем детальный разбор
    print("\n📋 Детальный разбор пароля:")
    print(f"   • Длина: {strength_info['length']} символов")
    print(f"   • Строчные буквы: {'✅' if strength_info['has_lower'] else '❌'}")
    print(f"   • Заглавные буквы: {'✅' if strength_info['has_upper'] else '❌'}")
    print(f"   • Цифры: {'✅' if strength_info['has_digit'] else '❌'}")
    print(f"   • Спецсимволы: {'✅' if strength_info['has_special'] else '❌'}")

    # Рекомендации по улучшению
    if strength_info['missing']:
        print("\n💡 Рекомендации по улучшению:")
        for item in strength_info['missing']:
            print(f"   • Добавьте {item}")

if __name__ == "__main__":
    main()