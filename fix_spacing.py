#!/usr/bin/env python3
"""
Script to fix E302 and E305 spacing issues in Python files:
- E302: expected 2 blank lines, found 1
- E305: expected 2 blank lines after class or function definition, found 1
"""
import re
import os

# Files with E302/E305 issues based on flake8 output
files_to_fix = [
    "app/api/endpoints/sentiment.py",
    "app/core/config.py",
    "app/core/settings.py",
    "app/main.py",
    "app/models/sentiment.py",
    "app/services/sentiment_analyzer.py",
    "tests/conftest.py",
    "tests/test_services/test_sentiment_analyzer.py"
]

def fix_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Convert Windows line endings to Unix for consistency
    content = content.replace('\r\n', '\n')
    
    # Fix pattern for E302: Functions and classes should have two blank lines before them
    # Look for patterns where there's only one blank line before a def or class
    content = re.sub(r'([^\n])\n\n(class |def )', r'\1\n\n\n\2', content)
    content = re.sub(r'([^\n])\n(class |def )', r'\1\n\n\n\2', content)
    
    # Fix pattern for E305: Two blank lines after function or class
    content = re.sub(r'(def [^\n]+\n[^\n]*\n[^\n]*\n)\n(class |def )', r'\1\n\n\2', content)
    content = re.sub(r'(class [^\n]+\n[^\n]*\n[^\n]*\n)\n(class |def )', r'\1\n\n\2', content)
    
    # Ensure file ends with exactly one newline
    content = content.rstrip('\n') + '\n'
    
    # Write back the fixed content
    with open(file_path, 'w') as f:
        f.write(content)

# Process each file
for file_path in files_to_fix:
    print(f"Fixing spacing issues in {file_path}...")
    normalized_path = file_path.replace('\\', '/')
    fix_file(normalized_path)

print("\nAttempted to fix E302 and E305 spacing issues.")
print("Please run flake8 again to verify the fixes worked.")
print("You may need to manually adjust some files if automatic fixes weren't complete.")