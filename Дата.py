import logging
from datetime import datetime

# Налаштування виводу в консоль
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d'
)

# Отримуємо поточну дату
today = datetime.now().strftime('%Y-%m-%d')

# Виводимо в консоль
logging.info(f"Сьогодні: {today}")