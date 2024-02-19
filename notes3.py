import json


def add_notes(thenote, title, body, id, datetime):
    notes = {
        'title': title,
        'body': body,
        'id': id,
        'datetime': datetime
    }
    thenote.append(notes)
    print('заметка добавлена')

def save_to_file(filename, notese):
    with open(filename, 'w',encoding='utf-8') as file:
        json.dump(notese, file, indent=4)
        print('заметка сохранена')
        

def views_notese(thenote):
    for index, notes in enumerate(thenote, start=1):
        print(f"{index}. {notes['title']}, {notes['body']}, {notes['id']}, {notes['datetime']}\n")


def edit_notes(thenote, search_key, new_data):
    for notes in thenote:
        if (search_key.lower() in notes['title'].lower() or search_key.lower() in notes['id'].lower()):
            notes.update(new_data)
            print('заметка изменена')
            return
    print('заметка не найдена')
    
def delete_notes(thenote,search_key ):
    
    for notes in thenote[:]:
        if (search_key.lower() in notes['id'].lower() or search_key.lower()):
            thenote.remove(notes)
            print('заметка удалена')
            return
    print('заметка не найдена')

def main():
    thenote = []
    filename = 'notese.json'

    while True:
        print("1. Добавить заметку")
        print("2. Сохранить заметку")
        print("3. Вывести все заметки")
        print("4. Изменить заметку")
        print("5. Удалить заметку")
        print("6. Выйти")

        choice = input('Выберите действие: ')
        if choice == '1':
            last_title= input('введите заголовок: ')
            first_body = input('введи тему: ')
            id = input('введите id номер(цифры 1-100): ')
            datetime = input('введите дату и врему в формате дд/мм/гггг чч.мм.сс: ')
            add_notes(thenote, last_title, first_body, id, datetime)
        elif choice == '2':
            save_to_file(filename, thenote)
        elif choice == '3':
            views_notese(thenote)
        elif choice == '4':
            search_key = input("Введите заголовок или id для изменения: ")
            new_title = input('Введите Новый заголовок: ')
            new_body = input('Введите Новая тема: ')
            new_id = input('Введите Новый id: ')
            new_datetime = input('Введите Новые дата и время: ')
            new_data = {
                'title': new_title,
                'body': new_body,
                'id': new_id,
                'datetime': new_datetime
            }
            edit_notes(thenote, search_key, new_data)
        elif choice == '5':
            search_key = input("Введите id для удаления: ")
            delete_notes(thenote, search_key)
        elif choice == '6':
            break
        else:
            print('Некорректный выбор. Попробуйте снова')

if __name__ == "__main__":
    main()