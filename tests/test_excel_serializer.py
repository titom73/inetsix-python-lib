from inetsix.serializer import ExcelSerializer
import pytest
import os.path
import types
import openpyxl


XLSX_FILE = 'tests/Book1.xlsx'


@pytest.fixture
def get_xlsx_file(file=XLSX_FILE):
    """
    Build file path based on where we are.

    Parameters
    ----------
    file : string , optional
        Path to file to load, by default XLSX_FILE

    Returns
    -------
    [type]
        [description]
    """    
    # Check if we can access file from root of the repository
    if os.path.exists(XLSX_FILE):
        return XLSX_FILE
    # Check if file exist in same folder
    elif os.path.exists(XLSX_FILE.split('/')[-1]):
        return XLSX_FILE.split('/')[-1]
    # Default return None and should stop testing.
    else:
        return None


def test_wrong_xlsx_to_json(get_xlsx_file='UNKNOWN'):
    """
    Test inetsix.serializer.ExcelSerializer is raising exception.

    A wrong file is used to raise openpyxl.utils.exceptions.InvalidFileException

    Parameters
    ----------
    get_xlsx_file : str, optional
        Incorrect Filename, by default 'UNKNOWN'
    """    
    with pytest.raises(openpyxl.utils.exceptions.InvalidFileException):
        xlsx_json = ExcelSerializer(excel_path=get_xlsx_file).serialize_book()


def test_complete_xlsx_to_json(get_xlsx_file):
    """
    Test output is coherent for a full file to JSON.

    Parameters
    ----------
    get_xlsx_file : string
        Correct file path to load XLSX content
    """    
    xlsx_json = ExcelSerializer(excel_path=get_xlsx_file).serialize_book()
    # Test instance type
    assert isinstance(xlsx_json, dict), 'Data is not a dict as expected'
    # Test content of the structure.
    assert 'Sheet1' in xlsx_json, 'JSON does not contain expected Sheet name'


def test_sheet_xlsx_to_json(get_xlsx_file, sheet_name='Sheet1'):
    """
    Test output is coherent for a a single Sheet of a book to JSON.

    Parameters
    ----------
    get_xlsx_file : string
        Correct file path to load XLSX content
    sheet_name: string , optional
        Sheet name to convert, by default 'Sheet1'
    """    
    xlsx_json = ExcelSerializer(excel_path=get_xlsx_file).serialize_table(sheet=sheet_name)
    # Test instance type
    assert isinstance(xlsx_json, list), 'Data is not a list as expected'
    # Test content of the structure.
    assert len(xlsx_json)>1, 'JSON does not contain enough entries'

