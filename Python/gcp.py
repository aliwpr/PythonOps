import boto3
import os
from google.cloud import storage

awsAccessKeyId = 'myAccessId'
awsSecretAccessKey = 'mySecretAccessKey'
awsRegionName = 'myRegion'

s3Client = boto3.client('s3', aws_access_key_id=awsAccessKeyId, aws_secret_access_key=awsSecretAccessKey, region_name=awsRegionName)
ec2Resource = boto3.resource('ec2', aws_access_key_id=awsAccessKeyId, aws_secret_access_key=awsSecretAccessKey, region_name=awsRegionName)

def startEc2Instance(instanceId):
    ec2Resource.Instance(instanceId).start()
    print(f'EC2 instance started')

def stopEc2Instance(instanceId):
    ec2Resource.Instance(instanceId).stop()
    print(f'EC2 instance stopped.')

# Define AWS S3 functions
def uploadFileToS3(filePath, bucketName, objectName=None):
    if objectName is None:
        objectName = os.path.basename(filePath)
    
    response = s3Client.upload_file(filePath, bucketName, objectName)
    print(f'file uploaded!')

def downloadFileFromS3(bucketName, objectName, file_path):
    s3Client.download_file(bucketName, objectName, file_path)
    print(f'file downloaded!')

# Usage
if __name__ == "__main__":
    instanceIdExample = 'i-1234567890abcdef0'
    startEc2Instance(instanceIdExample)
    stopEc2Instance(instanceIdExample)
    
    
    fileToUpload = 'var/log/file.txt'
    s3BucketName = 'myBucketName'
    s3ObjectName = 'myUploadedFile-txt'
    
    uploadFileToS3(fileToUpload, s3BucketName, s3ObjectName)
    downloadFileFromS3(s3BucketName, s3ObjectName, 'var/log/file.txt')