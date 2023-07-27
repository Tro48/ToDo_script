import sys
import os


def add_line(text):
    with open('list_of_entries.txt', 'a+', -1, 'utf-8') as entries_add:
        entries_add.writelines(text + "\n")
        entries_add.close()
    with open('list_of_entries.txt', encoding='utf-8') as entries:
        print("Новое задание добавлено в список!")
        print('Новый список дел:' "\n" + entries.read())


if os.path.isfile("list_of_entries.txt"):

    with open('list_of_entries.txt', encoding='utf-8') as entries:
        print('Весь список дел:' "\n" + entries.read())

else:
    print("Пока что нет записей...")

if len(sys.argv) == 1:
    print("Это Help. Что бы добавить задачу введите add 'Текст задачи в ковычках'.")
    sys.exit(1)
elif len(sys.argv) < 3:  # Проверка на пустую строку после add
    print("Ошибка! Вы не ввели задание!")
    sys.exit(1)


else:
    commands = sys.argv[1]

    if commands == "add":
        entries_text = sys.argv[2]
        add_line(entries_text)
        sys.exit(2)
    else:
        print("такой комманды нет!")
        with open('list_of_entries.txt', encoding='utf-8') as entries:
            print('Весь список дел:' "\n" + entries.read())
