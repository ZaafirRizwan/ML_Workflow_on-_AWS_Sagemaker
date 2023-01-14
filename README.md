# Project: Building ML Workflow For Scones Unlimited On Amazon SageMaker

Data Staging/ETL:

1. Extracting data from the hosting service.
2. Exploring and Transforming into the correct shape and format
3. Loading data to S3.

Training Image Classification Model:

1. Creating Estimator Object
2. Setting Hyperparameters and Model Inputs
3. Calling .fit method on Model.

Deploying Model: 
1. Creating Endpoint and Deploying the model to that Endpoint.
2. Invoking Endpoint For Predicting Test Data

Draft Lambdas(python=3.8) and Step Function Workflow:
1. Lambda1.py is responsible for data generation.
2. Lambda2.py is responsible for image classification.
3. Lambda3.py is responsible for filtering out low-confidence inferences
