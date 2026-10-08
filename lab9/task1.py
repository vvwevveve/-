n = int(input())
i = 1

while i <= n:
    if 5 <= i <= 9:
        i += 1
        continue
    if 17 <= i <= 37:
        i += 1
        continue
    if 78 <= i <= 87:
        i += 1
        continue
    print(i)
    i += 1
