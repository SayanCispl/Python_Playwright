#!/usr/bin/env python
"""Simple test runner to verify the project works."""

import subprocess
import sys
import os

def run_tests():
    """Run the pytest tests."""
    os.chdir('/Users/codeclouds-sayan/Projects/Python_Playwright')

    cmd = [
        sys.executable,
        '-m',
        'pytest',
        'tests/',
        '--browser=chromium',
        '--base-url=https://automationexercise.com',
        '-v',
        '--tb=short'
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    return result.returncode

if __name__ == '__main__':
    sys.exit(run_tests())

