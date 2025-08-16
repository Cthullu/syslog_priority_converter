#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Perform unittests related to syslog severities.
"""

import unittest

from syslog_converter.severity import get_severity_value
from syslog_converter.severity import get_severity_keyword


class SeverityTests(unittest.TestCase):
    """
    Tests for syslog severity operations.
    """

    def test_get_severity_value_valid(self):
        """
        Test the get_severity_value function with various priority values.
        """
        self.assertEqual(get_severity_value(0), 0)
        self.assertEqual(get_severity_value(7), 7)
        self.assertEqual(get_severity_value(8), 0)
        self.assertEqual(get_severity_value(15), 7)
        self.assertEqual(get_severity_value(16), 0)
        self.assertEqual(get_severity_value(23), 7)
        self.assertEqual(get_severity_value(24), 0)
        self.assertEqual(get_severity_value(31), 7)
        self.assertEqual(get_severity_value(32), 0)
        self.assertEqual(get_severity_value(39), 7)
        self.assertEqual(get_severity_value(40), 0)
        self.assertEqual(get_severity_value(47), 7)
        self.assertEqual(get_severity_value(48), 0)
        self.assertEqual(get_severity_value(55), 7)
        self.assertEqual(get_severity_value(56), 0)
        self.assertEqual(get_severity_value(63), 7)
        self.assertEqual(get_severity_value(64), 0)
        self.assertEqual(get_severity_value(191), 7)

    def test_get_severity_value_invalid_value(self):
        """
        Test the get_severity_value function with invalid priority values.
        """
        with self.assertRaises(ValueError):
            get_severity_value(-1)
        with self.assertRaises(ValueError):
            get_severity_value(192)

    def test_get_severity_value_invalid_type(self):
        """
        Test the get_severity_value function with invalid types.
        """
        with self.assertRaises(TypeError):
            get_severity_value("invalid")
        with self.assertRaises(TypeError):
            get_severity_value(3.14)

    def test_get_severity_keyword_valid(self):
        """
        Test the get_severity_keyword function with valid severity values.
        """
        self.assertEqual(get_severity_keyword(0), "emerg")
        self.assertEqual(get_severity_keyword(1), "alert")
        self.assertEqual(get_severity_keyword(2), "crit")
        self.assertEqual(get_severity_keyword(3), "err")
        self.assertEqual(get_severity_keyword(4), "warning")
        self.assertEqual(get_severity_keyword(5), "notice")
        self.assertEqual(get_severity_keyword(6), "info")
        self.assertEqual(get_severity_keyword(7), "debug")

    def test_get_severity_keyword_invalid_value(self):
        """
        Test the get_severity_keyword function with invalid severity values.
        """
        with self.assertRaises(KeyError):
            get_severity_keyword(-1)
        with self.assertRaises(KeyError):
            get_severity_keyword(8)

    def test_get_severity_keyword_invalid_type(self):
        """
        Test the get_severity_keyword function with invalid types.
        """
        with self.assertRaises(TypeError):
            get_severity_keyword("invalid")
        with self.assertRaises(TypeError):
            get_severity_keyword(3.14)
        with self.assertRaises(TypeError):
            get_severity_keyword(None)


if __name__ == "__main__":
    unittest.main()
