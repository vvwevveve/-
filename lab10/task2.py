num1 = int(input())

while True:
    num2 = int(input())
    if num2 > num1:
        break
    else:
        print("Ошибка")

while True:
    num3 = int(input())
    if num3 > num2:
        break
    else:
        print("Ошибка")

print("Последовательность принята")