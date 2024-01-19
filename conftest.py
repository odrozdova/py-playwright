import pytest
from dotenv import load_dotenv

import yaml

load_dotenv()


@pytest.fixture(scope='session')
def get_urls():
    with open(f'./yaml/urls.yaml') as file_read:
        file = yaml.load(file_read, Loader=yaml.FullLoader)
    return file
