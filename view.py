def choice():
    return int(input("--------------\n\
Добро пожаловать в справочник!\
\n--------------\n\
Нажми 1 для вывода всего справочника\n\
Нажми 2 для поиска информации\n\
Нажми 3 для добавления данных\n\
Нажми 4 для удаления данных\n\
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


def del_data():
    print("--------------")
    return input("Что будем удалять?: ")


def view_result(data):
    print("--------------")
    print(
        f"Фамилия: {data[0]}\nИмя: {data[1]}\nНомер телефона: {data[2]}\nКомментарий: {data[3]}")
