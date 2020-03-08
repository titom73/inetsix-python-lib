import urllib3
import shutil
import os.path
import logging


def download_http(remote_file, local_file=None):
    """
    Function to download file over HTTP/HTTPS.

    Parameters
    ----------
    remote_file : string
        URL to download file.
    local_file : string, optional
        Local Filename to save file, default is None

    Returns
    -------
    string
        Name of downloaded file.
    """
    logger = logging.getLogger('inetsix.tools.download_http')
    logger.info('Download initiated')
    url = remote_file
    file_name = url.split('/')[-1]
    if local_file is not None:
        file_name = local_file
    http = urllib3.PoolManager()
    try:
        r = http.request('GET', url, preload_content=False)
        if r.status == 404:
            return None
    except (KeyError, urllib3.exceptions.HTTPError) as details:
        print("HTTP Error:" + str(details))
        return None
    with open(file_name, 'wb') as out_file:
        shutil.copyfileobj(r, out_file)
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
