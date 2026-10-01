COFFEE = 120
TEA = 80
JUICE = 100
WATER = 50
LEMONADE = 90

item = input("Выберите напиток (1-5 или название): ").strip().lower()

match item:
    case "1" | "кофе":
        name, price = "Кофе ☕", COFFEE
    case "2" | "чай":
        name, price = "Чай 🍵", TEA
    case "3" | "сок":
        name, price = "Сок 🧃", JUICE
    case "4" | "вода":
        name, price = "Вода 💧", WATER
    case "5" | "лимонад":
        name, price = "Лимонад 🥤", LEMONADE
    case _:
        print("Ошибка: такого напитка нет в меню")
        exit()

count = int(input("Количество порций: "))
promo = input("Код скидки (если есть): ").strip().upper()

total = price * count
discount = int(total * 0.20) if promo == "STUDENT" else 0
final = total - discount

if count % 10 == 1 and count % 100 != 11:
    word = "порция"
elif 2 <= count % 10 <= 4 and not (12 <= count % 100 <= 14):
    word = "порции"
else:
    word = "порций"

print(f"\nТовар: {name}")
print(f"Цена за порцию: {price} руб")
print(f"Количество: {count} {word}")
print(f"Сумма: {total} руб")
if discount:
    print(f'Скидка "STUDENT" (20%): -{discount} руб')
print(f"💰 К ОПЛАТЕ: {final} руб")