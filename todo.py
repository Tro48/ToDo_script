import sys
import os


class TodoManager:

    def __init__(self):
        self.file_list = None

    def add(self, text):
        self.file_list.append(text)

    def update(self, num, text):
        number = int(num) - 1
        self.file_list[number] = text

    def delete(self, num):
        number = int(num) - 1
        self.file_list.pop(number)

    def save(self):
        save_question = input("Сохранить изменения? Y/Да N/Нет\n")
        if save_question == 'y':
            with open('list_of_entries.txt', 'w', -1, 'utf-8') as edit_line:
                for todo in self.file_list:
                    edit_line.write(todo + '\n')
                print("Изменения сохранены!")
        elif save_question == 'n':
            print("Данные не сохранены!")


    def list(self):
        with open('list_of_entries.txt', encoding='utf-8') as write_line:
            self.file_list = write_line.read().split('\n')
            self.file_list.pop(-1)


command_help = ("\nadd 'текст задачи в ковычках' - Добавлет новую задачу.\n"
                "\nedit number 'text' - Изменяет задачу по номеру.\n"
                "\nremove number - Удаляет задачу из списка по номеру.\n"
                "\nremove all - Удаляет все задачи из списка.")


todos_in_file = TodoManager()
todos_in_file.list()


def write_entries():
    if os.path.isfile("list_of_entries.txt"):
        if os.stat('list_of_entries.txt').st_size != 0:
            index = 1
            print("Весь список дел:")
            for todo in todos_in_file.file_list:
                print(str(index) + "." + todo)
                index += 1
        else:
            print("Пока что нет записей...")
    return


def add():
    entries_text = sys.argv[2]
    repeat_todo = 0
    for todo in todos_in_file.file_list:
        if todo == entries_text:
            repeat_todo = 1
    if repeat_todo == 1:
        print("ОШИБКА! ТАКАЯ ЗАДАЧА УЖЕ СУЩЕСТВУЕТ!")
    else:
        todos_in_file.add(entries_text)
        print("Задача успешно добавлена!")
        todos_in_file.save()

    return


def edit(number, text):
    if os.stat('list_of_entries.txt').st_size != 0:
        todos_in_file.update(number, text)
        print("ЗАДАНИЕ", number, "ЗАМЕНЕНО!")
        todos_in_file.save()
    else:
        print("НЕВЕРНАЯ КОМАНДА! В СПИСКЕ НЕТ ЗАДАЧ!")
        print(command_help)

    return


def remove(number):
    if sys.argv[2] == "all":
        with open('list_of_entries.txt', 'w', -1, 'utf-8'):
            print("Список дел очищен!")
    else:
        if os.stat('list_of_entries.txt').st_size != 0:
            if sys.argv[2].isdigit() == bool(True):
                if len(todos_in_file.file_list) >= int(sys.argv[2]):
                    todos_in_file.delete(number)
                    print("Задача номер", number, "успешно удалена!")
                    todos_in_file.save()

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
        if sys.argv[2].isdigit() == bool(True):

            if len(todos_in_file.file_list) >= int(sys.argv[2]):
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
