#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Argument parsers for the convert_syslog_priority script.
"""

import argparse

def get_parser(version: str) -> argparse.ArgumentParser:
    """
    Returns an ArgumentParser for the check_systemd.py script.

    :return: ArgumentParser
    """
    parser = argparse.ArgumentParser(
        prog = "convert_syslog_priority",
        description="Convert syslog priority value to facility and severity level.",
    )

    parser.add_argument(
        "-d", "--debug",
        dest = "debug",
        help = "turn on debug logging",
        action = "store_true",
        default = False,
    )

    parser.add_argument(
        "-v", "--version",
        action = "version",
        version = f'%(prog)s {version}'
    )

    parser.add_argument(
        dest = "priority",
        type = int,
        metavar = "<priority>",
        help = "Priority to convert into facility and severity level.",
    )

    return parser
