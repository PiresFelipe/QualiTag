from os import path
import pytest
from qualitag.src.importer import PDFImporter
from qualitag.src.questions import Answer


@pytest.fixture
def mocks_path():
    return path.join(path.dirname(__file__), "mocks")


def test_pdf_importer_initialization():
    filepath = "document.pdf"
    importer = PDFImporter(filepath)

    # Check that the filepath is correctly set
    assert importer.filepath == filepath


def test_pdf_importer_import_data(mocks_path):
    file_content = "This is a test PDF file. \n "
    file_path = path.join(mocks_path, "test.pdf")

    importer = PDFImporter(file_path)

    # Call the import_data method
    result = importer.import_data()

    assert isinstance(result, Answer)
    assert result.text == file_content


def test_pdf_importer_file_not_found():
    # Use a non-existent file path
    filepath = ".pdf"
    importer = PDFImporter(filepath)

    # Verify that FileNotFoundError is raised when calling import_data
    with pytest.raises(FileNotFoundError):
        importer.import_data()
