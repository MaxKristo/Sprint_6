from datetime import datetime, timedelta
import random

class User:
    # тестовые данные пользователя 1
    user_1 = {
        'name': 'Сергей',
        'surname': 'Иванов',
        'address': 'улица Тверская, д. 14',
        'phone': f'8{random.randint(1000000000, 9999999999)}',
        'comment': f''
    }
    # тестовые данные пользователя 2
    user_2 = {
        'name': 'Виктор',
        'surname': 'Петров',
        'address': 'улица Тверская, д. 10',
        'phone': f'8{random.randint(1000000000, 9999999999)}',
        'comment': 'позвонить заранее'
    }

# проверка оформления заказа
order_confirm = "Заказ оформлен"

# дата заказа самоката форматируется как "текущее число + 2 дня"
order_date = datetime.now() + timedelta(days=2)
day_str = f"{order_date.day}"




