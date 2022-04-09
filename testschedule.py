# msg="hello"
# print(msg)
import os
from pprint import pprint
from turtle import clear
from google.cloud import storage
import schedule
import time
from datetime import datetime

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'assam2-roofing-storage-4fbb500ca671.json'

storage_client = storage.Client()


bucket_name = 'assam-roofing1'
bucket = storage_client.bucket(bucket_name)

vars(bucket)

# bucket = storage_client.bucket(bucket_name)
# bucket.storage_class = 'COLDLINE' # Archive | Nearline | Standard
# bucket.location = 'US' # Taiwan
# bucket = storage_client.create_bucket(bucket) # returns Bucket object

# print(vars(bucket))

# """
# Get Bucket
# """
my_bucket = storage_client.get_bucket(bucket_name)

# print(vars(my_bucket))

# """
# Upload File
# """
def upload_to_bucket():
    
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    blob_name='test/backupfile3'+date
    file_path=r''
    file_path=os.path.join(file_path,'sanu.xlx')
    bucket_name='assam-roofing1'
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        print('done')
        return True
    except Exception as e:
        print(e)
        return False


#file_path=r'D:\sanu_2021\python'

schedule.every(50).seconds.do(upload_to_bucket)
#schedule.every(50).minutes.do(upload_to_bucket)
while True:
    schedule.run_pending()
    time.sleep(1)


    