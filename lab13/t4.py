ip_text = input("введите ip-адрес: ")
parts = ip_text.split(".")

is_correct = True

for item in parts:
    num = int(item)
    if num < 0 or num > 255:
        is_correct = False
        break

if is_correct == True:
    print("ДА")
else:
    print("НЕТ")