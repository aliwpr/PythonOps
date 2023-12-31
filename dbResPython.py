import os
import shutil
import datetime
# we have to restore it from last backup folder in dbPython.py
def restoreFiles(backupDirectory, destinationDirectory):
    """
    parameters:
    - backupDirectory: 
    - destinationDirectory:
    """

    backupDirectories = sorted(
        [os.path.join(backupDirectory, d) for d in os.listdir(backupDirectory)],
        key=lambda x: os.path.getmtime(x),
        reverse=True
    )

    if not backupDirectories:
        print("backup directory does not exist")
        return None

    latestBackupDirectory = backupDirectories[0]

    # Copy files from the latest backup to the destination directory
    for root, dirs, files in os.walk(latestBackupDirectory):
        for file in files:
            sourcePath = os.path.join(root, file)
            relativePath = os.path.relpath(sourcePath, latestBackupDirectory)
            destinationPath = os.path.join(destinationDirectory, relativePath)
            os.makedirs(os.path.dirname(destinationPath), exist_ok=True)
            shutil.copy2(sourcePath, destinationPath)

    print(f"done to  {destinationDirectory}")
#example
if __name__ == "__main__":
    backupDirectory = "/var/lib/ali"

    destinationDirectory = "/var/lib/muysql" 
    restoreFiles(backupDirectory, destinationDirectory)
