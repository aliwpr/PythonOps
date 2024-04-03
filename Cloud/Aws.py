import boto3

AWSaccessKey = "myAccessKey"
AWSsecretKey = 'mySecretKey'

# create abd s3 client
s3 = boto3.client('s3', aws_access_key_id=AWSaccessKey, aws_secret_access_key=AWSsecretKey)

def uploadToS3(bucketName, filePath, keyName):
    try:
        s3.upload_file(filePath, bucketName, keyName)
        print(f"file uploaded .")
    except Exception as e:
        print(f"error occured: {e}")

def downloadFromS3(bucketName, keyName, localFilePath):
    """Download a file from AWS S3 bucket."""
    try:
        s3.download_file(bucketName, keyName, localFilePath)
        print(f"file  downloaded.")
    except Exception as e:
        print(f"error when downloading : {e}")
