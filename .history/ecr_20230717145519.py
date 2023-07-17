import boto3

ecr_client = boto3.client('ecr')

repository_name = "my_monitoring_app_image"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 998152753302.dkr.ecr.ap-south-1.amazonaws.com