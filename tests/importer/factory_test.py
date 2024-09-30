from os import path
import pytest
from qualitag.src.importer import import_data
from qualitag.src.questions import Answer


@pytest.fixture
def mocks_path():
    return path.join(path.dirname(__file__), "mocks")


def test_import_txt_data(mocks_path):
    file = path.join(mocks_path, "test.txt")
    assert isinstance(import_data(file), Answer)


def test_import_pdf_data(mocks_path):
    file = path.join(mocks_path, "test.pdf")
    assert isinstance(import_data(file), Answer)


def test_import_error(mocks_path):
    file = path.join(mocks_path, "test.xxx")
    with pytest.raises(ValueError):
        import_data(file)
