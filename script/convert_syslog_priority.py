#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert given syslog priority value into facility and severity values.
"""

__author__: str = "Daniel Kuß"
__version__: str = "1.1.0"
__src__: str = "https://github.com/Cthullu/syslog_priority_converter"
__status__: str = "Production"


import logging
import argparse

from sys import exit as sys_exit
from typing import Optional

import syslog_converter


def get_parser() -> argparse.ArgumentParser:
    """
    Returns an ArgumentParser for the convert_syslog_priority.py script.

    Args:
        None

    Returns:
        argparse.ArgumentParser: Configured argument parser.
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
        version = f'%(prog)s {__version__}'
    )

    parser.add_argument(
        dest = "priority",
        type = int,
        metavar = "<priority>",
        help = "Priority to convert into facility and severity level.",
    )

    return parser.parse_args()


def extract_values(priority: int, logger: Optional[logging.Logger] = None) -> dict:
    """
    Extract the facility and severity value from a provided priority.
    Also adds the facility and severity name.

    Args:
        priority (int): Syslog priority value.
        logger (Optional[logging.Logger]): Logger instance for logging debug messages.

    Returns:
        dict: Dictionary containing facility value, facility keyword, severity value,
            and severity keyword.
    """
    ret_val = {}

    logger.debug("Get facility value from provided priority '%s'.", priority)
    try:
        ret_val["facility_value"] = syslog_converter.get_facility_value(priority)
    except TypeError as exc:
        logger.error("Invalid type for priority value: %s", exc)
        raise TypeError("Priority must be an integer.") from exc
    except ValueError as exc:
        logger.error("Invalid priority value: %s", exc)
        raise ValueError("Priority must be between 0 and 191 inclusive.") from exc

    logger.debug("Get facility keyword for value '%s'.",ret_val["facility_value"])
    try:
        ret_val["failicty_keyword"] = syslog_converter.get_facility_keyword(
            ret_val["facility_value"]
        )
    except KeyError as exc:
        logger.error("Invalid facility value: %s", exc)
        raise KeyError("Facility must be between 0 and 23 inclusive.") from exc
    except TypeError as exc:
        logger.error("Invalid type for facility value: %s", exc)
        raise TypeError("Facility must be an integer.") from exc

    logger.debug("Get severity level from provided priority '%s'.", priority)
    try:
        ret_val["severity_value"] = syslog_converter.get_severity_value(priority)
    except TypeError as exc:
        logger.error("Invalid type for priority value: %s", exc)
        raise TypeError("Priority must be an integer.") from exc

    try:
        ret_val["severity_value"] = syslog_converter.get_severity_value(priority)
    except ValueError as exc:
        logger.error("Invalid priority value: %s", exc)
        raise ValueError("Priority must be between 0 and 191 inclusive.") from exc
    except TypeError as exc:
        logger.error("Invalid type for priority value: %s", exc)
        raise TypeError("Priority must be an integer.") from exc

    logger.debug("Get severity keyword for value '%s'.",ret_val["severity_value"])
    try:
        ret_val["severity_keyword"] = syslog_converter.get_severity_keyword(
            ret_val["severity_value"]
        )
    except KeyError as exc:
        logger.error("Invalid severity value: %s", exc)
        raise KeyError("Severity must be between 0 and 7 inclusive.") from exc
    except TypeError as exc:
        logger.error("Invalid type for severity value: %s", exc)
        raise TypeError("Severity must be an integer.") from exc

    return ret_val


def main() -> int:
    """
    Main function.

    Args:
        None

    Returns:
        int: Exit code, 0 on success, 1 on error.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname) -8s] (%(filename)s:%(lineno)d) %(message)s",
    )
    logger = logging.getLogger(__name__)

    logger.debug("PArsing command line arguments.")
    cli_args = get_parser()

    if cli_args.debug:
        logger.setLevel(level=logging.DEBUG)
        logger.debug("Debug logging enabled.")
    else:
        logging.basicConfig(level=logging.INFO)

    logger.debug("Check if provided priority value '%s' is valid.", cli_args.priority)
    if cli_args.priority < 0 or cli_args.priority > 191:
        print(f"Value '{cli_args.priority}' is not a valid priority.")
        return 1

    logger.debug("Call subfunction to extract values from priority.")
    try:
        extracted_values = extract_values(cli_args.priority, logger)
    except (TypeError, ValueError, KeyError) as exc:
        logger.error("Error extracting values: %s", exc)
        print(f"Error: {exc}")
        return 1

    print(f"Facility: {extracted_values['facility_value']} "
          f"({extracted_values['failicty_keyword']})")
    print(f"Severity: {extracted_values['severity_value']} "
          f"({extracted_values['severity_keyword']})")

    return 0


if __name__ == "__main__":
    sys_exit(main())
