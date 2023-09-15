numbers = input("Введіть числа через кому: ").split(',')
num_list = [int(num.strip()) for num in numbers]
num_tuple = tuple(num_list)
print("Список:", num_list)
print("Кортеж:", num_tuple)
print("Сума:", sum(num_list))
print("Середнє арифметичне:", sum(num_list) / len(num_list))