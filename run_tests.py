#!/usr/bin/env python
"""Run tests and capture output to file."""
import subprocess
import sys
import os

os.chdir('/Users/codeclouds-sayan/Projects/Python_Playwright')

# Run pytest
result = subprocess.run(
    [
        sys.executable, '-m', 'pytest',
        'tests/',
        '--browser=chromium',
        '--base-url=https://automationexercise.com',
        '--alluredir=allure-results',
        '-v',
        '--tb=short'
    ],
    capture_output=True,
    text=True,
    timeout=600
)

# Write output to file
with open('/tmp/pytest_result.txt', 'w') as f:
    f.write("STDOUT:\n")
    f.write(result.stdout)
    f.write("\n\nSTDERR:\n")
    f.write(result.stderr)
    f.write(f"\n\nReturn code: {result.returncode}\n")

print("Tests completed. Output written to /tmp/pytest_result.txt")
sys.exit(result.returncode)

