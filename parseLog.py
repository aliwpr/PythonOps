import re

def parseLog_file(file_path):
    error_sample = re.compile(r'\bERROR\b', re.IGNORECASE)
    warning_sample = re.compile(r'\bWARNING\b', re.IGNORECASE)
    errors = []
    warnings = []
    with open(file_path, 'r') as f:
        for line_number, line in enumerate(f, start=1):
            if error_sample.search(line):
                errors.append(f"error in line{line_number}:{line.strip()}")

            if warning_sample.search(line):
                warnings.append(f"warning in line {line_number}:{line.strip()}")

    print("errors:")
    for error in errors:
        print(error)

    print("\nwarnings:")
    for warning in warnings:
        print(warning)
# each path you want
file_path = '/var/log/nginx/nginx_error.log'
parseLog_file(file_path)
