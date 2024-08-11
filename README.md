# Syslog Priority Converter

[![Perform Python Linter Run](https://github.com/Cthullu/syslog_priority_converter/actions/workflows/python_lint.yml/badge.svg?branch=main)](https://github.com/Cthullu/syslog_priority_converter/actions/workflows/python_lint.yml)
[![.github/workflows/markdown_linter.yml](https://github.com/Cthullu/syslog_priority_converter/actions/workflows/markdown_linter.yml/badge.svg?branch=main)](https://github.com/Cthullu/syslog_priority_converter/actions/workflows/markdown_linter.yml)

I occassionaly work with syslog message processing and always find myself
struggling with converting the syslog `priority` back to `facility` and
`severity` values.

I therefore decided to write a small python tool which does the work for me.

## Usage

This tools takes a syslog priority value (integer between 0 and 191) and
prints the `priority` and `facility` `values` and `keywords`.

~~~bash
usage: convert_syslog_priority [-h] [-d] [-v] <priority>

Convert syslog priority value to facility and severity level.

positional arguments:
  <priority>     Priority to convert into facility and severity level.

options:
  -h, --help     show this help message and exit
  -d, --debug    turn on debug logging
  -v, --version  show program's version number and exit
~~~

## License

MIT

## Author

Daniel Kuß
