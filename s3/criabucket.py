import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def create_s3_bucket(bucket_name, region=None):
    try:
        s3_client = boto3.client('s3', region_name=region)
        if region:
            response = s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        else:
            response = s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully.")
        return response
    except NoCredentialsError:
        print("Error: No AWS credentials found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    bucket_name = "luccas101001"
    region = "us-east-1"  # Altere para a região desejada
    create_s3_bucket(bucket_name, region)