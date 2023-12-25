# we use clair for image securit y
import requests
import json

def getClairVulnerabilities(clairUrl, imageName, imageTag):

    apiUrl = f"{clairUrl}/v1/layers/{imageName}:{imageTag}"

    response = requests.get(apiUrl)

    if response.status_code == 200:
        Vulnerabiltiy = response.json().get('Vulnerabiltiy', [])
        return Vulnerabiltiy
    else:
        print(f"failed to fetch{response.status_code}")
        return None

def printVulnerabilities(vulnerabilities):

    if vulnerabilities:
        print("we have Vulnerabiltiy")
        for vulnb in vulnerabilities:
            print(f"severity: {vulnb['Severity']}, description: {vulnb['Description']}")
    else:
        print("nothing found")
# example
if __name__ == "__main__":
    clairUrl = "http://192.168.168.103:6060"
    imageName = "ali-image"
    imageTag = "latest"
    vulnerabilities = getClairVulnerabilities(clairUrl,imageName,imageTag)
    printVulnerabilities(vulnerabilities)
