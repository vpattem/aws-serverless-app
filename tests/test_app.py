import pytest
from app import app

def test_lambda_handler():
    event = {}
    context = {}
    response = app.lambda_handler(event, context)
    assert response['statusCode'] == 200
    assert response['body'] == '"Hello from Lambda!"'