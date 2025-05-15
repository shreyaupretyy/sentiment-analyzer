#!/usr/bin/env python3
"""
Script to automatically fix common flake8 errors:
- W293 (blank line contains whitespace)
- W292 (no newline at end of file)
"""
import os
import re

# Files to fix based on flake8 output
files_to_fix = [
    "app/api/endpoints/sentiment.py",
    "app/core/config.py",
    "app/core/settings.py",
    "app/main.py",
    "app/models/sentiment.py",
    "app/services/sentiment_analyzer.py",
    "tests/conftest.py",
    "tests/test_api/test_sentiment.py",
    "tests/test_services/test_sentiment_analyzer.py"
]

for file_path in files_to_fix:
    print(f"Fixing {file_path}...")
    
    # Read the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Fix W293: blank line contains whitespace
    # Replace any line that only has whitespace with an empty line
    content = re.sub(r'^\s+$', '', content, flags=re.MULTILINE)
    
    # Fix W292: no newline at end of file
    # Ensure file ends with exactly one newline
    if not content.endswith('\n'):
        content += '\n'
    else:
        # Remove any extra newlines at the end
        content = content.rstrip('\n') + '\n'
    
    # Write the fixed content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

print("\nFixed whitespace and newline issues.")
print("Please manually remove unused imports (F401 errors) from:")
print("- tests/test_api/test_sentiment.py: 'json' imported but unused")
print("- tests/test_services/test_sentiment_analyzer.py: 'pytest' imported but unused")