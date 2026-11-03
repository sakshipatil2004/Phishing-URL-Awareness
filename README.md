
# Phishing URL Awareness Checker

## 1. Project Overview

The Phishing URL Awareness Checker is a beginner-friendly Python command-line application developed as part of the EWB Cybersecurity Internship mini project.

The tool examines URL text for common warning signs that may be associated with phishing attacks. It helps users identify suspicious URL characteristics and understand why they should inspect unexpected links carefully.

The program performs text-based checks only. It does not open websites, connect to the internet, or use external APIs.

## 2. Features

The checker identifies six URL warning signs:

1. **@ Symbol Detection:** Checks whether the URL contains an @ symbol.
2. **URL Length Check:** Identifies URLs longer than 100 characters.
3. **IP Address Detection:** Checks whether the hostname uses an IPv4-style address instead of a domain name.
4. **Hostname Segment Check:** Identifies hostnames containing five or more dot-separated segments.
5. **Punycode Detection:** Checks whether the hostname contains the `xn--` marker.
6. **HTTP Scheme Detection:** Identifies URLs using HTTP instead of HTTPS.

Additional features:

- Explains why each warning sign matters.
- Displays a security summary when warning signs are found.
- Allows users to check multiple URLs using a continuous loop.
- Supports a quit command to exit the application.
- Handles malformed URL input without crashing.

## 3. Technologies and Requirements

- Programming Language: Python 3.10 or above
- Editor: Visual Studio Code
- Python Libraries:
  - `re` (regular expressions)
  - `urllib.parse` (URL parsing)

All libraries used are included with Python. No additional packages or API keys are required.

## 4. Project Structure

```text
phishing-url-awareness/
│
├── phishing_checker.py
├── README.md
├── requirements.txt
│
├── tests/
│   └── test_samples.md
│
└── screenshots/
    ├── sample_run.png
    └── test_results.png
```

## 5. How to Run the Project

### Step 1: Install Python

Install Python 3.10 or above if it is not already installed.

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

### Step 3: Open the Terminal

In VS Code, select Terminal → New Terminal.

### Step 4: Run the Program

Execute the following command:

```bash
python phishing_checker.py
```

### Step 5: Enter a URL

Enter a sample URL when prompted. The program will display any identified warning signs and explain why they matter.

Type `quit` to exit the application.

## 6. Example Output

Example input:

```text
http://192.0.2.10/account
```

Expected warning categories:

- IP address used instead of a familiar domain.
- HTTP scheme detected.

The application also displays explanations and a security summary.

## 7. Testing

The application was tested using all five sample URLs provided in the EWB project workbook. An additional malformed URL test was also performed.

| Test | Description | Result |
|---|---|---|
| 1 | Normal-looking HTTPS URL | PASS |
| 2 | URL containing an IP address and HTTP | PASS |
| 3 | URL containing an @ symbol and HTTP | PASS |
| 4 | URL containing multiple hostname segments | PASS |
| 5 | URL containing a punycode marker | PASS |
| 6 | Malformed URL input | PASS |

Detailed test inputs and results are documented in `tests/test_samples.md`.

## 8. Screenshots

The following screenshots provide evidence of the application execution and testing:

- `screenshots/sample_run.png` – Example program execution and warning output.
- `screenshots/test_results.png` – Evidence of the five workbook sample tests.

## 9. Improvements Implemented

The following improvements were added to make the application more useful and user-friendly:

1. **Continuous URL Checking:** Added a loop so users can inspect multiple URLs without restarting the program.
2. **Warning Explanations:** Added simple explanations for each detected warning sign to help users understand potential risks.
3. **Security Summary:** Added a summary when warning signs are detected, reminding users to review the URL carefully.
4. **Malformed Input Handling:** Added error handling to prevent the program from crashing when it receives malformed URL input.
5. **Improved Output Formatting:** Organized the results into readable sections.

These improvements were checked through sample inputs and repeated program execution.

## 10. Limitations

- The application checks only six selected URL characteristics.
- It does not determine whether a website is genuinely malicious.
- It does not access threat intelligence databases.
- It does not open or scan websites.
- It does not perform real-time URL reputation checks.
- A URL with no detected warning signs is not necessarily safe.
- HTTPS does not guarantee that a website is legitimate.

The tool is intended for basic phishing awareness and educational purposes, not as a replacement for professional security solutions.

## 11. Ethical Use

This project is designed for cybersecurity education and phishing awareness.

All testing was performed using fictional sample URLs. The application does not access websites, send network requests, or collect user information.

Users should verify unexpected links through trusted, independent sources rather than relying only on automated URL checks.

## 12. Author

Name: Sakshi Prabhakar Patil 

Project: Phishing URL Awareness Checker

Internship: EWB Cybersecurity Internship
