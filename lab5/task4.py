import math

def calculate_rectangle_area(width, height):
    """Вычисляет площадь прямоугольника."""
    return width * height

def calculate_circle_area(radius):
    """Вычисляет площадь круга."""
    return math.pi * (radius ** 2)

w, h = map(float, input("Введите ширину и высоту прямоугольника: ").split())
print(f"Площадь прямоугольника: {calculate_rectangle_area(w, h):.2f}")

r = float(input("Введите радиус круга: "))
print(f"Площадь круга: {calculate_circle_area(r):.2f}")