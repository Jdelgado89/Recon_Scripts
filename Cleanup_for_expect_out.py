@this script is meant to sperate the Shadow and Passwd file that the expect script finds.
#!/usr/bin/python3
import sys
import os
import re

if len(sys.argv) != 2:
    print("Usage: python3 split_passwd_shadow.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

if not os.path.isfile(input_file):
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)

passwd_file = "passwd_extracted.txt"
shadow_file = "shadow_extracted.txt"

# Terminal escape sequence cleanup
def remove_ansi_sequences(text):
    ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

with open(input_file, 'r') as infile:
    lines = infile.readlines()

# Clean lines
cleaned_lines = [remove_ansi_sequences(line).strip() for line in lines if line.strip()]

# Find start of "Passwd File" and "Shadow File"
passwd_start = None
shadow_start = None

for idx, line in enumerate(cleaned_lines):
    if "Passwd File" in line:
        passwd_start = idx + 1  # content starts after this
    elif "Shadow File" in line:
        shadow_start = idx + 1

# Extract portions
if passwd_start is not None and shadow_start is not None:
    passwd_lines = cleaned_lines[passwd_start:shadow_start-1]
    shadow_lines = cleaned_lines[shadow_start:]

    with open(passwd_file, 'w') as pf:
        pf.write('\n'.join(passwd_lines) + '\n')

    with open(shadow_file, 'w') as sf:
        sf.write('\n'.join(shadow_lines) + '\n')

    print(f"Extracted to '{passwd_file}' and '{shadow_file}'")
else:
    print("Could not locate 'Passwd File' or 'Shadow File' markers.")
