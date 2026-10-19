text = input("введите числа через пробел: ")
numbers = text.split()

pairs_count = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            pairs_count = pairs_count + 1

print(f"количество совпадающих пар: {pairs_count}")