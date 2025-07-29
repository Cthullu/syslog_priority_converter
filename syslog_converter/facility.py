#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Perform operations related to syslog facilities.
"""

from syslog_converter import PRIORITY_CONVERSION_FACTOR
from syslog_converter import FACILITY_KEYWORDS


def get_facility_value(priority: int) -> int:
    """
    Get the facility value from a provided priority.

    Args:
        priority (int): Syslog priority value.

    Returns:
        int: Facility value derived from the priority.

    Raises:
        TypeError: If the priority is not an integer.
        ValueError: If the priority is not between 0 and 191 inclusive.
    """
    if not isinstance(priority, int):
        raise TypeError("Priority must be an integer.")

    if priority < 0 or priority > 191:
        raise ValueError("Priority must be between 0 and 191 inclusive.")

    return priority // PRIORITY_CONVERSION_FACTOR


def get_facility_keyword(facility: int) -> str:
    """
    Get the facility keyword from a provided facility value.

    Args:
        facility (int): Facility value.

    Returns:
        str: Facility keyword corresponding to the facility value.

    Raises:
        KeyError: If the facility value is not recognized.
        TypeError: If the facility is not an integer.
    """
    if not isinstance(facility, int):
        raise TypeError("Facility must be an integer.")

    try:
        return FACILITY_KEYWORDS[facility]
    except KeyError:
        raise KeyError("Facility must be between 0 and 23 inclusive.")
