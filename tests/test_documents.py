import unittest.mock
import documents
from documents import get_name, get_shelf, get_add_doc, get_list, get_move, get_as


def test_get_shelf(doc_number1, doc_number2):
    assert get_shelf(doc_number1)
    assert not get_shelf(doc_number2)


def test_get_name(doc_number, name):
    with unittest.mock.patch('builtins.input', return_value=doc_number):
        assert get_name() == name


def test_get_list(doc_number):
    get_list(doc_number)
    test = True
    for directory_docs_list in documents.directories.values():
        if doc_number in directory_docs_list:
            test = False
    assert test


def test_get_add_doc(shelf_number):
    with unittest.mock.patch('builtins.input', return_value=shelf_number):
        get_add_doc()
        assert shelf_number in documents.directories.keys()


def test_get_as(doc_number, shelf_number):
    get_as(doc_number, shelf_number)
    assert doc_number in documents.directories[shelf_number]


def test_get_move(user_doc_number):
    with unittest.mock.patch('builtins.input', return_value=user_doc_number):
        shelf_number = get_move()
        assert user_doc_number in documents.directories[shelf_number]


def test_get_as(new_doc_number, new_doc_type, new_doc_owner_name,
                new_doc_shelf_number):
    get_as(new_doc_number, new_doc_type, new_doc_owner_name,
           new_doc_shelf_number)
    new_doc = {
        "type": new_doc_type,
        "number": new_doc_number,
        "name": new_doc_owner_name
    }
    assert new_doc in documents.documents
    assert new_doc_number in documents.directories[new_doc_shelf_number]
