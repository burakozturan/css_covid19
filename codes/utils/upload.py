import boto3


class FileOperations(object):
    def __init__(self):
        self.client = boto3.client('s3',
                                   aws_access_key_id="AKIAIQ67PJWQISOVKMKQ",
                                   aws_secret_access_key="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"
                                   )

    def upload_file(self, file_name, bucket, object_name):
        self.client.upload_file(file_name, bucket, object_name)
