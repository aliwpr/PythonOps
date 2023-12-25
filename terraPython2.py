import os
# pip install python_terraform
from python_terraform import Terraform

def provisionResources(provider, resourceCount):
    """automate provisioning of AWS resources with terraform.

    parameters:
    - provider: ("aws")
    - resourceCount: number of resources to provision"""

    # specify terraform folder
    terraformFolder = f"terraform_{provider}"
    os.chdir(terraformFolder)

    tf = Terraform(workingDir=".")
    tf.init()

    variables = {"resourceCount": resourceCount}

    # apply configuration
    returnCode, stdout, stderr = tf.apply(
        skip_input=True,
        no_color=IsDocker(),
        var=variables,
        auto_approve=True
    )

    # ifErr
    if returnCode != 0:
        print(f"error happens: {stderr.decode('utf-8')}")
    else:
        print("resources provisioned well.")

def IsDocker():
    """check if the script running in a docker container."""

    with open('/proc/1/cgroup', 'rt') as ifh:
        return 'docker' in ifh.read() # true or false

if __name__ == "__main__":
    # example run def
    cloudProvider = "aws"
    resourceCount = 3

    # we have to declare these 2 var for def to work 
    provisionResources(cloudProvider, resourceCount)
