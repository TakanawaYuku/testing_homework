import imp
import unittest
from urllib import response
import requests
from yandex import create_folder
from Token import token
import json
import time
import random


class TestSomething(unittest.TestCase):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'OAuth {token}'
    }

    def test_status_code(self):
        create_folder('Test_Yandex_Folder')
        response = requests.get(f'{self.URL}?path=Test_Yandex_Folder',
                                headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['_embedded']['path'],
                         'disk:/Test_Yandex_Folder')

    def test_status_code_false(self):
        create_folder('Test_Yandex_Folder')
        response = requests.get(
            f'{self.URL}?path=path_false_{str(random.randint(1, 999))}',
            headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Не удалось найти')
