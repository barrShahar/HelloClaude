from utils import create_response, create_error_response, get_item_from_db, delete_item_from_db

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']
        
        if not item_id:
            return create_error_response(400, "Item ID is required")
        
        existing_item = get_item_from_db(item_id)
        if existing_item is None:
            return create_error_response(404, f"Item with ID '{item_id}' not found")
        
        success = delete_item_from_db(item_id)
        
        if not success:
            return create_error_response(500, "Failed to delete item")
        
        return create_response(200, {
            'message': f'Item with ID {item_id} deleted successfully'
        })
        
    except KeyError:
        return create_error_response(400, "Item ID is required in path parameters")
    except Exception as e:
        print(f"Unexpected error: {e}")
        return create_error_response(500, "Internal server error")