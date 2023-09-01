import sys
from todo_classes import TodoManager


def help():
    print("\nadd 'текст задачи в ковычках' - Добавлет новую задачу.\n"
          "\nedit number 'text' - Изменяет задачу по номеру.\n"
          "\nremove number - Удаляет задачу из списка по номеру.\n"
          "\nremove all - Удаляет все задачи из списка.")


def save_ask(todos_in_file):
    save_question = input("Сохранить изменения? Y/Да\n").lower()
    if save_question == 'y':
        todos_in_file.save()
        print("Изменения сохранены!")
    elif save_question != 'y':
        print("Данные не сохранены!")


def write_entries(todos_in_file):
    if todos_in_file.empty:
        index = 1
        print("Весь список дел:")
        for todo in todos_in_file.file_list:
            print(str(index) + "." + todo)
            index += 1

    return


def add(todos_in_file, entries_text):
    repeat_todo = 0
    for todo in todos_in_file.file_list:
        if todo == entries_text:
            repeat_todo = 1
            break
    if repeat_todo:
        print("ОШИБКА! ТАКАЯ ЗАДАЧА УЖЕ СУЩЕСТВУЕТ!")
    else:
        todos_in_file.add(entries_text)
        save_question = input("Сохранить изменения? Y/Да\n").lower()
        if save_question == 'y':
            todos_in_file.save()
            print("Изменения сохранены!")
            print("Задача успешно добавлена!")
        else:
            print("Данные не сохранены!")

    return


def edit(todos_in_file, number, text):
    if number.isdigit():
        if number != text:
            if todos_in_file.empty:
                index = int(number) - 1
                todos_in_file.update(index, text)
                if todos_in_file.update(index, text):
                    print("ЗАДАНИЕ", number, "ЗАМЕНЕНО!")
                    save_ask(todos_in_file)
                else:
                    print("НЕВЕРНАЯ КОМАНДA! ЗАДАЧА С ТАКИМ НОМЕРОМ НЕ СУЩЕСТВУЕТ")

            else:
                print("ОШИБКА! СПИСОК ЗАДАЧ ПУСТ!")

        else:
            print("НЕВЕРНАЯ КОМАНДA!")
            help()
    else:
        print("НЕВЕРНАЯ КОМАНДA!")
        help()
    return


def remove(todos_in_file, number):
    if number == "all":
        if todos_in_file.empty:
            todos_in_file.delete_all()
            print("Список дел очищен!")
            save_ask(todos_in_file)
        else:
            print("ОШИБКА! СПИСОК ЗАДАЧ ПУСТ!")
            help()
    else:
        if todos_in_file.empty:
            if number.isdigit():
                index = int(number)
                if todos_in_file.delete(index - 1):
                    print("Задача номер", number, "успешно удалена!")
                    save_ask(todos_in_file)
                else:
                    print("НЕВЕРНАЯ КОМАНДА! ЗАДАЧА С ТАКИМ НОМЕРОМ НЕ СУЩЕСТВУЕТ!")
                    help()
            else:
                print("НЕВЕРНАЯ КОМАНДA!")
                help()
        else:
            print("ОШИБКА! СПИСОК ЗАДАЧ ПУСТ!")
            help()
    return


command_by_name = {
    'help': (help, 0),
    'add': (add, 1),
    'edit': (edit, 2),
    'remove': (remove, 1),
}


def main():
    todos_in_file = TodoManager()

    if len(sys.argv) == 1:
        write_entries(todos_in_file)
        return

    command_name = sys.argv[1]

    if command_name not in command_by_name:
        print("НЕВЕРНАЯ КОМАНДA!")
        help()
        return

    func, args_number = command_by_name[command_name]
    args = sys.argv[2:]

    if args_number != len(args):
        print("КОММАНДА ВВЕДЕНА НЕВЕРНО!")
        help()
        return

    elif command_name == "help":
        help()
        return

    else:
        func(todos_in_file, *args)
        return


if __name__ == '__main__':
    main()
