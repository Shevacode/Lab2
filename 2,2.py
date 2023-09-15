word = input("Введіть слово: ")
max_letter = max(word, key=word.count)
print("Найчастіше:", max_letter)
print("Входження:", word.count(max_letter))