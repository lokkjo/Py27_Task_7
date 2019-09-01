documents = [
    {"type": "passport", "number": "2207 876234",
     "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2",
     "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "12002",
     "name": "Василий Гупкин"},
    {"type": "another_note", "number": "1321 26",}, # тестовый словарь
    {"type": "insurance", "number": "10006",
     "name": "Аристарх Павлов"},
    {"type": "wrong_note", "number": "1026"} # тестовый словарь
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': ['1321 26', '1026', '12002'] # номера из тестовых словарей
}

# Функции проверки по существующим записям

def existing_doc_number_check(num_input=None):
    existing_docs = []
    for document in documents:
        existing_docs.append(document['number'])
    if num_input in existing_docs:
        return True
    else:
        return False

def existing_shelf_number_check(shelf_input=None):
    existing_shelves = list(directories.keys())
    if shelf_input in existing_shelves:
        return True
    else:
        return False

# Функции рабочих команд

def name_list(): # Функция для задания 7-3, вызывается командой 'n'
    counter = 0
    names_dict = {}
    for document in documents:
        try:
            counter += 1
            names_dict.update({counter: [document['number'],
                                         document['name']]})
        except Exception as e:
            if isinstance(e, KeyError):
                names_dict.update({counter: [document['number'],
                                             'Имени не указано']})
    for item in names_dict.items():
        print(f'{item[0]}: {item[1][1]}, {item[1][0]}')


def add_shelf(new_shelf_number=None):
    if new_shelf_number == None:
        new_shelf_number = input("Введите номер новой полки: ")
    if existing_shelf_number_check(new_shelf_number) == True:
        print('Такая полка уже есть')
        return None
    else:
        directories[new_shelf_number] = []


def people():
    num_input = input("Введите номер документа: ")
    for document in documents:
        if str(num_input) == document['number']:
            return document['name']
    return f'Документа №{num_input} не существует'


def list_action():
    counter = 0
    for document in documents:
        counter += 1
        result = (
            f'{document["type"]} "{document["number"]}" '
            f'"{document["name"]}"')
        print(result)
    print(f'\nВсего документов в базе: {counter}')


def shelf():
    num_input = input("Введите номер документа: ")
    shelf_list = directories.items()
    for shelf in shelf_list:
        if num_input in shelf[1]:
            return f'\nПолка номер {shelf[0]}'
    return 'Неверный номер'


def add():
    new_doc = {
        'type': input('Введите тип нового документа: '),
        'number': input('Введите номер нового документа: '),
        'name': input('Введите имя владельца документа: ')
    }
    while existing_doc_number_check(new_doc['number']) == True:
        print(f'\nДокумент №{new_doc["number"]} уже существует.')
        new_doc['number'] = input('Введите правильный номер: ')
    documents.append(new_doc)
    shelf_input = input('Введите номер полки для документа: ')
    if shelf_input not in directories.keys():
        add_shelf(shelf_input)
    new_doc_list = [new_doc['number']]
    directories[shelf_input] = directories[
                                   shelf_input] + new_doc_list
    print(f'Документ №{new_doc["number"]} добавлен '
          f'на полку {shelf_input}')



def delete():
    num_input = input("Введите номер документа: ")
    if existing_doc_number_check(num_input) == False:
        print(f'Документа №{num_input} не существует')
        return None
    shelf_list = directories.items()
    for document in documents:
        if str(num_input) == document['number']:
            documents.remove(document)
    for space in shelf_list:
        if num_input in space[1]:
            space[1].remove(num_input)
    directories[space[0]] = space[1]
    print(f'Документ №{num_input} удалён из системы.')


def move():
    num_input = input("Введите номер документа: ")
    if existing_doc_number_check(num_input) == False:
        print(f'Документа №{num_input} не существует')
        return None
    shelf_number = input("Введите полку, куда поместить документ: ")
    if existing_shelf_number_check(shelf_number) == False:
        add_shelf(shelf_number)
    shelf_list = directories.items()
    for space in shelf_list:
        if num_input in space[1]:
            space[1].remove(num_input)
    directories[space[0]] = space[1]
    directories[shelf_number] = (directories[shelf_number] +
                                 [num_input])
    print(f'Документ №{num_input} перемещён на полку №{shelf_number}')



def help_text():
    return ("Чтобы получить имя владельца по номеру документа,\n\
        введите р.\n\
Чтобы получить список всех документов,\n\
        введите l.\n\
Чтобы получить список владельцев всех документов\n\
        введите n. \n\
Чтобы узнать номер полки, на которой лежит документ,\n\
        введите s.\n\
Чтобы добавить новый документ в систему,\n\
        введите a.\n\
Чтобы удалить документ из системы,\n\
        введите d.\n\
Чтобы добавить новую полку для документов,\n\
        введите as.\n\
Чтобы переместить документ на другую полку,\n\
        введите m.\n\
Чтобы получить данный список команд,\n\
        введите h.\n\
Чтобы выйти из системы,\n\
        введите exit.\n\
\nЖелаем вам продуктивной работы!")


def user_interface():
    command_input: str = (input('\nВведите нужную команду: \n>'))
    if command_input == 'p':
        print(people())
        user_interface()
    elif command_input == 'l':
        list_action()
        user_interface()
    elif command_input == 's':
        print(shelf())
        user_interface()
    elif command_input == 'a':
        add()
        user_interface()
    elif command_input == 'd':
        delete()
        user_interface()
    elif command_input == 'as':
        add_shelf()
        user_interface()
    elif command_input == 'm':
        move()
        user_interface()
    elif command_input == 'n':
        name_list()
        user_interface()
    elif command_input == 'h':
        print(help_text())
        user_interface()
    elif command_input == 'exit':
        print('До встречи!')
        pass
    else:
        print('Команда не распознана.')
        user_interface()


def user_greeting():
    print('Здравствуйте!\n')
    print(help_text())
    user_interface()


user_greeting()
