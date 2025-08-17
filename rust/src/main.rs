use clap::Parser;
use lazy_static::lazy_static;
use std::collections::HashMap;

// Our global syslog priority convert value
static SYSLOG_PRIORITY_CONVERT: u8 = 8;

lazy_static! {
    // This is a map of syslog severity values to their string representations
    static ref SEVERITY_MAP: HashMap<u8, &'static str> = {
        let mut m = HashMap::new();
        m.insert(0, "Emergency");
        m.insert(1, "Alert");
        m.insert(2, "Critical");
        m.insert(3, "Error");
        m.insert(4, "Warning");
        m.insert(5, "Notice");
        m.insert(6, "Informational");
        m.insert(7, "Debug");
        m
    };
}

// This is a map of syslog facility values to their string representations
lazy_static! {
    static ref FACILITY_MAP: HashMap<u8, &'static str> = {
        let mut m = HashMap::new();
        m.insert(0, "Kernel messages");
        m.insert(1, "User-level messages");
        m.insert(2, "Mail system");
        m.insert(3, "System daemons");
        m.insert(4, "Security/authorization messages");
        m.insert(5, "Messages generated internally by syslogd");
        m.insert(6, "Line printer subsystem");
        m.insert(7, "Network news subsystem");
        m.insert(8, "UUCP subsystem");
        m.insert(9, "Clock daemon");
        m.insert(10, "Security/authorization messages");
        m.insert(11, "FTP daemon");
        m.insert(12, "NTP subsystem");
        m.insert(13, "Log audit");
        m.insert(14, "Log alert");
        m.insert(15, "Clock daemon (note 2)");
        m.insert(16, "Local use 0 (local0)");
        m.insert(17, "Local use 1 (local1)");
        m.insert(18, "Local use 2 (local2)");
        m.insert(19, "Local use 3 (local3)");
        m.insert(20, "Local use 4 (local4)");
        m.insert(21, "Local use 5 (local5)");
        m.insert(22, "Local use 6 (local6)");
        m.insert(23, "Local use 7 (local7)");
        m
    };
}


// This is the command line interface (CLI) for our syslog priority converter.
// It uses the `clap` crate to parse command line arguments.
#[derive(Parser)]
#[command(version, about, long_about = None)]
struct Cli {
    /// We directly check for type and range of the syslog priority value (0-191)
    #[arg(value_parser = clap::value_parser!(u8).range(0..=191))]
    priority: u8,
}

fn main() {
    // First, we read CLI input
    // We should check if the input is within the valid range (0 - 191). if not, we should return an
    // error. We should also handle the case where the input is not a valid number.
    // This is all taken care of by the `clap` crate.
    let cli = Cli::parse();

    // Now we convert the syslog priority to severity and facility.
    // Syslog severity is the remainder when divided by the syslog priority convert value
    let severity: u8 = cli.priority % SYSLOG_PRIORITY_CONVERT;

    // Syslog facility is the quotient when divided by the syslog priority convert value
    let facility: u8 = cli.priority / SYSLOG_PRIORITY_CONVERT;


    // Let's do some testing to see if the severity and facility values are correct
    let severity_str = unwrap_hashmap_value(&SEVERITY_MAP, severity);
    let facility_str = unwrap_hashmap_value(&FACILITY_MAP, facility);

    // Finally, we print the syslog severity and facility to the console
    println!("Syslog severity: {severity} {severity_str}");
    println!("Syslog facility: {facility} {facility_str}");
}

fn unwrap_hashmap_value(map_to_unwrap: &HashMap<u8, &'static str>, search_value: u8) -> &'static str {
    // This function is used to unwrap the hashmap value and return the string representation.
    // If the value is not found, we return "Unknown".

    let foo = map_to_unwrap.get(&search_value);
    match foo {
        Some(value) => {
            &*value
        }
        None => {
            "Unknown"
        }
    }
}
