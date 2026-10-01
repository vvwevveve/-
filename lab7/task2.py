import random

status = input("Введите статус: ").strip().lower()

match status:
    case "pending":
        print("Статус: В ожидании ⏳")
        print("Описание: Заказ ожидает подтверждения")
        print(f"Примерное время: {random.randint(15, 45)} минут")
    case "processing":
        print("Статус: В обработке ⚙️")
        print("Описание: Заказ собирается")
        print(f"Примерное время: {random.randint(1, 4)} часа")
    case "shipped":
        print("Статус: Отправлено ✈️")
        print("Описание: Ваш заказ находится в пути к вам")
        print("Примерное время: 2-5 дней")
        print("Рекомендация: Следите за уведомлениями о доставке")
    case "delivered":
        print("Статус: Доставлено 🎉")
        print("Описание: Заказ успешно вручен")
        print("Примерное время: Завершено")
    case "cancelled":
        print("Статус: Отменено ❌")
        print("Описание: Заказ аннулирован")
        print("Примерное время: -")
    case _:
        print(f'Ошибка: Неизвестный статус "{status}"')
        print("Доступные статусы: pending, processing, shipped, delivered, cancelled")