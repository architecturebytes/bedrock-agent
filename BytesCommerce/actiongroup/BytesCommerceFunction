import json

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    
    api_path = event['apiPath']
    
    if api_path == "/GetProductInventory":
        
        # Product Inventory data retrieval (from database or another service) code would go here.
        response_data = [
			{"Product Id": "P001", "Product Name": "ThunderBlast", "Quantity": 297},
			{"Product Id": "P002", "Product Name": "SilverSurge", "Quantity": 0},
			{"Product Id": "P003", "Product Name": "BlueRider", "Quantity": 463},
			{"Product Id": "P004", "Product Name": "CloudRunner", "Quantity": 904},
			{"Product Id": "P005", "Product Name": "GoldenGlimmer", "Quantity": 440},
			{"Product Id": "P006", "Product Name": "BlazeFusion", "Quantity": 608},
			{"Product Id": "P007", "Product Name": "NeptuneWave", "Quantity": 0},
			{"Product Id": "P008", "Product Name": "GreenExplorer", "Quantity": 791},
			{"Product Id": "P009", "Product Name": "ShadowSprint", "Quantity": 384},
			{"Product Id": "P010", "Product Name": "TimelessElegance", "Quantity": 707},
			{"Product Id": "P011", "Product Name": "ThunderStrike", "Quantity": 971},
			{"Product Id": "P012", "Product Name": "SkyBlaze", "Quantity": 172},
			{"Product Id": "P013", "Product Name": "GreenExplorer", "Quantity": 936},
			{"Product Id": "P014", "Product Name": "FireFlyer", "Quantity": 732},
			{"Product Id": "P015", "Product Name": "OrangeHorizon", "Quantity": 0},
			{"Product Id": "P016", "Product Name": "BlazeFusion", "Quantity": 642},
			{"Product Id": "P017", "Product Name": "SilverSurge", "Quantity": 31},
			{"Product Id": "P018", "Product Name": "BlueExplorer", "Quantity": 674},
			{"Product Id": "P019", "Product Name": "BlackJet", "Quantity": 203},
			{"Product Id": "P020", "Product Name": "GoldRush", "Quantity": 698}
		] 
    elif api_path == "/RestockProduct":
        
        # Product Restock Order creation code would go here.
        response_data = {"status": "Success"}
    else:
        response_data = {"message": "Unknwon API Path"}
        

    #response_body = {
    #    'items': items
    #}
    
    response_body = {
        'application/json': {
            'body': json.dumps(response_data)
        }
    }
    
    action_response = {
        'actionGroup': event['actionGroup'],
        'apiPath': event['apiPath'],
        'httpMethod': event['httpMethod'],
        'httpStatusCode': 200,
        'responseBody': response_body
    }
    
    session_attributes = event['sessionAttributes']
    prompt_session_attributes = event['promptSessionAttributes']
    
    api_response = {
        'messageVersion': '1.0', 
        'response': action_response,
        'sessionAttributes': session_attributes,
        'promptSessionAttributes': prompt_session_attributes
    }
    
    print("Returning API response: " + json.dumps(api_response))
        
    return api_response
