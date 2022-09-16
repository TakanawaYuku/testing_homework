import unittest.mock
import documents
from documents import get_delete


def test_get_delete(doc_number):
    with unittest.mock.patch('builtins.input', return_value=doc_number):
        get_delete()
        test = True
        for document in documents.documents:
            if document['number'] == doc_number:
                test = False
        for numbers in documents.directories.values():
            if doc_number in numbers:
                test = False
        assert test
