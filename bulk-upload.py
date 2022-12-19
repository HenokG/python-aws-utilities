import boto3
from os import walk

from botocore.exceptions import ClientError

bucket = 'employee-documents-for-bulk-download-test'

def upload(file_name, key):
	s3 = boto3.client('s3')

	try:
		s3.upload_file(file_name, bucket, key)
	except ClientError as e:
		print('error while uploading file {e}')
		return False

	return True


def start_file_upload():
	for (_, __, files) in walk('bulk-files'):
		for i, file in enumerate(files):
			print('uploading %s => %s' % (i/len(files), file))
			upload('bulk-files/'+file, file)



start_file_upload()