USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    """Конвертирует сумму из долларов в рубли."""
    return amount_usd * USD_TO_RUB

dollars = float(input("Введите сумму в долларах: "))
rubles = convert_usd_to_rub(dollars)
print(f"Сумма в рублях: {rubles:.2f} руб.")