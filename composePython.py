def generateDockerCompose(environment):
    """ generate Docker Compose file for different env.

    parameters:
    - environment: target environment ('dev' or 'prod')

    returns:
    - docker Compose content(string)"""

    if environment not in ['dev', 'prod']:
        raise Exception("just 'dev' or 'prod'")
  
    commonServices = """
    version: '3'
    services:
      web:
        image: nginx:alpine
        ports:
          - "8083:80"
    """
    # or u can add every thing u want to this dev and production 
    environmentSpecificServices = {
        'dev': """
          db:
            image: postgres:latest
            ports:
              - "54321:5432"
        """,
        'prod': """
          db:
            image: postgres:latest
            ports:
              - "5432:5432"
            deploy:
              replicas: 3
        """
    }
    dockerComposeContent = commonServices + environmentSpecificServices[environment]
    # for space
    return dockerComposeContent.strip()  

def saveToFile(dockerComposeContent, fileName):

    with open(fileName, "w") as file:
        file.write(dockerComposeContent)

# example
if __name__ == "__main__":
    targetEnvironment = "dev"
    composeFileName = f"docker-compose-{targetEnvironment}.yml"
    generatedComposeContent = generateDockerCompose(targetEnvironment)
    saveToFile(generatedComposeContent, composeFileName)
