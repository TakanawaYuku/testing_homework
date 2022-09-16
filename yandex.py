from Token import token
import requests


def create_folder(folder):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    requests.put(f'{URL}?path={folder}', headers=headers)


if __name__ == '__main__':
    create_folder('Test_Yandex_Folder')
