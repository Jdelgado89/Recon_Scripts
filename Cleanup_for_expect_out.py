import sys
import os
import re

if len(sys.argv) < 2:
    print("Usage: python3 split_passwd_shadow.py <file1> [file2 file3 ...]")
    sys.exit(1)

# Terminal escape sequence cleanup
def remove_ansi_sequences(text):
    ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

for input_file in sys.argv[1:]:
    if not os.path.isfile(input_file):
        print(f"Skipping '{input_file}': Not a valid file.")
        continue

    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Clean and strip empty lines
    cleaned_lines = [remove_ansi_sequences(line).strip() for line in lines if line.strip()]

    # Find start of passwd and shadow sections
    passwd_start = None
    shadow_start = None

    for idx, line in enumerate(cleaned_lines):
        if "Passwd File" in line:
            passwd_start = idx + 1
        elif "Shadow File" in line:
            shadow_start = idx + 1

    if passwd_start is not None and shadow_start is not None:
        passwd_lines = cleaned_lines[passwd_start:shadow_start - 1]
        shadow_lines = cleaned_lines[shadow_start:]

        # Append to output files
        with open("passwd_extracted.txt", "a") as pf:
            pf.write(f"# Extracted from {input_file}\n")
            pf.write('\n'.join(passwd_lines) + '\n')

        with open("shadow_extracted.txt", "a") as sf:
            sf.write(f"# Extracted from {input_file}\n")
            sf.write('\n'.join(shadow_lines) + '\n')

        print(f"Appended: {input_file}")
    else:
        print(f"Skipped '{input_file}': Could not find both 'Passwd File' and 'Shadow File' markers.")
