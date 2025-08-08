#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Converter:
    def __init__(self, priority: int):
        """
        Initialize a Converter with a priority.

        Args:
            priority (int): The priority to convert.

        Raises:
            ValueError: If the priority is not between 0 and 191 inclusive.
        """
        self.__PRIORITY_CONVERSION_FACTOR = 8

        self.__FACILITY_KEYWORDS = {
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

        self.__SEVERITY_KEYWORDS = {
            0: "emerg",
            1: "alert",
            2: "crit",
            3: "err",
            4: "warning",
            5: "notice",
            6: "info",
            7: "debug",
        }

        self.priority = priority


    def __str__(self) -> str:
        """
        Returns a string representation of the Converter.

        Args:
            None

        Returns:
            str: A string representation of the Converter. Including priority, severity, facility
                and their name representives.

        """
        return f"{self.priority}"


    @property
    def priority(self) -> int:
        """
        Get the priority value.

        Args:
            None

        Returns:
            int: The priority value.
        """
        return self._priority


    @priority.setter
    def priority(self, priority: int) -> None:
        """
        Set the priority value.

        Args:
            priority (int): The value to set as priority

        Returns:
            None

        Raises:
            ValueError: If the priority is not between 0 and 191 inclusive.
        """
        if priority < 0 or priority > 191:
            raise ValueError("Priority must be between 0 and 191 inclusive.")

        self._priority = priority


    @property
    def facility(self) -> int:
        """
        Get the facility level (nummeric).

        Args:
            None

        Returns:
            int: The nummeric facility level.
        """
        self._facility = self._priority // self.__PRIORITY_CONVERSION_FACTOR
        return self._facility


    @property
    def facility_level(self) -> str:
        """
        Get the facility level (string).

        Args:
            None

        Returns:
            str: The facility level name.

        Raises:
            KeyError: If the facility value is not recognized.
        """
        try:
            return self.__FACILITY_KEYWORDS[self._facility]
        except KeyError as exc:
            raise KeyError("Facility must be between 0 and 23 inclusive.") from exc


    @property
    def severity(self) -> int:
        """
        Get the severity level (nummeric).

        Args:
            None

        Returns:
            int: The nummeric severity level.
        """
        self._severity = self._priority % self.__PRIORITY_CONVERSION_FACTOR
        return self._severity


    @property
    def severity_level(self) -> str:
        """
        Get the facility level (string).

        Args:
            None

        Returns:
            str: The severity level name.

        Raises:
            KeyError: If the severity value is not recognized.
        """
        try:
            return self.__SEVERITY_KEYWORDS[self._severity]
        except KeyError as exc:
            raise KeyError("Severity must be between 0 and 7 inclusive.") from exc
