import docker
import requests
import json

# Configuration
containerName = "my-container"  
loggingEndpoint = "http://fluentbit.com/logs"  # or everything else
headers = {'Content-Type': 'application/json'}

client = docker.from_env()

def forwardLogs(log):
    try:
        response = requests.post(loggingEndpoint, data=json.dumps(log), headers=headers)
        response.raise_for_status()
        print(f"log forwarde complete")
    except requests.exceptions.RequestException as e:
        print(f"{e}")

try:
    container = client.containers.get(containerName)
except docker.errors.NotFound:
    print(f"container does not exist")
    exit(1)

for line in container.logs(stream=True, follow=True):
    logEntry = {
        "container_id": container.short_id,
        "container_name": container.name,
        "log": line.decode('utf-8').strip()
    }
    forwardLogs(logEntry)