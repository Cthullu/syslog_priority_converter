#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert given syslog priority value into facility and severity values.
"""

PRIORITY_CONVERSION_FACTOR = 8

FACILITY_KEYWORDS = {
    0: "Kernel messages",
    1: "User-level messages",
    2: "Mail system",
    3: "System daemons",
    4: "Security/authorization messages",
    5: "Messages generated internally by syslogd",
    6: "Line printer subsystem",
    7: "Network news subsystem",
    8: "UUCP subsystem",
    9: "Clock daemon",
    10: "Security/authorization messages",
    11: "FTP daemon",
    12: "NTP subsystem",
    13: "Log audit",
    14: "Log alert",
    15: "Clock daemon (note 2)",
    16: "Local use 0 (local0)",
    17: "Local use 1 (local1)",
    18: "Local use 2 (local2)",
    19: "Local use 3 (local3)",
    20: "Local use 4 (local4)",
    21: "Local use 5 (local5)",
    22: "Local use 6 (local6)",
    23: "Local use 7 (local7)",
}

SEVERITY_KEYWORDS = {
    0: "emerg",
    1: "alert",
    2: "crit",
    3: "err",
    4: "warning",
    5: "notice",
    6: "info",
    7: "debug",
}
