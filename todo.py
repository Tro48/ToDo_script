import sys
import re

while True:
    entries = open('list_of_entries.txt', encoding='utf-8')
    print('Весь список дел:' "\n" + entries.read())
    entries.close()
    print('Для добавления задачи введите --add "текст"\nДля выхода введите "--exit"')
    command = input(">")
    exit_command = "--exit"
    if command == command:
        text_command = "--add "
        command_add = command.split(" ")[0]
        if command_add == "--add":
            text = command.split(text_command)[1]
            text = re.sub('"', '', text)
            entries_add = open('list_of_entries.txt', 'a+', -1, 'utf-8')
            entries_add.writelines(text + "\n")
            entries_add.close()

        elif command == exit_command:
            sys.exit()

        else:
            print("такой комманды нет")
            continue