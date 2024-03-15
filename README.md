# Bedrock Agent Tutorial

Refer YouTube Video: https://www.youtube.com/watch?v=6O9DqCrInvw 

**BytesCommerce/BytesCommerceFunction.py**<br>
This lambda function is configured in Action Group.

**BytesCommerce/BytesCommerceSchema.json**<br>
This is the Open API Schema configured in Action Group.

**BytesCommerce/kb-data**<br>
Here you will find two (knowledge base) files used in the demo:<br>
ProductCatalog.csv, ProductDescriptions.pdf

**BytesCommerce/InvokeAgentBytesCommerce.py**<br>
This is a lambda function to invoke the BytesCommerce Agent programmatically.<br>
If you don't plan to invoke the Agent programmatically, you can ignore it.<br>
You must use a version of boto3 that supports bedrock-agent-runtime (eg. version 1.34.49). <br>

Check boto3 version in a lambda function:<br>
`print(boto3.__version__)`<br>
`print(botocore.__version__)`

To use latest version of boto3 with your lambda function (assuming it is not available via AWS Console by default) you can follow these steps to include it via a Layer:<br>
1. Open Cloud Shell in AWS Console OR any shell/command-line environment with AWS configured.<br>
2. Create a new directory:<br>
  `LIB_DIR=boto3-mylayer/python`<br>
  `mkdir -p $LIB_DIR`<br>
3. Install the boto3 library to LIB_DIR by running the following command:<br>
  `pip3 install boto3 -t $LIB_DIR`<br>
4. Zip all the dependencies to /tmp/boto3-mylayer.zip by running the following command:<br>
  `cd boto3-mylayer`<br>
  `zip -r /tmp/boto3-mylayer.zip .`<br>
5. Publish the layer by running the following command:<br>
  `aws lambda publish-layer-version --layer-name boto3-mylayer --zip-file fileb:///tmp/boto3-mylayer.zip`<br>
  The command returns the new layer's Amazon Resource Name (ARN), similar to the following one:<br>
  `arn:aws:lambda:region:$ACC_ID:layer:boto3-mylayer:1`<br>
6. Once the layer is created, you can go to AWS Console > lambda function (InvokeAgentBytesCommerce) and attach the layer to it.<br>
   OR use the following command to attach the layer to your lambda function.<br>
   `aws lambda update-function-configuration --function-name <name-of-your-lambda i.e InvokeAgentBytesCommerce> --layers <layer ARN as seen above>`

Within your lambda function you can print boto3 version to verify:<br>
`print(boto3.__version__)`<br>
`print(botocore.__version__)`

**How to gain access to Foundation Model**<br>
In AWS Console > Bedrock > Foundation Models > Base Model > Model Access > Manage Model Access > Select the Models you need access to and hit Save.

**Cleanup**<br>
Delete/release all resources related to Bedrock Agent - If you no longer need the Agent<br>
- Agent (Actions and Knowledge Bases)<br>
- OpenSearch Serverless Collection - This must be explicitly deleted. Although it is created automatically during Knowledge Base Creation - it doesn't get deleted automatically on Knowledge Base deletion<br>
- Unsubscribe(Remove Access) to any AWS Bedrock Models (for eg. Anthropic Claude)
- Lambda function(s) & S3 bucket(s)
- Any other related resources you may have created.
