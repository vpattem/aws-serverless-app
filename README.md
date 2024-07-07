
# AWS Serverless Application

## Overview
This project demonstrates a serverless application using AWS services. The application consists of an API Gateway, AWS Lambda functions, and DynamoDB for data storage.

## Created By
**Venkatesh Pattem** - DevOps Engineer with a passion for serverless architecture and cloud computing.

## Prerequisites
- AWS CLI installed and configured
- AWS SAM CLI installed
- Python 3.8 or later
- Docker (for local testing)

## Project Structure
- `app/`: Contains the Lambda function code.
- `tests/`: Contains the unit tests for the application.
- `infra/`: Infrastructure as code (IaC) templates and deployment scripts.

## Getting Started

### 1. Clone the Repository
```sh
git clone https://github.com/vpattem/aws-serverless-app.git
cd aws-serverless-app
```

### 2. Set Up the Environment
Copy the example environment file and update it with your configuration.
```sh
cp .env.example .env
```
Open the `.env` file and update it with your AWS credentials and other necessary information:
```plaintext
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
TABLE_NAME=SampleDynamoDBTable
AWS_REGION=us-east-1
```

### 3. Install Dependencies
Install the dependencies for both the application and the infrastructure.
```sh
# Application dependencies
pip install -r app/requirements.txt

# Infrastructure dependencies
pip install -r infra/requirements.txt
```

### 4. Deploy the Application
Navigate to the `infra/` directory and deploy the application using the AWS SAM CLI.
```sh
cd infra
./deploy.sh
```

### 5. Test the Application
Run unit tests to ensure the application works correctly.
```sh
pytest tests/
```

## Deployment

### AWS SAM Template (template.yaml)
The `template.yaml` file in the `infra/` directory defines the AWS resources for the serverless application.

### Deploy Script (deploy.sh)
The `deploy.sh` script automates the deployment process.
```sh
#!/bin/bash

# Build the application
sam build

# Deploy the application
sam deploy --guided
```

## Lambda Function (app/app.py)
This is the main Lambda function code. It handles API requests and interacts with DynamoDB.

```python
import json
import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name=os.environ['AWS_REGION'])
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    
    # Example operation: Put item into DynamoDB
    response = table.put_item(
       Item={
            'id': '123',
            'data': 'Hello from Lambda!'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```

## Testing (tests/test_app.py)
Unit tests for the Lambda function.

```python
import pytest
from app import app

def test_lambda_handler():
    event = {}
    context = {}
    response = app.lambda_handler(event, context)
    assert response['statusCode'] == 200
    assert response['body'] == '"Hello from Lambda!"'
```

## Cleanup
To delete the resources created by the stack, run:
```sh
aws cloudformation delete-stack --stack-name your-stack-name
```

## Conclusion
This project provides a basic structure for an AWS serverless application with clear instructions on setup, deployment, and testing. Feel free to modify and expand it according to your needs.
