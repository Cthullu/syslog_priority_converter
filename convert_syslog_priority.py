#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check systemd services and timers.
"""

__author__: str = "Daniel Kuß"
__version__: str = "1.0.0"
__src__: str = "https://github.com/Cthullu/syslog_priority_converter"
__status__: str = "Production"

import logging
import sys
import argparse
import constant as const

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


def extract_values(priority: int, logger: logging = None) -> dict:
    """
    Extract the facility and severity value from a provided priority.
    Also adds the facility and severity name.

    :return: dict
    """
    ret_val = {}

    logger.debug("Perform integer division for '%s'.", priority)
    ret_val["facility_value"] = priority // const.PRIORITY_CONVERSION_FACTOR

    logger.debug("Get facility keyword for value '%s'.",ret_val["facility_value"])
    ret_val["failicty_keyword"] = const.FACILITY_KEYWORDS[ret_val["facility_value"]]

    logger.debug("Get severity level from provided priority '%s'.", priority)
    ret_val["severity_value"] = priority - (ret_val["facility_value"]
                                            * const.PRIORITY_CONVERSION_FACTOR)

    logger.debug("Get severity keyword for value '%s'.",ret_val["severity_value"])
    ret_val["severity_keyword"] = const.SEVERITY_KEYWORDS[ret_val["severity_value"]]

    return ret_val


def main() -> int:
    """
    Main function.

    :return: int
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname) -8s] (%(filename)s:%(lineno)d) %(message)s",
    )
    logger = logging.getLogger(__name__)

    logger.debug("PArsing command line arguments.")
    cli_args = get_parser(__version__).parse_args()

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
    extracted_values = extract_values(cli_args.priority, logger)

    print(f"Facility: {extracted_values['facility_value']} "
          f"({extracted_values['failicty_keyword']})")
    print(f"Severity: {extracted_values['severity_value']} "
          f"({extracted_values['severity_keyword']})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
