import json


THRESHOLD = .93


def lambda_handler(event, context):

    # Grab the inferences from the event
    event = json.loads(event['body'])
    print(type(event))
    
    inferences = json.loads(event['inferences'])
    
    inference = [float(x) for x in inferences]

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = False
    for i in inference:
        if THRESHOLD < i:
            meets_threshold = True
    

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
