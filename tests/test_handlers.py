import json
import pytest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from handlers.get_items import lambda_handler as get_items_handler
from handlers.get_item import lambda_handler as get_item_handler  
from handlers.create_item import lambda_handler as create_item_handler
from handlers.update_item import lambda_handler as update_item_handler
from handlers.delete_item import lambda_handler as delete_item_handler

@patch('handlers.get_items.scan_all_items')
def test_get_items_success(mock_scan):
    mock_scan.return_value = [
        {'id': '1', 'name': 'Item 1'},
        {'id': '2', 'name': 'Item 2'}
    ]
    
    event = {}
    context = {}
    
    response = get_items_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['count'] == 2
    assert len(body['items']) == 2

@patch('handlers.get_items.scan_all_items')
def test_get_items_error(mock_scan):
    mock_scan.return_value = None
    
    event = {}
    context = {}
    
    response = get_items_handler(event, context)
    
    assert response['statusCode'] == 500
    body = json.loads(response['body'])
    assert 'error' in body

@patch('handlers.get_item.get_item_from_db')
def test_get_item_success(mock_get_item):
    mock_get_item.return_value = {'id': '123', 'name': 'Test Item'}
    
    event = {
        'pathParameters': {'id': '123'}
    }
    context = {}
    
    response = get_item_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['item']['id'] == '123'

@patch('handlers.get_item.get_item_from_db')
def test_get_item_not_found(mock_get_item):
    mock_get_item.return_value = None
    
    event = {
        'pathParameters': {'id': '123'}
    }
    context = {}
    
    response = get_item_handler(event, context)
    
    assert response['statusCode'] == 404
    body = json.loads(response['body'])
    assert 'error' in body

@patch('handlers.create_item.put_item_to_db')
def test_create_item_success(mock_put_item):
    mock_put_item.return_value = True
    
    event = {
        'body': json.dumps({
            'name': 'Test Item',
            'description': 'Test Description'
        })
    }
    context = {}
    
    response = create_item_handler(event, context)
    
    assert response['statusCode'] == 201
    body = json.loads(response['body'])
    assert body['message'] == 'Item created successfully'
    assert 'item' in body

def test_create_item_missing_name():
    event = {
        'body': json.dumps({
            'description': 'Test Description'
        })
    }
    context = {}
    
    response = create_item_handler(event, context)
    
    assert response['statusCode'] == 400
    body = json.loads(response['body'])
    assert 'error' in body

@patch('handlers.update_item.get_item_from_db')
@patch('handlers.update_item.put_item_to_db')
def test_update_item_success(mock_put_item, mock_get_item):
    mock_get_item.return_value = {
        'id': '123',
        'name': 'Original Name',
        'created_at': '2024-01-01T00:00:00'
    }
    mock_put_item.return_value = True
    
    event = {
        'pathParameters': {'id': '123'},
        'body': json.dumps({
            'name': 'Updated Name'
        })
    }
    context = {}
    
    response = update_item_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['message'] == 'Item updated successfully'

@patch('handlers.delete_item.get_item_from_db')
@patch('handlers.delete_item.delete_item_from_db')
def test_delete_item_success(mock_delete_item, mock_get_item):
    mock_get_item.return_value = {'id': '123', 'name': 'Test Item'}
    mock_delete_item.return_value = True
    
    event = {
        'pathParameters': {'id': '123'}
    }
    context = {}
    
    response = delete_item_handler(event, context)
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert 'deleted successfully' in body['message']