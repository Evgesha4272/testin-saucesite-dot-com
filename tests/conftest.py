import pytest


@pytest.fixture()
def set_up():
    print('\nStart test')
    yield
    print('\nEnd test')


