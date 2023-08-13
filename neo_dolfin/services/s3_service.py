import boto3
import datetime

class S3Service():
    ''' This is a service for getting objects from an S3 Bucket, with the option to get a specific object
        or to get the last modified'''
    def get_specified_object(bucket_name, object_name):
        # Get a specified object from a specified s3 bucket
        s3_client = boto3.client('s3')

        response = s3_client.get_object(Bucket = bucket_name, Key = object_name)
        
        return response['Body'].read()

    def set_object(data, bucket_name, username, file_extension):
        # Creates a new object, combining the user's username, the current time and the file extension to provide a unique filename
        s3_client = boto3.client('s3')
        current_time = datetime.datetime.now().strftime("%m%d%Y%H%M%S")

        response = s3_client.put_object(Body = data, Bucket = bucket_name, Key = username + current_time + file_extension)

        return response['HTTPStatusCode']

    def get_latest(bucket_name, username):
        # modified from https://stackoverflow.com/questions/45375999/how-to-download-the-latest-file-of-an-s3-bucket-using-boto3
        get_lateset_object = lambda obj: int(obj['LastModified'].strftime('%S'))

        s3 = boto3.client('s3')
        objects = s3.list_objects(Bucket = bucket_name)['Contents']
        
        return [obj['Key'] for obj in sorted(objects, key = get_latest_object)][0]

    def create_bucket(bucket_name, configuration_json):
        # This method has many more properties that we can set. Worth discussing the merit of including these in our implementation
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html
        s3 = boto3.client('s3')

        response = s3.create_bucket(Bucket = bucket_name, CreateBucketConfiguration = configuration_json)

        return response['HttpStatusCode']

    def delete_bucket(bucket_name):
        # Delete a specific s3 bucket
        s3 = boto3.client('s3')

        response = s3.delete_bucket(Bucket = bucket_name)

        return response['HttpStatusCode']

    