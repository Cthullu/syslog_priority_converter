#include <iostream>
#include "Converter.h"


void print_usage() {
    // Print the usage instructions for the program
    std::cout << "Usage: syslog_priority_converter <syslog_priority> | --help" << std::endl;
    std::cout << "Converts syslog priority to a human-readable format." << std::endl;
    std::cout << "Example: syslog_priority_converter 3" << std::endl;
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
    } catch (const std::invalid_argument& e) {
        std::cerr << "Syslog priority must be an integer, not: " << argv[1] << std::endl;
        return 1;
    }

    // Create an instance of SyslogPriorityConverter
    Converter converter;

    // Try to pass the priority to the converter
    try {
        converter.set_priority(syslog_priority);
    } catch (const std::out_of_range& e) {
        std::cerr << e.what() << std::endl;
        return 1;
    } catch (std::string& e) {
        std::cerr << e << std::endl;
        return 1;
    }

    // Get the facility and severity levels from the converter
    int facility = converter.get_facility();
    int severity = converter.get_severity();
    std::string severity_level = converter.get_severity_level();
    std::string facility_level = converter.get_facility_level();

    // Print the results
    std::cout << "Syslog Priority: " << syslog_priority << std::endl;
    std::cout << "Severity Level: " << severity << " " << severity_level << std::endl;
    std::cout << "Facility Level: " << facility << " " << facility_level << std::endl;

    // Exit the program successfully
    return 0;
}
