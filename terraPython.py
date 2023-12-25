# generate terraForm configurations based on params

def generateTerraformConfig(resourceName, instanceType, region, count):
    
    """ parameters:
    - resourceName: name of the resource
    - instanceType: type of the intance 
    - region: AWS region 
    - count: number of instances to craet

    returns:
    - terraform configuration as a string """
    terraformTemplate = f"""
    provider "aws" {{
      region = "{region}"
    }}

    resource "aws_instance" "{resourceName}" {{
      instance_type = "{instanceType}"
      count         = {count}
    }}
    """
    # remove whitespace
    return terraformTemplate.strip()  

def saveToFile(terraformConfig, fileName):
    """ parameters:
    - terraformConfig: Terraform configuration as a string
    - fileName: Name of the file to save the configuration"""

    with open(fileName, "w") as file:
        file.write(terraformConfig)

if __name__ == "__main__":
    resourceName = "webServer"
    instanceType = "t2.micro"
    region = "us-east-2"
    count = 3
    # we have to fill for this def to work 
    generatedConfig = generateTerraformConfig(resourceName, instanceType, region, count)
    # this def too
    saveToFile(generatedConfig, "generated.tf")
