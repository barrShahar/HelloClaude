import json
import uuid
import os
from datetime import datetime
from src.utils import create_response, create_error_response, put_item_to_db
import anthropic

def generate_story(name, description):
    """Generate a short story using Anthropic API"""
    try:
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            return description  # Fallback to original description
        
        client = anthropic.Anthropic(api_key=api_key)
        
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=50,
            system="Write 1-2 sentence stories.",
            messages=[{
                "role": "user", 
                "content": f"{name}: {description}"
            }]
        )
        
        return message.content[0].text.strip()
        
    except Exception as e:
        print(f"Error generating story: {e}")
        return description  # Fallback to original description

def lambda_handler(event, context):
    try:
        if not event.get('body'):
            return create_error_response(400, "Request body is required")
        
        body = json.loads(event['body'])
        
        if not body.get('name'):
            return create_error_response(400, "Item name is required")
        
        # Generate story from name and description
        original_description = body.get('description', '')
        story_description = generate_story(body['name'], original_description)
        
        item = {
            'id': str(uuid.uuid4()),
            'name': body['name'],
            'description': story_description,
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