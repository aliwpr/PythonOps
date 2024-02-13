import re

def parseLogFile(filePath):
    errorSample = re.compile(r'\bERROR\b', re.IGNORECASE)
    warningSample = re.compile(r'\bWARNING\b', re.IGNORECASE)
    errors = []
    warnings = []
    with open(filePath, 'r') as f:
        for lineNumber, line in enumerate(f, start=1):
            if errorSample.search(line):
                errors.append(f"error in line{lineNumber}:{line.strip()}")

            if warningSample.search(line):
                warnings.append(f"warning in line {lineNumber}:{line.strip()}")

    print("errors:")
    for error in errors:
        print(error)

    print("\nwarnings:")
    for warning in warnings:
        print(warning)
# each path you want
filePath = '/var/log/nginx/nginx_error.log'
parseLogFile(filePath)
