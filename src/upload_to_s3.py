import boto3
import botocore
import os


def upload_file_to_s3(file_name, bucket_name, object_name=None, region='us-east-1'):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket_name: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :param region: AWS region where the bucket is located
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Create an S3 client
    s3_client = boto3.client('s3', region_name=region)

    # Check if the bucket exists
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} exists.")
    except botocore.exceptions.ClientError:
        # If a client error is thrown, then the bucket does not exist
        print(f"Bucket {bucket_name} does not exist. Creating bucket.")
        try:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
            print(f"Bucket {bucket_name} created.")
        except botocore.exceptions.ClientError as e:
            print(f"Error creating bucket: {e}")
            return False

    # Upload the file
    try:
        response = s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File {file_name} uploaded to {bucket_name}/{object_name}.")
        return True
    except botocore.exceptions.ClientError as e:
        print(f"Error uploading file: {e}")
        return False

# Example usage
if __name__ == "__main__":
    file_name = f"{os.environ.get('CLEANED_TABLE_NAME')}.csv"
    bucket_name = 'movie-etl'
    region = 'us-east-1'  # Specify your region
    upload_file_to_s3(file_name, bucket_name, region=region)