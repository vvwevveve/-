# Prakticheskaya rabota №3 - Elkin Dmitry

x_val = 42
pi_num = 3.14159
msg = "Hello, Python!"
flag = True
arr = [1, 2, 3]
tpl = (4, 5, 6)
dct = {"name": "Alice", "age": 30}
st = {7, 8, 9}
empty_val = None

print('Тип переменной x_val:', type(x_val))
print('Тип переменной pi_num:', type(pi_num))
print('Тип переменной msg:', type(msg))
print('Тип переменной flag:', type(flag))
print('Тип переменной arr:', type(arr))
print('Тип переменной tpl:', type(tpl))
print('Тип переменной dct:', type(dct))
print('Тип переменной st:', type(st))
print('Тип переменной empty_val:', type(empty_val))


my_items = [1, 2, 3]
print('Стартовый список:', my_items)
my_items[0] = 100
print('Обновленный список:', my_items)
# Изменил нулевой элемент списка

my_tuple_val = (1, 2, 3)
print('Стартовый кортеж:', my_tuple_val)
# my_tuple_val[0] = 100
# Попытался поменять кортеж, но ничего не вышло

text_val = 'cat'
print('Изначальная строка:', text_val)
# text_val[0] = 'b'
# Строка неизменяема

try:
    num_a = input()
    num_b = input()
    num_b = int(num_b)
    num_a = int(num_a)
    print(num_a + num_b)
except:
    print('Ошибка: введены неверные данные.')


fruits_list = ['яблоко', 'банан', 'груша']
fruits_list.append('апельсин')
print('Список фруктиков:', fruits_list)
unique_fruits = set(fruits_list)
print('Множество фруктиков:', unique_fruits)


user_name = input('Ваше имя: ')
user_age_str = input('Ваш возраст: ')
hobbies_str = input('Хобби через запятую: ')
user_age = int(user_age_str)
hobbies_list = [item.strip() for item in hobbies_str.split(",")]
profile = {
    'name': user_name,
    'age': user_age,
    'hobbies': hobbies_list
}
print('=' * 30)
print('ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ')
print('=' * 30)
print('Имя:', profile['name'])
print('Возраст:', profile['age'])
print('Хобби:', profile['hobbies'])
print('=' * 30)
