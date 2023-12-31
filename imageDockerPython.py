import os
# pip install docker 
import docker

def buildAndPushDockerImage(imageName, tag, dockerfilePath, registryUrl=None, username=None, password=None):
    """parameters:
    - tag: 
    - registryUrl: 
    - dockerfilePath: 
    - username: 
    - password: 
    - imageName: """

    client = docker.from_env()

    # Build the Docker image
    image, logs = client.images.build(
        path=os.path.abspath(dockerfilePath),
        tag=f"{registryUrl}/{imageName}:{tag}" if registryUrl else f"{imageName}:{tag}",
        rm=True,  # rm if intermediate
    )

    print("docker image built")

    # time to push after build
    if registryUrl and username and password:
        registryAuth = {'username': username, 'password': password}
        client.images.push(f"{registryUrl}/{imageName}:{tag}", auth_config=registryAuth)

        print("image pushed")
    else:
        print("registry credentials is wrong!")
#example
if __name__ == "__main__":
    imageName = "ali-image"
    tag = "latest"
    # mean here
    dockerfilePath = "."  
    registryUrl = "http://192.168.168.103:8081"
    username = "ali"
    password = "ali-pass"
    buildAndPushDockerImage(imageName, tag, dockerfilePath, registryUrl, username, password)
