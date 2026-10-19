n = int(input("введите количество строк: "))
chars_list = []

for i in range(n):
    text = input("введите строку: ")
    chars_list.extend(text)

print(f"список всех символов: {chars_list}")