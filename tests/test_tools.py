import pytest
import inetsix.tools

URL_OK = 'https://raw.githubusercontent.com/titom73/inetsix-python-lib/master/tests/Book1.xlsx'
URL_404 = 'https://github.com/titom73/inetsix-python-lib/blob/master/tests/Book2.xlsx'
FILENAME_DL = 'downloaded-file.xlsx'
FILENAME_SRC = 'Book1.xlsx'

def test_download_http_valide():
    print('* Use case: DL file with no rename')
    function_result =  inetsix.tools.download_http(remote_file=URL_OK)
    assert function_result == FILENAME_SRC,\
          'Filename returned is not correct: '+str(function_result)
    print('* Use case: DL file with rename')
    function_result =  inetsix.tools.download_http(remote_file=URL_OK, local_file=FILENAME_DL)
    assert function_result == FILENAME_DL,\
          'Filename returned is not correct: '+str(function_result)

def test_download_http_404():
    print('* Use case: DL file with 404 error')
    function_result =  inetsix.tools.download_http(remote_file=URL_404)
    assert function_result is None,\
           'Filename returned is not correct: '+str(function_result)
