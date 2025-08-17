#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the converter class
"""

import unittest

from os import path as os_path
from sys import path as sys_path
from sys import argv as sys_argv

dir_name = os_path.dirname(sys_argv[0])
file_path = os_path.abspath(dir_name)
sys_path.append(f"{file_path}/../")

try:
    from syslog_converter.converter import Converter
except ImportError as exc:
    raise ImportError(
        "The syslog_converter package is required for these tests."
    ) from exc


class ConverterTests(unittest.TestCase):
    """
    Tests for the Converter class.
    """

    def setUp(self) -> None:
        """
        Set up a new Converter instance for testing.
        """
        self.converter = Converter()
        self.empty_converter = Converter()

        # We have 24 facility levels (0-23).
        # We need to map the priority levels (0-191) to the facility levels (0-23).
        # Add the first and last priority for each facility level to check list.
        self.facilities_test_values = {
            0: 0,
            7: 0,
            8: 1,
            15: 1,
            16: 2,
            23: 2,
            24: 3,
            31: 3,
            32: 4,
            39: 4,
            40: 5,
            47: 5,
            48: 6,
            55: 6,
            56: 7,
            63: 7,
            64: 8,
            71: 8,
            72: 9,
            79: 9,
            80: 10,
            87: 10,
            88: 11,
            95: 11,
            96: 12,
            103: 12,
            104: 13,
            111: 13,
            112: 14,
            119: 14,
            120: 15,
            127: 15,
            128: 16,
            135: 16,
            136: 17,
            143: 17,
            144: 18,
            151: 18,
            152: 19,
            159: 19,
            160: 20,
            167: 20,
            168: 21,
            175: 21,
            176: 22,
            183: 22,
            184: 23,
            191: 23,
        }

        # We have 8 severity levels (0-7).
        # We need to map the priority levels (0-191) to the severity levels (0-7).
        # Check the first and last 7 priorities.

        self.severities_test_values = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 0,
            15: 7,
            16: 0,
            23: 7,
            24: 0,
            31: 7,
            32: 0,
            39: 7,
            40: 0,
            47: 7,
            48: 0,
            55: 7,
            56: 0,
            63: 7,
            64: 0,
            71: 7,
            72: 0,
            79: 7,
            80: 0,
            87: 7,
            88: 0,
            95: 7,
            96: 0,
            103: 7,
            104: 0,
            111: 7,
            112: 0,
            119: 7,
            120: 0,
            127: 7,
            128: 0,
            135: 7,
            136: 0,
            143: 7,
            144: 0,
            151: 7,
            152: 0,
            159: 7,
            160: 0,
            167: 7,
            168: 0,
            175: 7,
            176: 0,
            183: 7,
            184: 0,
            191: 7,
        }

        self.facilities_keywords = {
            0: "Kernel messages",
            8: "User-level messages",
            16: "Mail system",
            24: "System daemons",
            32: "Security/authorization messages",
            40: "Messages generated internally by syslogd",
            48: "Line printer subsystem",
            56: "Network news subsystem",
            64: "UUCP subsystem",
            72: "Clock daemon",
            80: "Security/authorization messages",
            88: "FTP daemon",
            96: "NTP subsystem",
            104: "Log audit",
            112: "Log alert",
            120: "Clock daemon (note 2)",
            128: "Local use 0 (local0)",
            136: "Local use 1 (local1)",
            144: "Local use 2 (local2)",
            152: "Local use 3 (local3)",
            160: "Local use 4 (local4)",
            168: "Local use 5 (local5)",
            176: "Local use 6 (local6)",
            184: "Local use 7 (local7)",
        }

        self.severity_keywords = {
            0: "emerg",
            1: "alert",
            2: "crit",
            3: "err",
            4: "warning",
            5: "notice",
            6: "info",
            7: "debug",
        }

    def test_converter_initialization(self):
        """
        Test the initialization of the Converter class.
        """
        self.assertIsInstance(self.converter, Converter)
        self.assertIsInstance(self.empty_converter, Converter)

        # Check if the initial values are set to None
        self.assertEqual(self.converter._priority, None)
        self.assertEqual(self.converter._facility, None)
        self.assertEqual(self.converter._severity, None)

    def test_priority_setter(self):
        """
        Test the priority setter of the Converter class.
        """
        self.converter.priority = 13
        self.assertEqual(self.converter.priority, 13)

        # Re-setting the value should be able without an error
        self.converter.priority = 14
        self.assertEqual(self.converter.priority, 14)

        # Test if setting the min and max allowed values works
        self.converter.priority = 0
        self.assertEqual(self.converter.priority, 0)

        self.converter.priority = 191
        self.assertEqual(self.converter.priority, 191)

        # Setting a value outside the boundries should raise an `ValueError`
        with self.assertRaises(ValueError):
            self.converter.priority = -1
            self.converter.priority = 192

        # Setting a None integer should raise a `TypeError`
        with self.assertRaises(TypeError):
            self.converter.priority = None
            self.converter.priority = "string"
            self.converter.priority = 3.14

    def test_priority_getter(self):
        """
        Test the priority getter of the Converter class.
        """
        self.converter.priority = 13
        self.assertEqual(self.converter.priority, 13)

        # Test if are getting a `None` value priority for an instance without set priority
        self.assertEqual(self.empty_converter.priority, None)

    def test_facility_getter(self):
        """
        Test the facility getter of the Converter class.
        """
        # Check that we get an `TypeError` for an instance without set priority
        with self.assertRaises(TypeError):
            _test = self.empty_converter.facility

        for priority, facility in self.facilities_test_values.items():
            self.converter.priority = priority
            self.assertEqual(self.converter.facility, facility)

    def test_facility_keywords(self):
        """
        Test if we get the correct facility keywords.
        """
        for priority, facility in self.facilities_keywords.items():
            self.converter.priority = priority
            self.assertEqual(self.converter.facility_level, facility)

    def test_severity_getter(self):
        """
        Test the severity getter of the Converter class.
        """
        # Check if we get an `TypeError` for an instance without set priority
        with self.assertRaises(TypeError):
            _test = self.empty_converter.severity

        for priority, severity in self.severities_test_values.items():
            self.converter.priority = priority
            self.assertEqual(self.converter.severity, severity)

    def test_severity_keywords(self):
        """
        Test if we get the correct severity keywords.
        """
        for priority, severity in self.severity_keywords.items():
            self.converter.priority = priority
            self.assertEqual(self.converter.severity_level, severity)


if __name__ == "__main__":
    # Perform tests if called directly
    unittest.main()
