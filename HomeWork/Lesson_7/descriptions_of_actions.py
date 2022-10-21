def start():
    return main_block()


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input('Ваш выбор: '))
    return choice


def intermediate():
    check = input('Хотите продолжить работу?: ').lower()
    while True:
        if check == 'да' or check == 'нет':
            break
        else:
            check = input('Ошибка, некорректный ввод, попробуйте еще раз: ').lower()
    match check:
        case 'да':
            return main_block(show_menu())
        case "нет":
            return stop()


def show_all(filename: str):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            print(dict(zip(fields, line.strip().split(','))))
    intermediate()


def find_second_name(second_name: str):
    for i in read_csv('phonebook.csv'):
        if (i["Фамилия"]) == second_name.capitalize():
            print(i)
            intermediate()
    print('Нет контакта с такой фамилией')
    intermediate()


def find_number(phone_number):
    for i in read_csv('phonebook.csv'):
        if (i["Телефон"]) == phone_number:
            print(i)
            intermediate()
    print('Нет контакта с таким номером телефона')
    intermediate()


def add_to_directory():
    with open('phonebook.csv', 'a', encoding='utf-8') as fin:
        fin.writelines(input('введите Фамилию: ') + ',')
        fin.writelines(input('введите Имя: ') + ',')
        fin.writelines(input('введите телефон: ') + ',')
        fin.writelines(input('введите описание: '))
    intermediate()


def save_in_txt():
    with open('phones.txt', 'w', encoding='utf-8') as txt:
        for i in read_csv('phonebook.csv'):
            txt.writelines(f'{i} \n')
    print('Ваш файл готов')
    intermediate()
    return txt
    


def stop():
    return print('Конец работы')


def main_block(numb: int = show_menu()):
    match numb:
        case 1:
            show_all('phonebook.csv')
        case 2:
            find_second_name(input('Введите фамилию: '))
        case 3:
            find_number(input('Введите номер телефона: '))
        case 4:
            add_to_directory()
        case 5:
            save_in_txt()
        case 6:
            stop()
        case _: 
            print('Введено некорректное значение')
            main_block(show_menu())

