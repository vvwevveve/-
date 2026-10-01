KM_BASE = 100
FUEL_PRICE = 49.50

def calculate_trip(distance, consumption, price=FUEL_PRICE):
    """Рассчитывает расход топлива и стоимость поездки."""
    fuel = distance * (consumption / KM_BASE)
    cost = fuel * price
    return fuel, cost

dist = float(input("Какое расстояние (км)? "))
consumption = float(input("Сколько литров на 100 км ест машина? "))

fuel_needed, total_cost = calculate_trip(dist, consumption)
print(f"Нужно бензина: {fuel_needed:.2f} л")
print(f"Стоимость: {total_cost:.2f} руб.")