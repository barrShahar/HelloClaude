import json
import os
import boto3
from botocore.exceptions import ClientError
from typing import Dict, Any, Optional

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'ItemsTable')
table = dynamodb.Table(table_name)

def create_response(status_code: int, body: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps(body)
    }

def create_error_response(status_code: int, message: str) -> Dict[str, Any]:
    return create_response(status_code, {'error': message})

def get_item_from_db(item_id: str) -> Optional[Dict[str, Any]]:
    try:
        response = table.get_item(Key={'id': item_id})
        return response.get('Item')
    except ClientError as e:
        print(f"Error getting item {item_id}: {e}")
        return None

def put_item_to_db(item: Dict[str, Any]) -> bool:
    try:
        table.put_item(Item=item)
        return True
    except ClientError as e:
        print(f"Error putting item: {e}")
        return False

def delete_item_from_db(item_id: str) -> bool:
    try:
        table.delete_item(Key={'id': item_id})
        return True
    except ClientError as e:
        print(f"Error deleting item {item_id}: {e}")
        return False

def scan_all_items() -> Optional[list]:
    try:
        response = table.scan()
        return response.get('Items', [])
    except ClientError as e:
        print(f"Error scanning table: {e}")
        return None