#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert given syslog priority value into facility and severity values.
"""

__author__: str = "Daniel Kuß"
__version__: str = "1.2.0"
__src__: str = "https://github.com/Cthullu/syslog_priority_converter"
__status__: str = "Production"


# Standard imports
from sys import exit as sys_exit

# Local imports
from syslog_converter.converter import Converter
from syslog_converter import utils


def main() -> int:
    """
    Main function.

    Args:
        None

    Returns:
        int: Exit code, 0 on success, 1 on error.
    """
    logger = utils.setup_logger("INFO")

    logger.info("Starting syslog priority conversion script.")

    cli_args = utils.get_cli_args(__version__)
    if cli_args.loglevel != "INFO":
        logger = utils.setup_logger(cli_args.loglevel)

    logger.debug("Creating converter instance with priority '%d'.", cli_args.priority)
    try:
        priority_converter = Converter(cli_args.priority)
    except ValueError as e:
        logger.error(
            "Received value error while creating converter object with priority '%d': %s",
            cli_args.priority, e
        )
        return 1

    logger.debug("Getting facility and severity values from converter object.")
    facility = priority_converter.facility
    facility_level = priority_converter.facility_level
    severity = priority_converter.severity
    severity_level = priority_converter.severity_level

    logger.debug("Printing values.")
    print(f"Syslog severity: {severity} {severity_level}")
    print(f"Syslog facility: {facility} {facility_level}")

    logger.info("Syslog priority conversion completed successfully.")
    logger.debug("Exiting with code 0.")
    return 0


if __name__ == "__main__":
    sys_exit(main())
