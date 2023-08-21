from abc import ABC, abstractmethod

class IS3Service(ABC):
    ''' This is a service for getting objects from an S3 Bucket, with the option to get a specific object
        or to get the last modified'''
    @abstractmethod
    def get_specified_object(bucket_name, object_name):
        raise NotImplementedError

    @abstractmethod
    def set_object(data, bucket_name, username, file_extension):
        raise NotImplementedError

    @abstractmethod
    def get_latest(bucket_name, username):
        # modified from https://stackoverflow.com/questions/45375999/how-to-download-the-latest-file-of-an-s3-bucket-using-boto3
        raise NotImplementedError

    @abstractmethod
    def create_bucket(bucket_name, configuration_json = None):
        raise NotImplementedError

    @abstractmethod
    def delete_bucket(bucket_name):
        raise NotImplementedError

