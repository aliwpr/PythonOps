# for sent http request pip install requests
import requests
from requests.auth import HTTPBasicAuth

def triggerJenkinsJob(jenkinsUrl, jobName, parameters, username, apiToken):
    """trigger a jenkins job with parameters with handle status.

    parameters:
    - jenkinsUrl: 
    - jobName: 
    - parameters: must be dict
    - username: we should have build permission on this user
    - apiToken: 

    returns:
    - (SUCCESS, FAILURE, ABORTED)
    """

    jobUrl = f"{jenkinsUrl}/job/{jobName}/buildWithParameters"
    # for requests
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'token': apiToken,
    }

    # we have to add paramters to data dict if we had params
    data.update(parameters)

    # triggered it 
    response = requests.post(
        jobUrl,
        headers=headers,
        data=data,
        auth=HTTPBasicAuth(username, apiToken),
    )

    # check resposne 
    if response.status_code == 201:
        print("job triggred successfully.")
    else:
        print(f"failed to trigger job.{response.status_code}")
        return None

    # get the queue item number if exist
    queueItemNumber = response.headers.get('Location').split('/')[-2]
    jobStatus = waitForJobCompletion(jenkinsUrl, queueItemNumber, username, apiToken)

    return jobStatus

def waitForJobCompletion(jenkinsUrl, queueItemNumber, username, apiToken):
    """wait for the job and send its status.

    parameters:
    - jenkinsUrl:
    - queueItemNumber: jenkins job queue item number
    - username: like first def
    - apiToken: like first def

    returns:
    - job status (SUCCESS, FAILURE, ABORTED)"""

    queueItemUrl = f"{jenkinsUrl}/queue/item/{queueItemNumber}/api/json"

    while True:
        response = requests.get(
            queueItemUrl,
            auth=HTTPBasicAuth(username, apiToken),
        )
        queueItemDetails = response.json()

        if not queueItemDetails.get('blocked', False):
            # we have to somehow get the job and its status 
            buildUrl = queueItemDetails.get('executable', {}).get('url')
            buildDetails = requests.get(
                f"{buildUrl}api/json",
                auth=HTTPBasicAuth(username, apiToken),
            ).json()
            jobStatus = buildDetails.get('result')

            return jobStatus

if __name__ == "__main__":
    # example
    jenkinsUrl = "http://192.168.168.103:8080"
    jobName = "ali-job"
    username = "ali"
    apiToken = "AKIAIOSFODNN7EXAMPLE"
    jobParameters = {
        'dict1': 'values1',
        'dict2': 'values2',
    }
    jobStatus = triggerJenkinsJob(jenkinsUrl, jobName, jobParameters, username, apiToken)

    if jobStatus:
        print(f"status: {jobStatus}")
    else:
        print("failed for getting status.")
