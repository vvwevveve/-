TAX_RATE = 0.13

income = float(input("Введите годовой доход: "))
tax = income * TAX_RATE
net_income = income - tax

print(f"Общая сумма дохода: {income:,.2f}".replace(",", " ") + " руб.")
print(f"Сумма рассчитанного налога: {tax:,.2f}".replace(",", " ") + " руб.")
print(f"Сумма «на руки» после вычета налога: {net_income:,.2f}".replace(",", " ") + " руб.")