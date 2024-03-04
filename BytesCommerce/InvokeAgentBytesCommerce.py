import boto3
import botocore
from botocore.client import BaseClient
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    #print(boto3.__version__)
    #print(botocore.__version__)

    #TODO: Make sure region is correct below:
    region_name = "us-east-1"
    agent_id = "TODO: PROVIDE_AGENT_ID_HERE"
    agent_alias_id = "TODO: PROVIDE_AGENT_ALIAS_ID_HERE"

    # Maintain same session id across invocations for continued (continuous) conversation.
    # Or use a new random session id, for a new conversation.
    session_id = "s03"

    prompt = "Get list of all products"

    completion = ""
    traces = []
    
    config = botocore.config.Config(
        read_timeout=900,
        connect_timeout=900,
        retries={"max_attempts": 0}
    )

    try:
        bedrock_client = boto3.client(
            service_name="bedrock-agent-runtime",
            region_name=region_name,
            config=config
        )

        response = bedrock_client.invoke_agent(
            agentId=agent_id,
            agentAliasId=agent_alias_id,
            sessionId=session_id,
            inputText=prompt
        )

        for event in response.get("completion"):
            print(event)
            try:
                trace = event["trace"]
                traces.append(trace['trace'])
            except KeyError:
                chunk = event["chunk"]
                completion = completion + chunk["bytes"].decode()
            except Exception as e:
                print(e)

    except ClientError as e:
        print(e)

    return {
        "statusCode": 200,
        "body": {
            "response": completion,
            "traces": traces
        }
    }
