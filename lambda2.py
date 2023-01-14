import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer
from sagemaker.predictor import Predictor
import boto3

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2023-01-13-17-18-55-192'

s3 = boto3.client('s3')

def lambda_handler(event, context):

    
    # Decode the image data
    event = event['body']
    image = base64.b64decode(event['image_data'])

        
    runtime = boto3.client('sagemaker-runtime')

    # Make a prediction:
    response = runtime.invoke_endpoint(
                                        EndpointName=ENDPOINT,
                                        Body=image
                                        )

    inferences = response["Body"].read().decode("utf-8")

    # We return the data back to the Step Function    
    event["inferences"] = inferences 
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
