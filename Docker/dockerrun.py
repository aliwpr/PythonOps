import docker

client = docker.from_env()

def deployContainer(imageName, command=None, ports=None, environment=None, volumes=None, name=None):
    try:
        print(f"deploying container from image {imageName}...")
        
        client.images.pull(imageName)
        
        container = client.containers.run(
            image=imageName,
            command=command,
            ports=ports,
            environment=environment,
            volumes=volumes,
            name=name,
            detach=True
        )
        
        print(f"container {container.id} started.")
    except docker.errors.APIError as e:
        print(f"{e.explanation}")


if __name__ == "__main__":
    container_image = "nginx"
    container_name = "my-nginx-container"
    container_ports = {'80/tcp': 8080}  
    container_volumes = {'/opt/nginx': {'bind': '/etc/nginx', 'mode': 'rw'}}

    deployContainer(
        image_name=container_image,
        ports=container_ports,
        volumes=container_volumes,
        name=container_name
    )