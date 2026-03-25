#!/usr/bin/env python
"""Analyze Allure test results."""
import json
import glob
import os

os.chdir('/Users/codeclouds-sayan/Projects/Python_Playwright')

# Read result files
result_files = glob.glob('allure-results/*result.json')
print(f"Total test result files: {len(result_files)}")

passed = 0
failed = 0
skipped = 0
errors = []

for result_file in result_files[:10]:  # Check first 10
    try:
        with open(result_file) as f:
            data = json.load(f)
            status = data.get('status', 'unknown')
            test_name = data.get('name', 'unknown')

            if status == 'passed':
                passed += 1
                print(f"✓ PASSED: {test_name}")
            elif status == 'failed':
                failed += 1
                print(f"✗ FAILED: {test_name}")
                # Check for errors
                if 'statusDetails' in data:
                    errors.append({
                        'test': test_name,
                        'message': data['statusDetails'].get('message', 'No message')
                    })
            elif status == 'skipped':
                skipped += 1
                print(f"⊘ SKIPPED: {test_name}")
    except Exception as e:
        print(f"Error reading {result_file}: {e}")

print(f"\nSummary:")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Skipped: {skipped}")

if errors:
    print(f"\nErrors found:")
    for error in errors[:5]:
        print(f"  - {error['test']}: {error['message'][:100]}")

# Write summary to file
with open('/tmp/allure_summary.txt', 'w') as f:
    f.write(f"Passed: {passed}\n")
    f.write(f"Failed: {failed}\n")
    f.write(f"Skipped: {skipped}\n")
    f.write(f"\nErrors:\n")
    for error in errors:
        f.write(f"  {error['test']}\n")

print("\nSummary written to /tmp/allure_summary.txt")

