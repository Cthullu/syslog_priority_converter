#include "Converter.h"
#include <iostream>

using namespace std;


// Constructor that takes a syslog priority and initializes the class
Converter::Converter() {
    priority = -1;
}


Converter::Converter(int p) {
    try {
        set_priority(p);
    } catch (std::string) {
        __throw_exception_again;
    }
}


// Priority setter
void Converter::set_priority(int p) {
    if (is_valid_priority(priority)) {
        facility = convert_priority_to_facility(priority);
        severity = convert_priority_to_severity(priority);
    } else {
        throw std::out_of_range("Syslog priority must be between 0 and 191.");
    }
}


// Getters for the private members
int Converter::get_priority() {
    if (priority == -1) {
        throw ("Converter not yet initialized");
    }
    return priority;
}


int Converter::get_facility() { return facility; }
int Converter::get_severity() { return severity; }


string Converter::get_severity_level() {
    // Get the severity level as string
    auto it = FACILITY_LEVEL_MAP.find(facility);
    if (it != FACILITY_LEVEL_MAP.end()) {
        return it->second;
    }
    return "Unknown Facility";
}


string Converter::get_facility_level() {
    // Get the severity level as a string
    auto it = SEVERITY_LEVEL_MAP.find(severity);
    if (it != SEVERITY_LEVEL_MAP.end()) {
        return it->second;
    }
    return "Unknown Severity";
}


// Class methods/functions
bool Converter::is_valid_priority(int p) {
    return (p >= MIN_PRIORITY && p <= MAX_PRIORITY);
}


int Converter::convert_priority_to_facility(int priority) {
    // Convert syslog priority to a facility level
    return priority / PRIORITY_CONVERSION_FACTOR;
}


int Converter::convert_priority_to_severity(int priority) {
    // Convert syslog priority to a severity level
    return priority % PRIORITY_CONVERSION_FACTOR;
}
