import json
import boto3
from urllib.parse import unquote_plus # to remove '+' sign from urls



s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')

def label_finder_function(bucket,key):
    response = rekognition.detect_labels(
        Image = {
            'S3Object':{
                'Bucket':bucket,
                'Name': key,
                
            }
        },
        
    )
    
    print("******** Response***********")
    print("\n")
    print(response)
    
    labels = [ label['Name'] for label in response['Labels']]
    print("labels")
    print("\n")
    print(labels)
    
    return label
    
    
    
    
    
def lambda_handler(event, context):
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
    # bucket = event['Records'][0]['s3']['bucket']['name']
    # key    = event['Records'][0]['s3']['bucket']['key']
    
    print(bucket)
    print(key)
    
    labels_found = label_finder_function(bucket,key)
    
    return labels_found
    
