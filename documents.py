documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]

directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}


def get_name(docs, number):
    documents = list(filter(lambda x: x['number'] == number, docs))
    if documents:
        return documents[0]['name']
    else:
        return 'Документа с таким номером нет'


def get_shelf(dirs, number):
    for key, value in dirs.items():
        if number in value:
            return key
    return 'В полках документа с данным номером нет.'


def get_list(docs):
    for x in docs:
        type = x['type']
        number = x['number']
        name = x['name']
        print('{0} "{1}" "{2}"'.format(type, number, name))


def get_add_doc(docs, shelfs, shelf, type, number, name):
    doc = {'type': type, 'number': number, 'name': name}
    docs.append(doc)
    shelfs[shelf].append(doc['number'])
    return 'Документ добавлен'


def get_delete(doc_num):
    initial_len = len(documents)
    for i, d in enumerate(documents):
        if d['number'] == doc_num:
            documents.pop(i)

    if initial_len == len(documents):
        return 'Документ не существует'

    for key, value in directories.items():
        if doc_num in value:
            value.remove(doc_num)

    return 'Документ успешно удален'


def get_move(doc_number, shelf_id):
    doc_existence = False

    if shelf_id not in directories:
        return 'Полки не существует'

    for key, value in directories.items():
        if doc_number in value:
            doc_existence = True
            directories[shelf_id] += [doc_number]
            value.remove(doc_number)

    if doc_existence:
        return 'Документ успешно перемещен'
    else:
        return 'Документ не существует'


def get_as(doc_type, doc_number, doc_owner, shelf_id):
    if shelf_id not in directories:
        return 'Полки не существует'

    new_doc = dict(type=doc_type, number=doc_number, name=doc_owner)

    documents.append(new_doc)
    directories[shelf_id] += [doc_number]
    return 'Документ успешно добавлен'


def secretary_documents():
    """
        p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
        s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
        Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
        l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
        a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
        имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию,
        когда пользователь будет пытаться добавить документ на несуществующую полку
        d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий,
        когда пользователь вводит несуществующий документ;
        m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы,
        когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
        as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай,
        когда пользователь добавляет полку, которая уже существует.;
        q - для выхода из прогарммы
    """
    while True:
        print(
            f'Возможные команды: p, s, l, a, d, m, as, \nДля подробной информации введите команду help'
        )
        comand = input('Введите название команды: ')

        if comand == 'p':
            num = input('Введите номер документа: ')
            print(get_name(documents, num))

        elif comand == 's':
            num = input('Введите номер документа: ')
            print(f'Документ находится на полке: ',
                  {get_shelf(directories, num)})

        elif comand == 'l':
            print(f'{get_list(documents)}')

        elif comand == 'a':
            shelf = input('Введите номер полки куда положить документ: ')
            if shelf in directories.keys():
                type = input('Введите тип документа: ')
                number = int(input('Введите номер документа: '))
                name = input('Введите имя владельца документа: ')
                print(
                    f'{get_add_doc(documents, directories, shelf, type, number, name)}'
                )
            else:
                print('Номер полки введен не верно')

        elif comand == 'd':
            doc_num = input(
                'Введите номер документа, который хотите удалить: ')
            print(f'{get_delete(doc_num)}')

        elif comand == 'm':
            doc_number = input(
                "Введите номер документа,который хотите переместить: ")
            shelf_id = input(
                "Введит номер полки, на которую хотите переместить документ: ")
            print(f'{get_move(doc_number, shelf_id)}')

        elif comand == 'as':
            doc_type = input('Введите тип докемента: ')
            doc_number = input('Введите номер документа: ')
            doc_owner = input('Введите имя владельца документа: ')
            shelf_id = input('Введит номер полки: ').format(directories.keys())
            print(f'{get_as(doc_type, doc_number, doc_owner, shelf_id)}')

        elif comand == 'q':
            break


if __name__ == '__main__':
    secretary_documents()
