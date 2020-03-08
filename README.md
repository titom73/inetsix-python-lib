# Inetsix Python toolbox

## Overview

This module provides some generic python functions usually used in many of scripts. Instead of rewriting these functions in all scripts, we have put them in a single module.

## Content

### Scripts

Repository provides following scripts:

- Excel to Json converter: [`excel-to-json.py`](bin/excel-to-json.py)

```shell
$ excel-to-json.py -e tests/Book1.xlsx -s Sheet1
[
    {
        "description": "ifd1",
        "interface": "ethernet1",
        "state": "up"
    },
    {
        "description": "ifd2",
        "interface": "ethernet2",
        "state": "down"
    }
]
```


### Functions & Classes

Current Functions and classes:

- [`ExcelSerializer`](inetsix/serializer.py) from `inetsix.serializer`: Class to serialize excel spreadsheet into Python structure to be consume in scripts or templates
- From `inetsix.tools`:
    - Download file with HTTP/HTTPS transport (`inetsix.tools.download_http`)
    - Load Environnment constant with `inetsix.tools.load_constant`

## Installation

```shell
# From github
$ pip install git+https://github.com/titom73/inetsix-python-lib.git

# From pypi servers
$ pip install inetsix
```