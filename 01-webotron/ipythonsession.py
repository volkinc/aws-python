# coding: utf-8
import boto3
session = boto3.Session(profile_name="alexander.volkov")
s3=session.resource('s3')

    
    
#new_bucket = s3.create_bucket(Bucket="volkov_third")
