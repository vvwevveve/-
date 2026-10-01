all_even = True

for _ in range(10):
    if int(input()) % 2 != 0:
        all_even = False

print("YES" if all_even else "NO")