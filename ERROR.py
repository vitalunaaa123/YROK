import logging

logging.basicConfig(
    level=logging.ERROR,
    format='ПОМИЛКА: %(message)s'
)

def divide(a, b):
    try:
        result = a / b
        print(f"Результат: {result}")
        return result
    except Exception as e:
        logging.error(f"Сталася помилка: {e}")
        print("Щось пішло не так!")

print("Спробуємо поділити 10 на 2:")
divide(10, 2)

print("\nСпробуємо поділити 10 на 0:")
divide(10, 0)

print("\nСпробуємо поділити '10' на 2:")
divide("10", 2)
