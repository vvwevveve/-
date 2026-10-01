import random

secret = random.randint(1, 10)

for _ in range(3):
    guess = int(input("Введите число: "))
    if guess == secret:
        print("Угадали!")
        break
    elif guess < secret:
        print("Неверно, нужно больше")
    else:
        print("Неверно, нужно меньше")
else:
    print(f"Попытки закончились. Загаданное число: {secret}")