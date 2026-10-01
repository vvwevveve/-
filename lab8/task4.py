m = float(input())
p = float(input())
n = int(input())

for day in range(1, n + 1):
    print(f"{day} {m}")
    m += m * (p / 100)