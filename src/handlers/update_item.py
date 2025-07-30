import json
from datetime import datetime
from src.utils import create_response, create_error_response, get_item_from_db, put_item_to_db

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']
        
        if not item_id:
            return create_error_response(400, "Item ID is required")
        
        if not event.get('body'):
            return create_error_response(400, "Request body is required")
        
        body = json.loads(event['body'])
        
        existing_item = get_item_from_db(item_id)
        if existing_item is None:
            return create_error_response(404, f"Item with ID '{item_id}' not found")
        
        updated_item = existing_item.copy()
        
        if 'name' in body:
            updated_item['name'] = body['name']
        
        if 'description' in body:
            updated_item['description'] = body['description']
        
        if 'tags' in body:
            updated_item['tags'] = body['tags']
        
        updated_item['updated_at'] = datetime.utcnow().isoformat()
        
        success = put_item_to_db(updated_item)
        
        if not success:
            return create_error_response(500, "Failed to update item")
        
        return create_response(200, {
            'message': 'Item updated successfully',
            'item': updated_item
        })
        
    except KeyError:
        return create_error_response(400, "Item ID is required in path parameters")
    except json.JSONDecodeError:
        return create_error_response(400, "Invalid JSON in request body")
    except Exception as e:
        print(f"Unexpected error: {e}")
        return create_error_response(500, "Internal server error")