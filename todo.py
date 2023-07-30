import sys
import os

command_help = ("\nadd 'текст задачи в ковычках' - Добавлет новую задачу.\n"
                "\nedit number 'text' - Изменяет задачу по номеру.\n"
                "\nremove number - Удаляет задачу из списка по номеру.\n"
                "\nremove all - Удаляет все задачи из списка.")


def todos_list():
    with open('list_of_entries.txt', encoding='utf-8') as write_line:
        todos = write_line.read().split('\n')
        todos.pop(-1)
    return todos


def write_entries():
    if os.path.isfile("list_of_entries.txt"):
        if os.stat('list_of_entries.txt').st_size != 0:
            todos = todos_list()
            todos_new = []
            for i in todos:
                index = todos.index(i)
                index += 1
                todos_new.append(str(index) + "." + i)
            print("Весь список дел:")
            for i in todos_new:
                print(i)

        else:
            print("Пока что нет записей...")


def add():
    entries_text = sys.argv[2]
    with open('list_of_entries.txt', 'a+', -1, 'utf-8') as entries_add:
        entries_add.writelines(entries_text + "\n")
    print("Задача успешно добавлена!")
    sys.exit()


def edit(number, text):
    if os.stat('list_of_entries.txt').st_size != 0:
        todos = todos_list()
        number = int(number) - 1
        todos[number] = text
        with open('list_of_entries.txt', 'w', -1, 'utf-8') as edit_line:
            for i in todos:
                edit_line.write(i + '\n')

        print("ЗАДАНИЕ", number + 1, "ИЗМЕНЕНО!")
    else:
        print("НЕВЕРНАЯ КОМАНДА! В СПИСКЕ НЕТ ЗАДАЧ!")
        print(command_help)

    sys.exit()


def remove(number):
    if sys.argv[2] == "all":
        with open('list_of_entries.txt', 'w', -1, 'utf-8'):
            print("Список дел очищен!")
    else:
        if os.stat('list_of_entries.txt').st_size != 0:
            todos = todos_list()
            number = int(number) - 1
            todos.pop(number)
            with open('list_of_entries.txt', 'w', -1, 'utf-8') as edit_line:
                for i in todos:
                    edit_line.write(i + '\n')
            print("Задача номер", number + 1, "успешно удалена!")
        else:
            print("НЕВЕРНАЯ КОМАНДА! В СПИСКЕ НЕТ ЗАДАЧ!")
            print(command_help)
    sys.exit()


def h():
    if sys.argv[2] == "!":
        print(command_help)
        sys.exit()


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
        add()

    elif commands == "edit":
        edit(sys.argv[2], sys.argv[3])

    elif commands == "remove":
        remove(sys.argv[2])

    elif commands == "help":
        h()
