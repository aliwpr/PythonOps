import os
import sys
import docker
from docker.errors import BuildError, APIError

def buildImage(dockerfilePath, tag, buildArgs=None):
    client = docker.from_env()
    print(f"building docker image with '{tag}'...")
    try:
        image, buildLogs = client.images.build(
            path=dockerfilePath,
            tag=tag,
            buildargs=buildArgs,
            decode=True
        )
        for chunk in buildLogs:
            if 'stream' in chunk:
                print(chunk['stream'].strip())
        print(f"image {tag} built completly")
        return image
    except BuildError as e:
        print(f"failed! sry cause of this error {e}")
        for chunk in e.build_log:
            if 'stream' in chunk:
                print(chunk['stream'].strip())
        sys.exit(1)
    except APIError as e:
        print(f"sry! server returned this error  {e}")
        sys.exit(1)

def pushImage(tag):
    client = docker.from_env()
    print(f"pushing...wait ")
    try:
        for chunk in client.images.push(tag, stream=True, decode=True):
            if 'status' in chunk:
                print(chunk['status'])
        print(f"image pushed.")
    except APIError as e:
        print(f"failed to push by this error {e}")
        sys.exit(1)

def main():
    dockerfilePath = '.'  
    imageTag = 'aliImage:latest'  
    shouldPush = False  
    buildArgs = {
        "GIT_COMMIT" : "40" # or anything
    }

    myimage = buildImage(dockerfilePath, imageTag, buildArgs)

    # Push the image, if specified
    if shouldPush:
        pushImage(imageTag)

if __name__ == "__main__":
    main()