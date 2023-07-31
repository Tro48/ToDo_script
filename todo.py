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
            index = 1
            print("Весь список дел:")
            for todo in todos:
                print(str(index) + "." + todo)
                index += 1

        else:
            print("Пока что нет записей...")
    return


def add():
    entries_text = sys.argv[2]
    todos = todos_list()
    repeat_todo = 0
    for todo in todos:
        if todo == entries_text:
            repeat_todo = 1
    if repeat_todo == 1:
        print("ОШИБКА! ТАКАЯ ЗАДАЧА УЖЕ СУЩЕСТВУЕТ!")
    else:
        with open('list_of_entries.txt', 'a+', -1, 'utf-8') as entries_add:
            entries_add.write(entries_text + "\n")
        print("Задача успешно добавлена!")
    return


def edit(number, text):
    if os.stat('list_of_entries.txt').st_size != 0:
        todos = todos_list()
        number = int(number) - 1
        todos[number] = text
        with open('list_of_entries.txt', 'w', -1, 'utf-8') as edit_line:
            for todo in todos:
                edit_line.write(todo + '\n')
        print("ЗАДАНИЕ", number + 1, "ИЗМЕНЕНО!")
    else:
        print("НЕВЕРНАЯ КОМАНДА! В СПИСКЕ НЕТ ЗАДАЧ!")
        print(command_help)

    return


def remove(number):
    if sys.argv[2] == "all":
        with open('list_of_entries.txt', 'w', -1, 'utf-8'):
            print("Список дел очищен!")
    else:
        todos = todos_list()
        if os.stat('list_of_entries.txt').st_size != 0:
            if sys.argv[2].isdigit() == bool(True):
                if len(todos) >= int(sys.argv[2]):
                    number = int(number) - 1
                    todos.pop(number)
                    with open('list_of_entries.txt', 'w', -1, 'utf-8') as edit_line:
                        for todo in todos:
                            edit_line.write(todo + '\n')
                    print("Задача номер", number + 1, "успешно удалена!")
                else:
                    print("НЕВЕРНАЯ КОМАНДА! ЗАДАЧА С ТАКИМ НОМЕРОМ НЕ СУЩЕСТВУЕТ!")
                    print(command_help)
            else:
                print("НЕВЕРНАЯ КОМАНДA!")
                print(command_help)
        else:
            print("ОШИБКА! СПИСОК ЗАДАЧ ПУСТ!")
            print(command_help)
    return


if len(sys.argv) == 1:
    write_entries()
    sys.exit()
elif len(sys.argv) < 3:
    commands = sys.argv[1]
    if commands == "help":
        print("ПОМОЩЬ:")
        print(command_help)
    else:
        print("НЕВЕРНАЯ КОМАНДA!")
        print(command_help)
    sys.exit()


else:
    commands = sys.argv[1]
    if commands == "add":
        add()

    elif commands == "edit":
        todos = todos_list()
        if sys.argv[2].isdigit() == bool(True):

            if len(todos) >= int(sys.argv[2]):
                if sys.argv[2] != sys.argv[-1]:
                    edit(sys.argv[2], sys.argv[3])

                else:
                    print("НЕВЕРНАЯ КОМАНДA!")
                    print(command_help)

            else:
                print("НЕВЕРНАЯ КОМАНДA! ЗАДАЧА С ТАКИМ НОМЕРОМ НЕ СУЩЕСТВУЕТ")
                print(command_help)
        else:
            print("НЕВЕРНАЯ КОМАНДA!")
            print(command_help)

    elif commands == "remove":
        remove(sys.argv[2])
    sys.exit()
