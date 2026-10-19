marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

count_5 = 0
count_2 = 0

for item in marks:
    if item == 5:
        count_5 = count_5 + 1
    if item == 2:
        count_2 = count_2 + 1

print(f"количество пятерок: {count_5}")
print(f"количество двоек: {count_2}")