import docker
from docker.errors import APIError

def checkContainerHealth(container):
    if container.attrs['State']['Health']['Status'] == 'healthy':
        return True
    else:
        return False

def customHealthCheck(container):
    try:
        # this line should be our healtch check this is for demonstrate
        response = container.exec_run("curl -f http://localhost:8080/")
        if response.exit_code == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"error occured {e}")
        return False

def performHealthChecks():
    client = docker.from_env()
    try:
        # List all running containers
        containers = client.containers.list()

        for container in containers:
            if 'Health' in container.attrs['State']:
                is_healthy = checkContainerHealth(container)
            else:
                is_healthy = customHealthCheck(container)

            if is_healthy:
                print(f"container '{container.name}' is at good state.")
            else:
                print(f"container '{container.name}' is not in good state.")

    except APIError as e:
        print(f"error on docker API {e}")

def main():
    performHealthChecks()

if __name__ == "__main__":
    main()