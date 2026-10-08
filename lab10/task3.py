maximum = 0

while True:
    num = int(input())
    if num == 0:
        break
    if num > maximum:
        maximum = num

print(maximum)