import view
import data_base as bd
import methods as m
import logg as l


def button_click():
    l.log()
    a = view.choice()
    match a:
        case 1:                          # вывод всего справочника
            print("--------------")
            bd.show_data()
        case 2:                          # поиск информации
            view.view_result(m.search_data(
                bd.create_dict(), view.search_data()))
        case 3:                          # добавление информации
            b = view.enter_data()
            bd.add_data(b)
            bd.csv_format(bd.create_dict())
            print("Готово")
        case 4:                          # удаление информации
            p = view.del_data()
            bd.unpack_dict(m.del_info(bd.create_dict(), p))
            bd.csv_format(bd.create_dict())
            print("--------------")
            print("Готово")
        case 5:                          # изменение информации
            ch, ph, new_info = view.change_data()
            b = bd.create_dict()
            search_res = m.search_data(b, ch)
            if search_res == None:
                print("Не найдено элементов для замены")
            elif len(search_res) == 1:
                bd.unpack_dict(m.change_data(bd.create_dict(), search_res, int(ph), new_info))
            else:
                print(f"Найдено {len(search_res)} контактов")
                view.view_result(search_res)
                i = int(input("Введи номер контакта который ты хочешь заменить: "))
                s = search_res[i-1]
                bd.unpack_dict(m.change_data(bd.create_dict(), s, int(ph), new_info))
            bd.csv_format(bd.create_dict())
            print("--------------")
            print("Готово")           
        case 6:                          # вывод в формате csv
            bd.csv_format(bd.create_dict())
            print("--------------")
            print("Готово. Смотри data_new.txt")   
        case _:
            print("--------------")
            print("Ты ввел некорректные данные")
