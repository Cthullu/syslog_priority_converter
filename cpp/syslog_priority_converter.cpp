#include <iostream>
#include "Converter.h"


using namespace std;

void print_usage() {
    // Print the usage instructions for the program
    cout << "Usage: syslog_priority_converter <syslog_priority> | --help" << endl;
    cout << "Converts syslog priority to a human-readable format." << endl;
    cout << "Example: syslog_priority_converter 3" << endl;
}


int main(int argc, char *argv[]) {
    // Check if the correct number of arguments is provided
    // The program expects one argument: either the syslog priority or "--help"
    if (argc != 2) {
        print_usage();
        return 1;
    }

    // Check if the argument is "--help"
    if (string(argv[1]) == "--help") {
        print_usage();
        return 0;
    }

    // Convert the argument to an integer
    int syslog_priority;
    try {
        syslog_priority = stoi(argv[1]);
    } catch (const invalid_argument& e) {
        cerr << "Syslog priority must be an integer, not: " << argv[1] << endl;
        return 1;
    }

    // Create an instance of SyslogPriorityConverter
    Converter converter;

    // Try to pass the priority to the converter
    try {
        converter.set_priority(syslog_priority);
    } catch (const out_of_range& e) {
        cerr << e.what() << endl;
        return 1;
    } catch (string& e) {
        cerr << e << endl;
        return 1;
    }

    // Get the facility and severity levels from the converter
    int facility = converter.get_facility();
    int severity = converter.get_severity();
    string severity_level = converter.get_severity_level();
    string facility_level = converter.get_facility_level();

    // Print the results
    cout << "Syslog Priority: " << syslog_priority << endl;
    cout << "Severity Level: " << severity << " " << severity_level << endl;
    cout << "Facility Level: " << facility << " " << facility_level << endl;

    // Exit the program successfully
    return 0;
}
