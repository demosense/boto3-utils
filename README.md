# Boto3 Utils

Python package for some functionality related with AWS Boto3 SDK, specially useful in AWS Lambda.
The functionality does an atomic operation to avoid connexion interruptions, also downloads the zip data on RAM
to avoid disk size limits


Usage:

`from boto3_utils import Boto3Utils`

`Boto3Utils.download(local_key_path, bucket, local_name, bucket_key, local_folder_path)`

