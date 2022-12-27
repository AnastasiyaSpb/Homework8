import view
import data_base as bd
import methods as m


def button_click():
    a = view.choice()
    match a:
        case 1:                          # вывод всего справочника
            bd.show_data()
        case 2:                          # поиск информации
            if a == 2:
                t = view.search_data()
            elif a == 4:
                t = view.change_data()
            d = bd.create_dict()
            c = m.count_info(d, t)
            if c == 0:
                print("Не найдено")
            elif c == 1:
                view.view_result(m.find_info(d, t))
            elif c >= 2:
                print("--------------")
                print(f"Найдено {c} совпадений")
                while c:
                    view.view_result(m.find_info(d, t))
                    d = m.del_info(d, t)
                    c -= 1
        case 3:                          # добавление информации
            b = view.enter_data()
            bd.add_data(b)
        case 4:                          # удаление информации
            p = view.del_data()
            bd.unpack_dict(m.del_info(bd.create_dict(), p))
        case _:
            print("Ты ввел некорректные данные")
