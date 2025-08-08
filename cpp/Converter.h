#include <unordered_map>
#include <string>
#ifndef CONVERTER_H
#define CONVERTER_H

using namespace std;

class Converter {
    public:
        Converter();
        Converter(int priority);
        void set_priority(int p);
        int get_priority();
        int get_facility();
        int get_severity();
        string get_severity_level();
        string get_facility_level();

    private:
        const int PRIORITY_CONVERSION_FACTOR = 8;
        const int MIN_PRIORITY = 0; // Minimum syslog priority value
        const int MAX_PRIORITY = 191; // Maximum syslog priority value

        const unordered_map<int, string> SEVERITY_LEVEL_MAP = {
            {0, "Emergency"},
            {1, "Alert"},
            {2, "Critical"},
            {3, "Error"},
            {4, "Warning"},
            {5, "Notice"},
            {6, "Informational"},
            {7, "Debug"}
        };

        const unordered_map<int, string> FACILITY_LEVEL_MAP = {
            {0, "Kernel messages"},
            {1, "User-level messages"},
            {2, "Mail system"},
            {3, "System daemons"},
            {4, "Security/authorization messages"},
            {5, "Messages generated internally by syslogd"},
            {6, "Line printer subsystem"},
            {7, "Network news subsystem"},
            {8, "UUCP subsystem"},
            {9, "Clock daemon"},
            {10, "Security/authorization messages"},
            {11, "FTP daemon"},
            {12, "NTP subsystem"},
            {13, "Log audit"},
            {14, "Log alert"},
            {15, "Clock daemon (note 2)"},
            {16, "Local use 0"},
            {17, "Local use 1"},
            {18, "Local use 2"},
            {19, "Local use 3"},
            {20, "Local use 4"},
            {21, "Local use 5"},
            {22, "Local use 6"},
            {23, "Local use 7"}
        };


        int priority;
        int facility;
        int severity;

        bool is_valid_priority(int p);
        int convert_priority_to_facility(int p);
        int convert_priority_to_severity(int p);
};

#endif
