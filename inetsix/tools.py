import urllib
import os.path
import logging


def download_http(remote_file):
    """
    Function to download file over HTTP/HTTPS.

    Parameters
    ----------
    remote_file : string
        URL to download file.

    Returns
    -------
    string
        Name of downloaded file.
    """
    logger = logging.getLogger('inetsix.tools.download_http')
    logger.info('Download initiated')
    url = remote_file
    file_name = url.split('/')[-1]
    u = urllib.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    logger.debug(" * Downloading: %s Bytes: %s", str(file_name), str(file_size))
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        logger.debug("    > %s", str(status))
    f.close()
    return file_name


def load_constant(key_name, default='UNSET'):
    """Set up constant value from OS Environment.

    Help to define CONSTANT from OS Environment.
    If it is not defined, then, fallback to default value
    provided within parameters

    Example
    -------
    >>> USERNAME = load_constant(key_name='USERNAME_1', default='myUser')
    >>> print USERNAME
    >>> myUsername

    Parameters
    ----------
    key_name : string
        VAR to lookup in os.environment
    default : str, optional
        Default value to use if key_name is not defined. By default set to UNSET
    verbose : bool, optional
        Boolean to activate verbos mode

    Returns
    -------
    str
        Value to use to configure variable
    """
    logger = logging.getLogger('inetsix.tools.load_constant')
    logger.info('Load constant: %s', str(key_name))

    if key_name in os.environ:
        logger.debug("%s is set to %s", key_name, os.environ.get(key_name))
        return os.environ[key_name]
    else:
        logger.debug('%s is not set - using default (%s)', key_name, str(default))   # noqa E501
    return default

