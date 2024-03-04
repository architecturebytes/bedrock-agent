# Bedrock Agent Tutorial

Refer YouTube Video: https://www.youtube.com/watch?v=6O9DqCrInvw 

**BytesCommerce/BytesCommerceFunction**<br>
This lambda function is configured in Action Group.

**BytesCommerce/BytesCommerceSchema.json**<br>
This is the Open API Schema configured in Action Group.

**BytesCommerce/InvokeAgentBytesCommerce**<br>
This is a lambda function to invoke the BytesCommerce Agent programmatically.<br>
If you don't plan to invoke the Agent programmatically, you can ignore it.<br>
You must use a version of boto3 that supports bedrock-agent-runtime (eg. version 1.34.49). <br>

Check boto3 version in a lambda function:<br>
`print(boto3.__version__)`<br>
`print(botocore.__version__)`

To use latest version of boto3 with your lambda function you can follow these steps:<br>
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
