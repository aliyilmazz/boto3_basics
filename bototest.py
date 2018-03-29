import boto3
import sys

session = boto3.session.Session()

s3 = session.resource(
    service_name='s3',
    aws_access_key_id="12345",
    aws_secret_access_key ="12345678",
    endpoint_url='http://10.6.1.31:9000'
)

test_bucket_uuid = "60aade06-2907-11e8-a892-d4c9ef52f9c6"

if __name__=='__main__':

    if len(sys.argv) > 1:
        if sys.argv[1] == '-monitorall':
            target_bucket = s3.Bucket(test_bucket_uuid)
            print("listing ALL files under bucket %s" % test_bucket_uuid)
            for myobject in target_bucket.objects.all():
                print(myobject.key)
            print("done listing!")
        elif sys.argv[1] == '-deleteall':
            target_bucket = s3.Bucket(test_bucket_uuid)
            print("deleting ALL files under bucket %s" % target_bucket)
            for myobject in target_bucket.objects.filter(Prefix=''):
                s3.Object(test_bucket_uuid, myobject.key).delete()
            print("done deleting!")
        else:
            print("Invalid parameter. Available Commands:")
            print("$python3 redistest.py -monitorall: Monitors all entries in redis.")
            print("$python3 redistest.py -deleteall: Deletes all entries in redis.")

    else:
        print("Error: No parameters given. Available Commands:")
        print("$python3 redistest.py -monitorall: Monitors all entries in redis.")
        print("$python3 redistest.py -deleteall: Deletes all entries in redis.")


# # --- 1. list buckets ---
# print("listing buckets start")
# for bucket in s3.buckets.all():
#     print(bucket.name)
# print("listing buckets end")
# # -----------------------


# # --- 2. list files inside a bucket ---
# target_bucket = s3.Bucket('60aade06-2907-11e8-a892-d4c9ef52f9c6')
# print("listing files under bucket %s" % target_bucket)
# for myobject in target_bucket.objects.filter(Prefix="operation"):
#     print(myobject.key)
# print("done listing!")
# # -------------------------------------


# # --- 2-1. delete files inside a bucket, starting with test_output ---
# target_bucket = s3.Bucket('donotdeletethisbucket')
# print("deleting files under bucket %s" % target_bucket)
# for myobject in target_bucket.objects.filter(Prefix='test_output'):
#     s3.Object('donotdeletethisbucket', myobject.key).delete()
# print("done deleting!")
# # -------------------------------------


# # --- 3. create bucket ---
# try:
#     s3.create_bucket(Bucket='donotdeletethisbucket')
# except Exception as e:
#     print("Error while creating bucket: %s" % e)
# # ------------------------


# # --- 4. upload file ---
# upload_from = "/home/yilmazali/workspace/video_splitter/test_video/birdakikalikvideo.wmv"
# upload_to = "birdakikalikvideo.wmv"
# print("Uploading started, please wait...")
# s3.Bucket('donotdeletethisbucket').upload_file(upload_from, upload_to)
# print("Upload complete!")
# # ----------------------


# # --- 4. download file ---
# download_from = "crowdflower_contents.tar.gz"
# download_to = "/home/yilmazali/crowdflower_contents.tar.gz"
# print("Downloading file...")
# s3.Bucket('donotdeletethisbucket').download_file(download_from, download_to)
# print("Download complete! File is available at %s" % download_to)
# # ------------------------


# # --- 5. rename file ---
# s3.Object('my_bucket','my_file_new').copy_from(CopySource='my_bucket/my_file_old')
# s3.Object('my_bucket','my_file_old').delete()
# # ----------------------

