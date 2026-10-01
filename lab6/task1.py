temp = float(input("Температура (°C): "))
pressure = int(input("Верхнее давление: "))
pulse = int(input("Пульс: "))

if temp < 35 or temp > 38 or pressure < 105 or pressure > 140 or pulse < 55 or pulse > 110:
    print("Требуется врач")
elif 36 <= temp <= 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100:
    print("Нормальное состояние")
else:
    print("Легкое недомогание")