import sys
from todo_classes import TodoManager

command_help = ("\nadd 'текст задачи в ковычках' - Добавлет новую задачу.\n"
                "\nedit number 'text' - Изменяет задачу по номеру.\n"
                "\nremove number - Удаляет задачу из списка по номеру.\n"
                "\nremove all - Удаляет все задачи из списка.")

command_by_name = {
    'help': "help",
    'add': "add",
    'edit': "edit",
    'remove': "remove",
}


def main():
    todos_in_file = TodoManager()

    def save_ask():
        save_question = input("Сохранить изменения? Y/Да\n").lower()
        if save_question == 'y':
            todos_in_file.save()
            print("Изменения сохранены!")
        elif save_question != 'y':
            print("Данные не сохранены!")

    def write_entries():
        if todos_in_file.ok:
            index = 1
            print("Весь список дел:")
            for todo in todos_in_file.file_list:
                print(str(index) + "." + todo)
                index += 1

        return

    def add():
        entries_text = sys.argv[2]
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

    def edit(number, text):
        if number.isdigit():
            if number != text:
                if todos_in_file.ok:
                    index = int(number) - 1
                    todos_in_file.update(index, text)
                    if todos_in_file.update(index, text):
                        print("ЗАДАНИЕ", number, "ЗАМЕНЕНО!")
                        save_ask()
                    else:
                        print("НЕВЕРНАЯ КОМАНДA! ЗАДАЧА С ТАКИМ НОМЕРОМ НЕ СУЩЕСТВУЕТ")
                        print(command_help)
                else:
                    print("ОШИБКА! СПИСОК ЗАДАЧ ПУСТ!")
                    print(command_help)
            else:
                print("НЕВЕРНАЯ КОМАНДA!")
                print(command_help)
        else:
            print("НЕВЕРНАЯ КОМАНДA!")
            print(command_help)
        return

    def remove(number):
        if sys.argv[2] == "all":
            with open('list_of_entries.txt', 'w', -1, 'utf-8'):
                print("Список дел очищен!")
        else:
            if todos_in_file.ok:
                if sys.argv[2].isdigit():
                    index = int(number) - 1
                    todos_in_file.delete(index)
                    if todos_in_file.delete(index):
                        print("Задача номер", number, "успешно удалена!")
                        save_ask()
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
        return

    elif len(sys.argv) < 3:
        commands = sys.argv[1]
        if commands == "help":
            print("ПОМОЩЬ:")
            print(command_help)
        else:
            print("НЕВЕРНАЯ КОМАНДA!")
            print(command_help)
        return
    else:
        commands = sys.argv[1]
        if commands == "add":
            add()

        elif commands == "edit":
            if sys.argv[2] != sys.argv[-1]:
                edit(sys.argv[2], sys.argv[3])
            else:
                print("НЕВЕРНАЯ КОМАНДA! ВВЕДИТЕ ТЕКСТ!")
                print(command_help)

        elif commands == "remove":
            remove(sys.argv[2])
        return


if __name__ == '__main__':
    main()
