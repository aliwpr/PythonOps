#file level operation
import shutil
from datetime import datetime

def backupData(source, destination):
    #option time output like this or which u want! 19930212145815
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backupFolder = f"backup_{timestamp}"
    try:
        # Copy the contents of the source folder to the backup folder
        shutil.copytree(source, f"{destination}/{backupFolder}")
        print(f"backup completed successfully to {destination}/{backupFolder}")
    except Exception as e:
        print(f"error during backup:{e}")

# each source and destination directory u  can mention now data directory to backup directory
source = 'data'
destination = 'backup'
backupData(source, destination)
