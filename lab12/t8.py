numbers_list = [42, 15, 8, 91, 23]
print(f"список до замены: {numbers_list}")

min_num = min(numbers_list)
min_index = 0

for i in range(len(numbers_list)):
    if numbers_list[i] == min_num:
        min_index = i
        break

numbers_list[0], numbers_list[min_index] = numbers_list[min_index], numbers_list[0]

print(f"список после замены: {numbers_list}")