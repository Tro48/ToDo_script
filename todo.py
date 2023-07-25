import sys
import os

if os.path.isfile("list_of_entries.txt"):
    entries = open('list_of_entries.txt', encoding='utf-8')
    print('Весь список дел:' "\n" + entries.read())
    entries.close()
else:
    print("Пока что нет записей...")

if len(sys.argv) == 1:
    print("Это Help. Что бы добавить задачу введите add 'Текст задачи в ковычках'.")
    sys.exit(1)

if len(sys.argv) < 3:  # Проверка на пустую строку после add
    print("Ошибка! Вы не ввели задание!")
    sys.exit(1)
else:
    commands = sys.argv[1]

    if commands == "add":
        entries_text = sys.argv[2]
        entries_add = open('list_of_entries.txt', 'a+', -1, 'utf-8')
        entries_add.writelines(entries_text + "\n")
        entries_add.close()
        entries = open('list_of_entries.txt', encoding='utf-8')
        print("Новое задание добавлено в список!")
        print('Новый список дел:' "\n" + entries.read())
        entries.close()
        sys.exit(1)

    else:
        print("такой комманды нет!")
        entries = open('list_of_entries.txt', encoding='utf-8')
        print('Весь список дел:' "\n" + entries.read())
        entries.close()
