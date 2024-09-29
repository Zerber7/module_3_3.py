# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a=11)
print_params(b=25)
print_params(c=[1, 2, 3])
print()
# 2.Распаковка параметров:
value_list = [1000, 'Urban', False]
print_params(*value_list)
print()
value_dict = {'a': 7, 'b': "Кирпич", 'c': [1, 2, 3]}
print_params(**value_dict)
print()
# 3.Распаковка + отдельные параметры:
value_list2 = [54.32, "'Cтрока'"]
print_params(*value_list2, 42)
