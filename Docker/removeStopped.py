import docker

client = docker.from_env()

def removeStoppedContainers():
    for container in client.containers.list(all=True):
        if container.status == "exited" or container.status == "created":
            print(f"removing {container.name}")
            container.remove()

def removeUnusedVolumes():
    for volume in client.volumes.list():
        if not volume.attrs['UsageData']['RefCount']:
            print(f"removing {volume.name}")
            volume.remove()

def removeUnusedNetworks():
    for network in client.networks.list():
        if len(network.attrs['Containers']) == 0 and not network.attrs['Internal']:
            print(f"removing {network.name}")
            network.remove()

def main(removeVolumes=False, removeNetworks=False):
    removeStoppedContainers()
    if removeVolumes:
        removeUnusedVolumes()
    if removeNetworks:
        removeUnusedNetworks()
if __name__ == "__main__":
    main(removeVolumes=True, removeNetworks=True)