# module allows you to spawn new processes
import subprocess

def deployContainer(serviceName, image, replicas, portMapping):
    createCommand = [
        'docker', 'service', 'create',
        '--name', serviceName,
        '--replicas', str(replicas),
        '-p', portMapping,
        image
    ]
    result = subprocess.run(createCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"'{serviceName}' deployed well.")
    else:
         print(f"error deploying '{serviceName}': {result.stderr.decode('utf-8')}")


def scaleService(serviceName, replicas):
    scaleCommand = [
        'docker', 'service', 'scale',
        f'{serviceName}={replicas}'
    ]
    result = subprocess.run(scaleCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"'{serviceName}' scaled to {replicas} replicas.")
    else:
        print(f"error scaling '{serviceName}': {result.stderr.decode('utf-8')}")


def removeService(serviceName):
    removeCommand = [
        'docker', 'service', 'rm', serviceName
    ]
    result = subprocess.run(removeCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check the return code to determine success or failure
    if result.returncode == 0:
        print(f"'{serviceName}' removed.")
    else:
        print(f"error removing '{serviceName}': {result.stderr.decode('utf-8')}")


if __name__ == "__main__":
    # for example deploy nginx web server
    deployContainer('webserver', 'nginx:alpine', 3, '80:80')
    # scale it for 5
    scaleService('web-service', 5)
    # remove it
    removeService('webserver')
