n = int(input())

first_max = -float("inf")
second_max = -float("inf")

for _ in range(n):
    num = int(input())
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max:
        second_max = num

print(int(first_max))
print(int(second_max))