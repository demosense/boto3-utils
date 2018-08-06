import os
import zipfile
import shutil
from io import BytesIO

import boto3


class Boto3Utils:

    @staticmethod
    def download(folder_path, bucket, name, key, dest):
        # if does not exit, get it from s3
        if not os.path.exists(folder_path):
            print(f"Downloading {name} from: {bucket}")
            # if the temporary folder exists, delete it
            temp_dest_folder = os.path.join(dest, '_temp')
            if os.path.exists(temp_dest_folder):
                shutil.rmtree(temp_dest_folder)

            Boto3Utils.download_zip(bucket, name, temp_dest_folder)
            print("finishing")

            if os.path.exists(os.path.join(temp_dest_folder, key)):
                temp_dest_folder = os.path.join(temp_dest_folder, key)

            # atomic operation. The lambda can be interrupted before
            os.rename(temp_dest_folder, folder_path)
        else:
            print(f"No need to download {name}")

    @staticmethod
    def download_zip(bucket_name, obj_name, dest_folder):
        # add the extension if it's not there
        if not obj_name.endswith('.zip'):
            obj_name += '.zip'

        s3 = boto3.client('s3')
        zip_obj = s3.get_object(Bucket=bucket_name, Key=obj_name)['Body'].read()

        print(f"Done downloading {obj_name}")
        my_zipfile = zipfile.ZipFile(BytesIO(zip_obj), 'r')

        my_zipfile.extractall(dest_folder)

        print(f"Done unzipping {obj_name}")

    @staticmethod
    def download_dir(client, resource, dist, local, bucket):
        paginator = client.get_paginator('list_objects_v2')

        print(f"downloading {dist} in {local}")

        for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):

            if result.get('CommonPrefixes') is not None:
                for subdir in result.get('CommonPrefixes'):
                    Boto3Utils.download_dir(client, resource, subdir.get('Prefix'), local, bucket)
            if result.get('Contents') is not None:
                for file in result.get('Contents'):
                    key = file.get('Key')
                    file_name = local + key
                    path_dirname = os.path.dirname(file_name)

                    # print(f"key: {key} file: {file_name} path_dirname: {path_dirname}")

                    if not os.path.exists(path_dirname):
                        # print(f"mkdir {path_dirname}")
                        os.makedirs(path_dirname)

                    # print("before")

                    if not key.endswith("/"):
                        #print(f"d: {file_name}")
                        client.download_file(bucket, key, file_name)
                    # print("after")
