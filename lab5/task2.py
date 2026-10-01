weight, height = map(float, input("Введите вес (кг) и рост (м): ").split())
bmi = weight / (height ** 2)
print(f"ИМТ: {bmi:.1f}")