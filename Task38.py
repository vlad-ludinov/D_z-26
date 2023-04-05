
def read_all_directory():
    phone_directory = open("phone_directory.txt", "r")
    directory = phone_directory.readlines()
    for line in directory:
        print(line, end = "")
    phone_directory.close()



menu_user_input = None

while menu_user_input != 9:
    print("Выберите команду: 1 - Просмотр справочника; 2 - Добавление новых данных в справочник; 3 - Изменение справочника; 4 - Удалиение данных из справочника; 9 - Прекращение работы")
    menu_user_input = int(input())
    if menu_user_input == 1:
        print("Что вы хотите просмотреть: 1 - Весь справочник; 2 - Определенную запись в справочнике")
        read_input = int(input())
        print(read_input)
        if read_input == 1:
            read_all_directory()
            print()

