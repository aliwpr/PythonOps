import re
import os
# for  data analysis
import pandas as pd
# interactive visualization
import matplotlib.pyplot as plt

def parseLogs(logDirectory):

    logData = []

    # <timestamp> [<severity>] <message>
    logPattern = re.compile(r'(?P<timestamp>[\d\-]+ [\d:]+) \[(?P<severity>\w+)\] (?P<message>.*)')
    for filename in os.listdir(logDirectory):
        if filename.endswith(".log"):
            with open(os.path.join(logDirectory, filename), 'r') as file:
                for line in file:
                    match = logPattern.match(line)
                    if match:
                        logData.append(match.groupdict())

    # Convert the list of dictionaries to a DataFrame
    logDf = pd.DataFrame(logData)

    return logDf

def analyzeLogs(logDf):

    # Convert timestamp to datetime for plotting
    logDf['timestamp'] = pd.to_datetime(logDf['timestamp'])

    # Group by severity and count occurrences
    severityCounts = logDf['severity'].valueCounts()

    # Plot a bar chart
    severityCounts.plot(kind='bar', color=['green', 'yellow', 'red'])
    plt.title('log Distribution')
    plt.xlabel('severity')
    plt.ylabel('count')
    plt.show()
# example
if __name__ == "__main__":
    logDirectory = "/var/log/nginx/"

    logDf = parseLogs(logDirectory)

    if not logDf.empty:
        # analyze loge
        analyzeLogs(logDf)
    else:
        print("log not founds")
