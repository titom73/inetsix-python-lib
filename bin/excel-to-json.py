#!/usr/bin/env python
# coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
from inetsix.serializer import ExcelSerializer
import pprint
import argparse
import json
import sys

if __name__ == "__main__":

    # Options management
    parser = argparse.ArgumentParser(description="Excel to JSON serializer")
    parser.add_argument('-e', '--excel', help='Input Excel file',default=None)
    parser.add_argument('-s', '--sheet', help='Excel sheet to serialize',default=None)
    options = parser.parse_args()

    # Check section
    if options.excel is None:
        sys.exit("Excel file is missing please provide it with option -e")

    # Load Excel workbook
    serializer = ExcelSerializer(excel_path=options.excel)
    json_result = None
    if options.sheet is not None:
        # Serialize given sheet.
        json_result = serializer.serialize_table(sheet=options.sheet)
    else:
        # If no sheet provided, we do on all workbook.
        json_result = serializer.serialize_book()
    
    # Work on display action
    result_display = json.dumps(json_result, sort_keys=True, indent=4, separators=(',', ': '))
    print(result_display)