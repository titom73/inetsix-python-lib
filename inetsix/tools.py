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
    url = remote_file
    file_name = url.split('/')[-1]
    u = urllib.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    logging.debug(" * Downloading: %s Bytes: %s", str(file_name), str(file_size))
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
        logging.debug("    > %s", str(status))
    f.close()
    return file_name