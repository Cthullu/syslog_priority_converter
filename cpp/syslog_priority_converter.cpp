#include <iostream>
#include <unordered_map>

// Using constexpr to define a constant for the priority conversion factor
constexpr int PRIORITY_CONVERSION_FACTOR = 8;
constexpr int MIN_PRIORITY = 0; // Minimum syslog priority value
constexpr int MAX_PRIORITY = 191; // Maximum syslog priority value

const std::unordered_map<int, std::string> SEVERITY_LEVEL_MAP = {
    {0, "Emergency"},
    {1, "Alert"},
    {2, "Critical"},
    {3, "Error"},
    {4, "Warning"},
    {5, "Notice"},
    {6, "Informational"},
    {7, "Debug"}
};

const std::unordered_map<int, std::string> FACILITY_LEVEL_MAP = {
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


void print_usage() {
    // Print the usage instructions for the program
    std::cout << "Usage: syslog_priority_converter <syslog_priority> | --help" << std::endl;
    std::cout << "Converts syslog priority to a human-readable format." << std::endl;
    std::cout << "Example: syslog_priority_converter 3" << std::endl;
}


bool is_valid_priority(int priority) {
    // Check if the priority is within the valid range
    return (priority >= MIN_PRIORITY && priority <= MAX_PRIORITY);
}


int convert_priority_to_severity(int priority) {
    // Convert syslog priority to a severity level
    return priority / PRIORITY_CONVERSION_FACTOR;
}


int convert_priority_to_facility(int priority) {
    // Convert syslog priority to a facility level
    return priority % PRIORITY_CONVERSION_FACTOR;
}


std::string get_severity_level(int severity) {
    // Get the severity level as a string
    auto it = SEVERITY_LEVEL_MAP.find(severity);
    if (it != SEVERITY_LEVEL_MAP.end()) {
        return it->second;
    }
    return "Unknown Severity";
}


std::string get_facility_level(int facility) {
    // Get the facility level as a string
    auto it = FACILITY_LEVEL_MAP.find(facility);
    if (it != FACILITY_LEVEL_MAP.end()) {
        return it->second;
    }
    return "Unknown Facility";
}

int main(int argc, char *argv[]) {
    // Check if the correct number of arguments is provided
    // The program expects one argument: either the syslog priority or "--help"
    if (argc != 2) {
        print_usage();
        return 1;
    }

    // Check if the argument is "--help"
    if (std::string(argv[1]) == "--help") {
        print_usage();
        return 0;
    }

    // Convert the argument to an integer
    int syslog_priority;
    try {
        syslog_priority = std::stoi(argv[1]);
    } catch (const std::invalid_argument &e) {
        std::cerr << "Syslog priority must be an integer, not: " << argv[1] << std::endl;
        return 1;
    }

    // Check if the syslog priority is within the valid range (0-191)
    if (not is_valid_priority(syslog_priority)) {
        std::cerr << "Syslog priority must be between 0 and 191." << std::endl;
        return 1;
    }

    // Convert the syslog priority to severity and facility
    int severity = convert_priority_to_severity(syslog_priority);
    int facility = convert_priority_to_facility(syslog_priority);

    // Get the human-readable severity and facility level
    std::string severity_level = get_severity_level(severity);
    std::string facility_level = get_facility_level(facility);

    // Print the results
    std::cout << "Syslog Priority: " << syslog_priority << std::endl;
    std::cout << "Severity Level: " << severity << " " << severity_level << std::endl;
    std::cout << "Facility Level: " << facility << " " << facility_level << std::endl;

    // Exit the program successfully
    return 0;
}
