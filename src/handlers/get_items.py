import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import create_response, create_error_response, scan_all_items

def lambda_handler(event, context):
    try:
        items = scan_all_items()
        
        if items is None:
            return create_error_response(500, "Failed to retrieve items from database")
        
        return create_response(200, {
            'items': items,
            'count': len(items)
        })
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return create_error_response(500, "Internal server error")