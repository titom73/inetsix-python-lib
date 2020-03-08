import shutil
from setuptools import setup
from inetsix import __version__, __author__, __license__, __email__

# Load list of requirements from req file
with open('requirements.txt') as f:
    REQUIRED_PACKAGES = f.read().splitlines()

# Load description from README file
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

# Rename Scripts to sync with original name
shutil.copyfile('bin/excel-to-json.py', 'bin/excel-to-json')

# Script version
VERSION = str(__version__)
AUTHOR = str(__author__)
AUTHOR_EMAIL = str(__email__)
LICENSE = str(__license__)

setup(
    name="inetsix",
    version=VERSION,
    scripts=["bin/excel-to-json.py"],
    packages=['inetsix'],
    python_requires=">=3.5",
    install_requires=REQUIRED_PACKAGES,
    url="https://github.com/titom73/inetsix-python-lib",
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="Tools & Python function from inetsix.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Telecommunications Industry',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: System :: Networking'
    ]
)
