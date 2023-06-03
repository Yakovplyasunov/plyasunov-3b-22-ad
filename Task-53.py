class HomeTasks:
    def __init__(self, file_name):
        file = open(file_name, 'r')
        self.lst = [i.replace('\n', '') for i in file.readlines()]
        self.file_name = file_name
        file.close()

    def app_elem(self, elem):
        self.lst.append(elem)
        file = open(self.file_name, 'a')
        file.write(elem + '\n')
        file.close()

    def del_elem(self, elem):
        self.lst.remove(elem)

    def print_lst(self):
        print(self.lst)


hometasks = HomeTasks('test_f.txt')
hometasks.print_lst()
hometasks.app_elem('Сложить диван')
hometasks.print_lst()
hometasks.app_elem('Сложить')
hometasks.print_lst()
