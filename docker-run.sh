#!/bin/bash
REG_ID=$(aws cloudformation describe-stacks --stack-name serverless-apps-fargate-example-ecr --query "Stacks[0].Outputs[?OutputKey=='RegistryName'] | [0].OutputValue" --output text)
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
docker run -d -p 8080:80 ${ACCOUNT_ID}.dkr.ecr.eu-west-1.amazonaws.com/${REG_ID}:latest