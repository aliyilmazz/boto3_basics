## Simple boto3 demonstration

In `bototest.py` you can find basic boto3 operations, such as:

- list buckets
- create bucket

inside a bucket,
- list files
- filter files
- upload/download files
- rename files
- delete files



Usage:


```
pip3 install boto3
python3 bototest.py <flags>
```

flags:
-monitorall: shows all files inside bucket named 'test_bucket_uuid' within module.
-deleteall: deletes all files inside bucket named 'test_bucket_uuid' within module.
