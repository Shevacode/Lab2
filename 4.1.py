students = {}
while True:
    name = input("Введіть ім'я студента або 'stop' для завершення: ")
    if name == 'stop':
        break
    grade = int(input(f"Введіть оцінку для {name}: "))
    students[name] = grade
print(students)