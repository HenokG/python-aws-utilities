import os

import boto3
from os import walk
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

bucket = os.environ.get('AWS_BUCKET')
bulk_upload_dir = os.environ.get('BULK_UPLOAD_DIR')

def upload(file_name, key):
	s3 = boto3.client('s3')

	try:
		s3.upload_file(file_name, bucket, key)
	except ClientError as e:
		print('error while uploading file {e}')
		return False

	return True


def start_file_upload():
	for (_, __, files) in walk(bulk_upload_dir):
		for i, file in enumerate(files):
			print('uploading %s => %s' % ((i+1)/len(files), file))
			upload(bulk_upload_dir+'/'+file, file)



start_file_upload()