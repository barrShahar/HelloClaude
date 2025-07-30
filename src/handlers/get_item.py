from src.utils import create_response, create_error_response, get_item_from_db

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']
        
        if not item_id:
            return create_error_response(400, "Item ID is required")
        
        item = get_item_from_db(item_id)
        
        if item is None:
            return create_error_response(404, f"Item with ID '{item_id}' not found")
        
        return create_response(200, {'item': item})
        
    except KeyError:
        return create_error_response(400, "Item ID is required in path parameters")
    except Exception as e:
        print(f"Unexpected error: {e}")
        return create_error_response(500, "Internal server error")