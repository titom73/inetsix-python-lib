import pytest
import inetsix.tools

URL_OK = 'https://github.com/titom73/inetsix-python-lib/blob/master/tests/Book1.xlsx'
URL_404 = 'https://github.com/titom73/inetsix-python-lib/blob/master/tests/Book2.xlsx'


def test_download_http_valide():
    function_result =  inetsix.tools.download_http(remote_file=URL_OK)
    assert function_result == 'Book1.xlsx', 'Filename returned is not correct: '+str(function_result)

def test_download_http_404d():
    function_result =  inetsix.tools.download_http(remote_file=URL_404)
    assert function_result is None, 'Filename returned is not correct: '+str(function_result)
