#!/usr/bin/env python3
""" I hate regular expresions """

import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """ Return a log message obfuscated """
    for item in fields:
        message = re.sub(
            fr"{item}=.+?{separator}",
            f"{item}={redaction}{separator}",
            message)

    return message
