#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Perform operations related to syslog facilities.
"""

from syslog_converter import PRIORITY_CONVERSION_FACTOR
from syslog_converter import SEVERITY_KEYWORDS


def get_severity_value(priority: int) -> int:
    """
    Get the severity value from a provided priority.

    Args:
        priority (int): Syslog priority value.

    Returns:
        int: Severity value derived from the priority.

    Raises:
        TypeError: If the priority is not an integer.
        ValueError: If the priority is not between 0 and 191 inclusive.
    """
    if not isinstance(priority, int):
        raise TypeError("Priority must be an integer.")

    if priority < 0 or priority > 191:
        raise ValueError("Priority must be between 0 and 191 inclusive.")

    return priority % PRIORITY_CONVERSION_FACTOR


def get_severity_keyword(severity: int) -> str:
    """
    Get the severity keyword from a provided severity value.

    Args:
        severity (int): Severity value.

    Returns:
        str: Severity keyword corresponding to the severity value.

    Raises:
        KeyError: If the severity value is not recognized.
        TypeError: If the severity is not an integer.
    """
    if not isinstance(severity, int):
        raise TypeError("Severity must be an integer.")

    try:
        return SEVERITY_KEYWORDS[severity]
    except KeyError as exc:
        raise KeyError("Severity must be between 0 and 7 inclusive.") from exc
