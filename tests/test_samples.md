
# Test Results

Python version used: 3.12.7
Operating system: Windows
Date: 2026-11-03

| # | Input | Expected | Actual | Result |
|---|---|---|---|---|
| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found | PASS |
| 2 | http://192.0.2.10/account | IP address and HTTP warnings | IP address and HTTP warnings displayed | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol and HTTP warnings | @ symbol and HTTP warnings displayed | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments warning | Many hostname segments warning displayed | PASS |
| 5 | https://xn--example.invalid/ | Punycode warning | Punycode warning displayed | PASS |
| 6 | http://[bad | Malformed URL handled without crashing | Invalid URL format message displayed | PASS |

## Testing Notes

All five workbook sample URLs were tested successfully.

The additional malformed URL test also passed. The program handled invalid input without crashing.

All tests used fictional sample URLs. No websites were opened and no network requests were made.
