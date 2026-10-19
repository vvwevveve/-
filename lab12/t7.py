numbers = [10, 20, 30, 40, 50]
search_num = int(input("введите число: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search_num:
        print(f"индекс числа: {i}")
        found = True
        break

if found == False:
    print(f"нет такого числа")