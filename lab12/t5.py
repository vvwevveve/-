data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_three = data[:3]
last_three = data[-3:]
reverse_list = data[::-1]
odd_index = data[1::2]

print(f"первая тройка чисел: {first_three}")
print(f"последняя тройка чисел: {last_three}")
print(f"список в обратном порядке: {reverse_list}")
print(f"элементы с нечетными индексами: {odd_index}")