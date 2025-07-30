import sys
import os
import json
import uuid
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import create_response, create_error_response, put_item_to_db

def lambda_handler(event, context):
    try:
        if not event.get('body'):
            return create_error_response(400, "Request body is required")
        
        body = json.loads(event['body'])
        
        if not body.get('name'):
            return create_error_response(400, "Item name is required")
        
        item = {
            'id': str(uuid.uuid4()),
            'name': body['name'],
            'description': body.get('description', ''),
            'created_at': datetime.utcnow().isoformat(),
            'updated_at': datetime.utcnow().isoformat()
        }
        
        if body.get('tags'):
            item['tags'] = body['tags']
        
        success = put_item_to_db(item)
        
        if not success:
            return create_error_response(500, "Failed to create item")
        
        return create_response(201, {
            'message': 'Item created successfully',
            'item': item
        })
        
    except json.JSONDecodeError:
        return create_error_response(400, "Invalid JSON in request body")
    except Exception as e:
        print(f"Unexpected error: {e}")
        return create_error_response(500, "Internal server error")