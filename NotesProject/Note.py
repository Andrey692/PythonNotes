
from datetime import datetime
import uuid
import csv



def add_note():
    title = input('Введите заголовок заметки: ').title()
    note = input('Введите тело заметки: ')
    note_id = str(uuid.uuid1())[0:3]
    date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    note_data = [note_id, title, note, date]
    
    try:
        with open('my_notes.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(note_data)
    except Exception as e:
        print(f"Произошла ошибка при записи заметки: {e}")
    print("ЗАМЕТКА УСПЕШНО СОЗДАНА")

    
def print_notes():
    try:
        with open('my_notes.csv', "r", encoding="utf-8") as fh:
            reader = csv.reader(fh)
            rows = list(reader)  # reader - итерируемый объект и может быть преобразован в список строк

        for row in rows:
            print(row)
    except Exception as e:
        print(f"Произошла ошибка при чтении заметок: {e}")

    print("выводим все заметки на экран")


def search_note():
    try:
        print(
            'Возможные варианты поиска:\n'
            '1. По id\n'
            '2. По заголовку'
            )
        var = input('выберите вариант поиска: ')
        while var not in ('1', '2', '3'):
            print('некорректный ввод!')
            var = input('выберите вариант поиска: ')
        
        search = input('Введите данные для поиска: ').title()

        found = False
        with open('my_notes.csv', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)  # Преобразуем объект reader в список строк

            for row_index, row in enumerate(rows):
                try:
                    # Определяем столбец, в котором будем искать
                    if var == '1':
                        column_index = 0  # Поиск по id
                    elif var == '2':
                        column_index = 1  # Поиск по заголовку
                    elif var == '3':
                        column_index = 3  # Поиск по дате
                    else:
                        print("Ошибка: Неправильный выбор варианта поиска")
                        return

                    # Проверяем, соответствует ли значение в найденном столбце критерию поиска
                    if row[column_index] == search:
                        print("Найдено:", row)
                        found = True

                        action = input("Хотите отредактировать (r) или удалить (d) эту заметку? ")
                        if action.lower() == 'r':
                            edit_note(rows, row_index)
                        elif action.lower() == 'd':
                            delete_note(rows, row_index)
                        else:
                            print("Некорректный выбор действия.")

                except IndexError:
                    print("Ошибка: Неправильный индекс столбца")
                    return
         # Записываем обновленные данные обратно в файл
        with open('my_notes.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(rows)

        if not found:
            print("Ничего не найдено с заданным критерием.")
    except FileNotFoundError:
        print("Ошибка: Файл не найден")
    except Exception as e:
        print("Произошла ошибка:", e)


def edit_note(rows, row_index):
    try:
        new_data = input("Введите новые данные через запятую (id, заголовок, текст, дата): ").split(',')
        rows[row_index] = new_data
        print("Заметка успешно отредактирована.")
    except Exception as e:
        print("Произошла ошибка при редактировании заметки:", e)


def delete_note(rows, row_index):
    try:
        del rows[row_index]
        print("Заметка успешно удалена.")
    except Exception as e:
        print("Произошла ошибка при удалении заметки:", e)


def interface():
    with open("my_notes.csv", 'a', encoding='utf-8'): 
        pass
    var = 0
    while var != '4':
        print(
           'Вас приветствует консольный блокнот!\n'
            'Возможные действия:\n'
            '1 -> Создать заметку\n'
            '2 -> Посмотреть все заметки\n'
            '3 -> Найти заметку\n'
            '4 -> Выход'
            )
        print()
        var = input('выберите вариант действия: ')
        while var not in ('1', '2', '3', '4'):
            print('некорректный ввод!')
            var = input('выберите вариант действия: ')
        print()    

        match var: 
            case '1':
                add_note()
            case '2':
                print_notes()
            case '3': 
                search_note()
            case '4':
                print('До свидания') 
        print()        


if __name__ == '__main__':
    interface()