#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Perform unittests related to syslog facilities.
"""

import unittest

from syslog_converter import get_facility_value
from syslog_converter import get_facility_keyword


class FacilityTests(unittest.TestCase):
    """
    Tests for syslog facility operations.
    """

    def test_get_facility_value_valid(self):
        """
        Test the get_facility_value function with various priority values.
        """
        self.assertEqual(get_facility_value(0), 0)
        self.assertEqual(get_facility_value(7), 0)
        self.assertEqual(get_facility_value(8), 1)
        self.assertEqual(get_facility_value(15), 1)
        self.assertEqual(get_facility_value(16), 2)
        self.assertEqual(get_facility_value(23), 2)
        self.assertEqual(get_facility_value(24), 3)
        self.assertEqual(get_facility_value(31), 3)
        self.assertEqual(get_facility_value(32), 4)
        self.assertEqual(get_facility_value(39), 4)
        self.assertEqual(get_facility_value(40), 5)
        self.assertEqual(get_facility_value(47), 5)
        self.assertEqual(get_facility_value(48), 6)
        self.assertEqual(get_facility_value(55), 6)
        self.assertEqual(get_facility_value(56), 7)
        self.assertEqual(get_facility_value(63), 7)
        self.assertEqual(get_facility_value(64), 8)
        self.assertEqual(get_facility_value(191), 23)


    def test_get_facility_value_invalid_value(self):
        """
        Test the get_facility_value function with invalid priority values.
        """
        with self.assertRaises(ValueError):
            get_facility_value(-1)
        with self.assertRaises(ValueError):
            get_facility_value(192)


    def test_get_facility_value_invalid_type(self):
        """
        Test the get_facility_value function with invalid types.
        """
        with self.assertRaises(TypeError):
            get_facility_value("invalid")
        with self.assertRaises(TypeError):
            get_facility_value(3.14)
        with self.assertRaises(TypeError):
            get_facility_value(None)


    def test_get_facility_keyword_valid(self):
        """
        Test the get_facility_keyword function with valid facility values.
        """
        self.assertEqual(get_facility_keyword(0), "kern")
        self.assertEqual(get_facility_keyword(1), "user")
        self.assertEqual(get_facility_keyword(2), "mail")
        self.assertEqual(get_facility_keyword(3), "daemon")
        self.assertEqual(get_facility_keyword(4), "auth")
        self.assertEqual(get_facility_keyword(5), "syslog")
        self.assertEqual(get_facility_keyword(6), "lpr")
        self.assertEqual(get_facility_keyword(7), "news")
        self.assertEqual(get_facility_keyword(8), "uucp")
        self.assertEqual(get_facility_keyword(9), "cron")
        self.assertEqual(get_facility_keyword(10), "authpriv")
        self.assertEqual(get_facility_keyword(11), "ftp")
        self.assertEqual(get_facility_keyword(12), "ntp")
        self.assertEqual(get_facility_keyword(13), "security")
        self.assertEqual(get_facility_keyword(14), "console")
        self.assertEqual(get_facility_keyword(15), "solaris-cron")
        self.assertEqual(get_facility_keyword(16), "local0")
        self.assertEqual(get_facility_keyword(17), "local1")
        self.assertEqual(get_facility_keyword(18), "local2")
        self.assertEqual(get_facility_keyword(19), "local3")
        self.assertEqual(get_facility_keyword(20), "local4")
        self.assertEqual(get_facility_keyword(21), "local5")
        self.assertEqual(get_facility_keyword(22), "local6")
        self.assertEqual(get_facility_keyword(23), "local7")


    def test_get_facility_keyword_invalid_value(self):
        """
        Test the get_facility_keyword function with invalid facility values.
        """
        with self.assertRaises(KeyError):
            get_facility_keyword(-1)
        with self.assertRaises(KeyError):
            get_facility_keyword(24)


    def test_get_facility_keyword_invalid_type(self):
        """
        Test the get_facility_keyword function with invalid types.
        """
        with self.assertRaises(TypeError):
            get_facility_keyword("invalid")
        with self.assertRaises(TypeError):
            get_facility_keyword(3.14)
        with self.assertRaises(TypeError):
            get_facility_keyword(None)
