def check_age():
    age = int(input("Введіть свій вік: "))
    if age < 18:
        return "Ви ще неповнолітній"
    else:
        return "Ви повнолітній"

def draw_pyramid():
    pyramid_height = int(input("Введіть висоту піраміди: "))
    for i in range(pyramid_height):
        print(' ' * (pyramid_height - i - 1) + '*' * (2 * i + 1))

def reverse_sentence():
    sentence = input("Введіть речення: ")
    return sentence[::-1]

def most_frequent_letter():
    word = input("Введіть слово: ")
    max_letter = max(word, key=word.count)
    return max_letter, word.count(max_letter)

def list_and_tuple():
    numbers = input("Введіть числа через кому: ").split(',')
    num_list = [int(num.strip()) for num in numbers]
    num_tuple = tuple(num_list)
    return num_list, num_tuple, sum(num_list), sum(num_list) / len(num_list)

def generate_squares():
    n = int(input("Введіть n: "))
    return [i**2 for i in range(1, n+1)]

def get_students_data():
    students = {}
    while True:
        name = input("Введіть ім'я студента або 'stop' для завершення: ")
        if name == 'stop':
            return students
        grade = int(input(f"Введіть оцінку для {name}: "))
        if name in students:
            students[name].append(grade)
        else:
            students[name] = [grade]

def main():
    while True:
        print("\nВиберіть задачу:")
        print("1 - Перевірка віку")
        print("2 - Піраміда з зірочок")
        print("3 - Речення задом наперед")
        print("4 - Найчастіша буква")
        print("5 - Список та кортеж")
        print("6 - Генерація квадратів чисел")
        print("7 - Введення даних студентів")
        print("q - Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            print(check_age())
        elif choice == "2":
            draw_pyramid()
        elif choice == "3":
            print(reverse_sentence())
        elif choice == "4":
            letter, count = most_frequent_letter()
            print(f"Найчастіше: {letter}\nВходження: {count}")
        elif choice == "5":
            l, t, s, avg = list_and_tuple()
            print(f"Список: {l}\nКортеж: {t}\nСума: {s}\nСереднє арифметичне: {avg}")
        elif choice == "6":
            print(generate_squares())
        elif choice == "7":
            students = get_students_data()
            for name, grades in students.items():
                print(name, grades)
        elif choice == "q":
            break

if __name__ == "__main__":
    main()
