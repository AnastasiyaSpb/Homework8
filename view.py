def choice():
    return int(input("Добро пожаловать в справочник!\
\n--------------\n\
Нажми 1 для вывода всего справочника\n\
Нажми 2 для поиска информации\n\
Нажми 3 для добавления данных\n\
Нажми 4 для удаления данных\n\
Нажми 5 для изменения данных\n\
Нажми 6 для перевода справочника в csv формат\n\
--------------\n\
Твой выбор: "))


def enter_data():
    print("--------------")
    s = input("Фамилия: ")
    n = input("Имя: ")
    t = input("Номер телефона: ")
    c = input("Комментарий: ")
    print("--------------")
    return s + "\n" + n + "\n" + t + "\n" + c + "\n"


def search_data():
    print("--------------")
    return input("Что будем искать?: ")

def show_choice():
    print("--------------")
    return int(input("Нажми 1 для вывода в обычном формате, нажми 2 для вывода в csv формате: "))

def del_data():
    print("--------------")
    return input("Что будем удалять?: ")


def change_data():
    print("--------------")
    a = input("Чьи данные ты хочешь изменить?\n")
    b = input("Что ты хочешь изменить? Нажми 1 если фамилию, 2 - имя, 3 - телефон, 4 - комментарий\n")
    c = input("Введи новую информацию\n")
    return a, b, c


def view_result(data):
    print("--------------")
    if data == None:
        print("Не найдено")
    else:
        for el in data:
            print(
                f"Фамилия: {el[0]}\nИмя: {el[1]}\nНомер телефона: {el[2]}\nКомментарий: {el[3]}")
            print("--------------")
