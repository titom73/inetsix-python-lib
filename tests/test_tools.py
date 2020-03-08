import inetsix.tools
import os.path

URL_OK = 'https://raw.githubusercontent.com/titom73/inetsix-python-lib/master/tests/Book1.xlsx'
URL_404 = 'https://github.com/titom73/inetsix-python-lib/blob/master/tests/Book2.xlsx'
FILENAME_DL = 'downloaded-file.xlsx'
FILENAME_SRC = 'Book1.xlsx'


def test_download_http_valide(url=URL_OK,
                              local_filename=FILENAME_DL,
                              filename_src=FILENAME_SRC):
    """
    Test Behavior with existing file

    Parameters
    ----------
    url : string, optional
        URL to download file, by default URL_OK
    local_filename : string, optional
        Filename used locally in rename test, by default FILENAME_SRC
    filename_src : string, optional
        Filename downloaded with URL, by default FILENAME_DL
    """
    print('* Use case: DL file with no rename')
    function_result = inetsix.tools.download_http(remote_file=url)
    assert function_result == filename_src,\
        'Filename returned is not correct: '+str(function_result)
    assert os.path.isfile(function_result) is True,\
        'File not found locally. Seems file '+str(function_result)+' has not been downloaded'

    print('* Use case: DL file with rename')
    function_result = inetsix.tools.download_http(remote_file=url,
                                                  local_file=local_filename)
    assert function_result == FILENAME_DL,\
        'Filename returned is not correct: '+str(function_result)
    assert os.path.isfile(function_result) is True,\
        'File not found locally. Seems file '+str(function_result)+' has not been downloaded'


def test_download_http_404(url=URL_404):
    """
    Test Behavior with 404 error code.
    """
    print('* Use case: DL file with 404 error')
    function_result = inetsix.tools.download_http(remote_file=url)
    assert function_result is None,\
        'Filename returned is not correct: '+str(function_result)
