import sys
import os


def write_entries():
    if os.path.isfile("list_of_entries.txt"):
        with open('list_of_entries.txt', encoding='utf-8') as entries:
            print('Весь список дел:' "\n" + entries.read())

    else:
        print("Пока что нет записей...")


def add_line(text):

    with open('list_of_entries.txt', 'a+', -1, 'utf-8') as entries_add:
        number = number_lines()
        n = str(number[-1] + 1)
        entries_add.writelines(n + "." + text + "\n")


        print("Новое задание добавлено в список!")


def edit_line():
    pass


def remove_line():
    pass


def number_lines():
    entries_list = []
    list_index = []
    if os.path.isfile("list_of_entries.txt"):
        if os.stat('list_of_entries.txt').st_size != 0:
            with open('list_of_entries.txt', encoding='utf-8') as lines:
                for line in lines:
                    current_line = line[:-1]
                    entries_list.append(current_line)
                for i in entries_list:
                    index = entries_list.index(i)
                    index += 1
                    list_index.append(index)
        else:
            list_index = [0]

        return list_index


if len(sys.argv) == 1:
    write_entries()
    sys.exit()
elif len(sys.argv) < 3:
    print("Ошибка! Вы не ввели задание!")
    sys.exit()


else:
    commands = sys.argv[1]

    if commands == "add":
        entries_text = sys.argv[2]
        add_line(entries_text)
        sys.exit()
    else:
        print("такой комманды нет!")
        print("Что бы добавить задачу введите add 'Текст задачи в ковычках'.")
