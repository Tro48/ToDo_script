import sys
import os

command_help = ("\nadd 'текст задачи в ковычках' - Добавлет новую задачу.\n"
                "\nedit number 'text' - Изменяет задачу по номеру.\n"
                "\nremove number - Удаляет задачу из списка по номеру.\n"
                "\nremove all - Удаляет все задачи из списка.")


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


def edit_line(number, text):
    entries_list = []
    with open('list_of_entries.txt', encoding='utf-8') as lines:
        for line in lines:
            current_line = line[:-1]
            entries_list.append(current_line)
        text = str(number) + "." + text
        number -= 1
        entries_list[number] = text

    with open('list_of_entries.txt', 'w', -1, 'utf-8') as new_lines:
        for i in entries_list:
            new_lines.writelines(i + "\n")


def delete_line(number_line):
    entries_list = []
    new_entries = []
    with open('list_of_entries.txt', encoding='utf-8') as lines:
        for line in lines:
            current_line = line[:-1]
            entries_list.append(current_line)
        number_line -= 1
        entries_list.pop(number_line)
        for i in entries_list:
            index = entries_list.index(i)
            index += 1
            index = str(index)
            text = i.split(".")[1]
            new_entries.append(index + "." + text)
    with open('list_of_entries.txt', 'w', -1, 'utf-8') as new_lines:
        for i in new_entries:
            new_lines.writelines(i + "\n")


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
    print("НЕВЕРНАЯ КОМАНДА!")
    print(command_help)
    sys.exit()


else:
    commands = sys.argv[1]
    if commands == "add":
        entries_text = sys.argv[2]
        add_line(entries_text)
        sys.exit()

    elif commands == "edit":
        if os.stat('list_of_entries.txt').st_size != 0:
            number_line = int(sys.argv[2])
            new_line = str(sys.argv[3])
            edit_line(number_line, new_line)
            print("Задача номер " + str(number_line) + " успешно заменена!")
        else:
            print("НЕВЕРНАЯ КОМАНДА! В СПИСКЕ НЕТ ЗАДАЧ!")
            print(command_help)
        sys.exit()

    elif commands == "remove":
        if sys.argv[2] == "all":
            with open('list_of_entries.txt', 'w', -1, 'utf-8') as del_all:
                print("Список дел очищен!")
        else:
            if os.stat('list_of_entries.txt').st_size != 0:
                number_line = sys.argv[2]
                number_line = int(number_line)
                delete_line(number_line)
                print("Задача номер " + str(number_line) + " успешно удалена!")
            else:
                print("НЕВЕРНАЯ КОМАНДА! В СПИСКЕ НЕТ ЗАДАЧ!")
                print(command_help)
        sys.exit()

    elif commands == "command":
        if sys.argv[2] == "help":
            print(command_help)
            sys.exit()
