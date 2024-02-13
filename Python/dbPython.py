import os
import subprocess
import datetime
import shutil

def backupFiles(sourceDirectory, destinationDirectory):
    """
    parameters:
    - sourceDirectory:
    - destinationDirectory: 
    """

    os.makedirs(destinationDirectory, exist_ok=True)
    #20210110135713
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    backupDirectory = os.path.join(destinationDirectory, f"backup_{timestamp}")
    os.makedirs(backupDirectory)

    for root, dirs, files in os.walk(sourceDirectory):
        for file in files:
            sourcePath = os.path.join(root, file)
            relativePath = os.path.relpath(sourcePath, sourceDirectory)
            destinationPath = os.path.join(backupDirectory, relativePath)
            os.makedirs(os.path.dirname(destinationPath), exist_ok=True)
            shutil.copy2(sourcePath, destinationPath)

    print(f"backup done to {backupDirectory}")

def backupMysqlDatabase(host, user, password, database, destinationDirectory):
    """
    parameters:
    - host: 
    - user: 
    - password: 
    - database: 
    - destinationDirectory: 
    """

    os.makedirs(destinationDirectory, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backupFile = os.path.join(destinationDirectory, f"{database}_backup_{timestamp}.sql")

    mysqldump_command = [
        "mysqldump",
        "--host", host,
        "--user", user,
        "--password", password,
        database,
        "--result-file", backupFile,
    ]
    subprocess.run(mysqldump_command)

    print(f"MySQL {database} backed up  {backupFile}")
#example
if __name__ == "__main__":
    sourceDirectory = "/var/lib/ali"
    fileDestinationDirectory = "/etc/ali"

    mysqlHost = "http://127.0.0.19"
    mysqlUser = "ali"
    mysqlPassword = "ali"
    mysqlDatabase = "metal"
    mysqlDestinationDirectory = "/etc/ali"
    # we need real env
    backupFiles(sourceDirectory, fileDestinationDirectory)

    # again we need real for test as u wish
    backupMysqlDatabase(mysqlHost, mysqlUser,mysqlPassword, mysqlDatabase,mysqlDestinationDirectory)
