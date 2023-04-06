def read_directory():
    print("Что вы хотите просмотреть: 1 - Весь справочник; 2 - Определенную запись в справочнике")
    read_input = int(input())
    phone_directory = open("phone_directory.txt", "r")
    directory = phone_directory.readlines()
    if read_input == 1:
        print()
        for line in directory:
            print(line, end = "")
        print()
    elif read_input == 2:
        print("Введите имя, номер телефона или коментарий интересующий вас:")
        clarification = input()
        print()
        find_lines = find_all_element_directory(directory, clarification)
        if find_lines == []:
            print("Такого в справочнике нет")
        else:
            for line in find_lines:
                print(line, end = "")
            print()
    print()
    phone_directory.close()

def append_new_in_directory():
    phone_directory = open("phone_directory.txt", "a")
    name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    comment = input("Введите коментарий: ")
    phone_directory.writelines(f"\n{name} - {phone_number} - {comment}")
    phone_directory.close()

def find_all_element_directory(data, element):
    lines = []
    for line in data:
        words = line.split(" - ")
        for parameter in words:
            if element == parameter:
                lines.append(line)
    return lines

def change_directory():
    phone_directory1 = open("phone_directory.txt", "r")
    print("Введите элемент который хотите изменить:")
    replaced_element = input()
    directory = phone_directory1.readlines()
    replaced_lines = find_all_element_directory(directory, replaced_element)
    if replaced_lines == []:
        print()
        print("Такого элемента нет")
    else:
        print("Введите элемент на который вы хотите заменить:")
        replacing_element = input()
        for line in replaced_lines:
            split_replaced_line = line.split(" - ")
            split_replaced_line.insert(split_replaced_line.index(replaced_element), replacing_element)
            split_replaced_line.pop(split_replaced_line.index(replaced_element))
            replacing_line = " - ".join(split_replaced_line)
            directory.insert(directory.index(line), replacing_line)
            directory.pop(directory.index(line))
        phone_directory2 = open("phone_directory.txt", "w")
        for line in directory:
            phone_directory2.writelines(line)
        phone_directory2.close()
        print()
        print("Готово")
    phone_directory1.close()
    print()
        
def delete_element_directory():
    phone_directory1 = open("phone_directory.txt", "r")
    print("Введите элемент, записи с которым вы хотите удалить:")
    remote_element = input()
    directory = phone_directory1.readlines()
    remote_lines = find_all_element_directory(directory, remote_element)
    if remote_element == []:
        print("Такого элемента в справочнике нет")
    else:
        for line in remote_lines:
            directory.pop(directory.index(line))
        phone_directory2 = open("phone_directory.txt", "w")
        for line in directory:
            phone_directory2.writelines(line)
        phone_directory2.close()
    phone_directory1.close()
    print()

menu_user_input = None

while menu_user_input != 9:
    print("Выберите команду: 1 - Просмотр справочника; 2 - Добавление новых данных в справочник; 3 - Изменение справочника; 4 - Удалиение данных из справочника; 9 - Прекращение работы")
    menu_user_input = int(input())
    if menu_user_input == 1:
        read_directory()
    elif menu_user_input == 2:
        append_new_in_directory()
    elif menu_user_input == 3:
        change_directory()
    elif menu_user_input == 4:
        delete_element_directory()
    



