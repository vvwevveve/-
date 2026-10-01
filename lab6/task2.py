pocket = int(input("Номер кармана: "))

if not 0 <= pocket <= 36:
    print("ошибка ввода")
elif pocket == 0:
    print("зеленый")
elif (1 <= pocket <= 10) or (19 <= pocket <= 28):
    print("красный" if pocket % 2 != 0 else "черный")
else:
    print("черный" if pocket % 2 != 0 else "красный")