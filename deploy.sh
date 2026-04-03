#!/bin/bash
# Ce script permet de reconstruire toute l'infra d'un coup
awslocal ec2 run-instances --image-id ami-00000000 --count 1 --instance-type t2.micro
zip function.zip lambda_function.py
awslocal lambda create-function --function-name EC2Manager --zip-file fileb://function.zip --handler lambda_function.lambda_handler --runtime python3.9 --role arn:aws:iam::000000000000:role/admin-role
awslocal lambda create-function-url-config --function-name EC2Manager --auth-type NONE
awslocal apigateway create-deployment --rest-api-id y8dvirlymk --stage-name prod
