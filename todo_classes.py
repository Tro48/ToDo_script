import os


class TodoManager:

    def __init__(self):
        if os.path.isfile("list_of_entries.txt"):
            if os.stat('list_of_entries.txt').st_size != 0:
                self.empty = True
                with open('list_of_entries.txt', encoding='utf-8') as write_line:
                    self.file_list = write_line.read().split('\n')
                    self.file_list.pop(-1)
            else:
                self.empty = False
                self.file_list = []
                print("Пока что нет записей...")
        else:
            with open('list_of_entries.txt', 'w', -1, 'utf-8'):
                self.empty = False
                self.file_list = []
                print("Пока что нет записей...")

    def add(self, text):
        self.file_list.append(text)

    def update(self, index, text):
        if len(self.file_list) > index:
            self.file_list[index] = text
            return True

        return False

    def delete(self, index):
        if len(self.file_list) > index:
            self.file_list.pop(index)
            return True

    def delete_all(self):
        self.file_list.clear()

    def save(self):
        with open('list_of_entries.txt', 'w', -1, 'utf-8') as edit_line:
            for todo in self.file_list:
                edit_line.write(todo + '\n')

    def list(self):
        return self.file_list
