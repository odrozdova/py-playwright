import pytest


import yaml


@pytest.fixture(scope='session')
def get_urls():
    with (open(f'./yaml/urls.yaml') as file_read):
        file = yaml.load(file_read, Loader=yaml.FullLoader)
    return file
