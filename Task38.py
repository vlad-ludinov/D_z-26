def read_directory():
    print("Что вы хотите просмотреть: 1 - Весь справочник; 2 - Определенную запись в справочнике")
    read_input = int(input())
    phone_directory = open("phone_directory.txt", "r")
    directory = phone_directory.readlines()
    if read_input == 1:
        for line in directory:
            print(line, end = "")
        print()
    elif read_input == 2:
        print("Введите имя, номер телефона или коментарий интересующий вас:")
        clarification = input()
        find_line = find_element_directory(directory, clarification)
        if find_line == None:
            print("Такого в справочнике нет")
            print()
        else:
            print(find_line)
    phone_directory.close()

def append_new_in_directory():
    phone_directory = open("phone_directory.txt", "a")
    name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    comment = input("Введите коментарий: ")
    phone_directory.writelines(f"\n{name} - {phone_number} - {comment}")
    phone_directory.close()

def find_element_directory(data, element):
    for line in data:
        words = line.split(" - ")
        for parameter in words:
            if element == parameter:
                return line

menu_user_input = None

while menu_user_input != 9:
    print("Выберите команду: 1 - Просмотр справочника; 2 - Добавление новых данных в справочник; 3 - Изменение справочника; 4 - Удалиение данных из справочника; 9 - Прекращение работы")
    menu_user_input = int(input())
    if menu_user_input == 1:
        read_directory()
    elif menu_user_input == 2:
        append_new_in_directory()
    



