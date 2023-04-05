def read_directory():
    print("Что вы хотите просмотреть: 1 - Весь справочник; 2 - Определенную запись в справочнике")
    read_input = int(input())
    phone_directory = open("phone_directory.txt", "r")
    directory = phone_directory.readlines()
    if read_input == 1:
        for line in directory:
            print(line, end = "")
    elif read_input == 2:
        print("Введите имя, номер телефона или коментарий интересующий вас:")
        clarification = input()
        flag = False
        for line in directory:
            words = line.split(" - ")
            for parameter in words:
                if clarification == parameter:
                    print(line, end = "")
                    flag = True
        if not flag:
            print("Такого в справочнике нет")
    print()
    phone_directory.close()


menu_user_input = None

while menu_user_input != 9:
    print("Выберите команду: 1 - Просмотр справочника; 2 - Добавление новых данных в справочник; 3 - Изменение справочника; 4 - Удалиение данных из справочника; 9 - Прекращение работы")
    menu_user_input = int(input())
    if menu_user_input == 1:
        read_directory()



