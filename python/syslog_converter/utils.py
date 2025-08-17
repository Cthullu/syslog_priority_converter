#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Various utility functions
"""

import argparse
import logging


LOGLEVELS = {
    "CRITICAL": logging.CRITICAL,
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "NOTSET": logging.NOTSET,
}


def get_cli_args(version: str) -> argparse.Namespace:
    """
    Returns an ArgumentParser for the convert_syslog_priority.py script.

    Args:
        version:

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        prog="convert_syslog_priority",
        description="Convert syslog priority value to facility and severity level.",
    )

    parser.add_argument(
        "-l",
        "--loglevel",
        choices=LOGLEVELS,
        default="WARNING",
        dest="loglevel",
        help="Select logging level.",
        metavar="<loglevel>",
        required=False,
        type=str.upper,
    )

    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {version}"
    )

    parser.add_argument(
        dest="priority",
        type=int,
        metavar="<priority>",
        help="Priority to convert into facility and severity level.",
    )

    return parser.parse_args()


def setup_logger(loglevel: str = "WARNING") -> logging.Logger:
    """
    Set up the logging configuration for the script.

    Args:
        loglevel (str): The logging level to set. Defaults to WARNING.

    Returns:
        logging.Logger: Configured logger instance.

    Raises:
        TypeError: If loglevel is not a string.
        ValueError: If loglevel is not a valid logging level.
    """
    if not isinstance(loglevel, str):
        raise TypeError("loglevel must be a string")

    if loglevel not in LOGLEVELS:
        raise ValueError(f"Invalid loglevel: {loglevel}")

    logger = logging.getLogger()
    logger.setLevel(LOGLEVELS[loglevel])

    # Create a console handler with the specified log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOGLEVELS[loglevel])
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname) -8s - %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
