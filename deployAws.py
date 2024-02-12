# AWS SDK for Python(Boto3) to create,configure,and manage AWS services
import boto3

def createEc2Instance():
    # required credentials 
    awsAccessKeyId = 'AKIAIOSFODNN7SZLQWSHE'
    awsSecretAccessKey = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCY'
    regionName = 'us_east1'

    ec2 = boto3.client('ec2', aws_access_key_id=awsAccessKeyId, aws_secret_access_key=awsSecretAccessKey, region_name=regionName)
    instance_params = {
        'imageId': 'ami-xx', # ami for image u want
        'instanceType': 't2.micro',  # instance type
        'minCount': 1,
        'maxCount': 1,
        'keyName': 'nameKeyPair', 
        'securityGroupIds': ['sg-xx'],  # security group ID
        'subnetId': 'subnet-xx',
    }
    # pass the parameters to ec2 object
    response = ec2.run_instances(**instance_params)
    instanceId = response['Instances'][0]['InstanceId']
    print(f"Ec2 instance{instanceId} created")

if __name__ == "__main__":
    createEc2Instance()
