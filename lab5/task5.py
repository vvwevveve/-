BANKNOTES = (5000, 2000, 1000, 500, 200, 100)

amount = int(input("Введите сумму (кратно 100): "))

for bill in BANKNOTES:
    count = amount // bill
    amount %= bill
    print(f"Купюры {bill} руб.: {count} шт.")