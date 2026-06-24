# Blind Time-Based SQL Injection Demo

An educational Python project demonstrating the concept of **Time-Based Blind SQL Injection** against intentionally vulnerable laboratory environments.

> **Disclaimer:** This project is provided for educational purposes only. It is intended for use in authorized security labs, training platforms, and environments where you have explicit permission to perform testing.

## Overview

This script illustrates how response timing can be used to infer information from a backend database when direct query results are unavailable. By measuring server delays triggered by conditional SQL statements, the script reconstructs a target value character by character.

The implementation is designed to help students and cybersecurity enthusiasts understand:

* Time-Based Blind SQL Injection concepts
* Automated HTTP requests with Python
* Response time analysis
* Character-by-character extraction logic
* Basic scripting techniques used in penetration testing labs

## Features

* Python implementation using the `requests` library
* Automated extraction workflow
* Modular and easy-to-read code structure
* Suitable for educational demonstrations and security training
* Configurable target URL and extraction parameters

## Requirements

* Python 3.x
* `requests`

Install dependencies:

```bash
pip install requests
```

## Usage

Configure the target laboratory environment and required parameters inside the script, then execute:

```bash
python main.py
```

## Notes

This repository intentionally excludes any real credentials, sensitive information, or production targets.

It should only be used in environments where testing is explicitly authorized, such as security training labs or personal practice setups.

## License

This project is released under the MIT License — see the [LICENSE](LICENSE) file for details.
