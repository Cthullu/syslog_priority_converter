#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the converter class
"""

from contextlib import AbstractContextManager
from typing import Any
import unittest

from os import path as os_path
from sys import path as sys_path
from sys import argv as sys_argv

dir_name = os_path.dirname(sys_argv[0])
file_path = os_path.abspath(dir_name)
sys_path.append(f"{file_path}/../")

try:
    from syslog_converter.utils import setup_logger
except ImportError:
    raise ImportError("The syslog_converter package is required for these tests.")


class TestSetupLogger(unittest.TestCase):

    def test_setup_logger_default(self):
        """
        Test setup_logger with default log level.
        """
        logger = setup_logger()
        self.assertEqual(logger.level, 30)  # WARNING level

    def test_setup_logger_custom_level(self):
        """
        Test setup_logger with a custom log level.
        """
        logger = setup_logger("NOTSET")
        self.assertEqual(logger.level, 0)  # NOTSET level

        logger = setup_logger("DEBUG")
        self.assertEqual(logger.level, 10)  # DEBUG level

        logger = setup_logger("INFO")
        self.assertEqual(logger.level, 20)  # INFO level

        logger = setup_logger("WARNING")
        self.assertEqual(logger.level, 30)  # WARNING level

        logger = setup_logger("ERROR")
        self.assertEqual(logger.level, 40)  # ERROR level

        logger = setup_logger("CRITICAL")
        self.assertEqual(logger.level, 50)  # CRITICAL level

    def test_setup_logger_invalid_level(self):
        """
        Test setup_logger with an invalid log level.
        """
        with self.assertRaises(ValueError):
            setup_logger("INVALID")

    def test_setup_logger_type_error(self):
        """
        Test setup_logger with a non-string log level.
        """
        with self.assertRaises(TypeError):
            setup_logger(123)
            setup_logger(None)


if __name__ == "__main__":
    # Perform tests if called directly
    unittest.main()
