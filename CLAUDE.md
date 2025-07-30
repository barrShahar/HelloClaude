# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a serverless CRUD API built with AWS SAM (Serverless Application Model) that provides REST endpoints to manage items in a DynamoDB table. The project demonstrates AWS Lambda functions, API Gateway integration, and infrastructure-as-code deployment.

## Development Commands

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Build the SAM application
sam build

# Start local API Gateway
sam local start-api

# Test individual Lambda functions locally
sam local invoke GetItemsFunction
sam local invoke CreateItemFunction --event events/create-item.json
```

### Testing
```bash
# Run unit tests
python -m pytest tests/ -v

# Run tests with coverage
python -m pytest tests/ --cov=src --cov-report=html
```

### Deployment
```bash
# Deploy to AWS (guided first-time setup)
sam deploy --guided

# Deploy with saved parameters
sam deploy

# Delete the stack
sam delete
```

## Architecture

### Directory Structure
- `src/handlers/` - Lambda function handlers for each API endpoint
- `src/utils.py` - Shared utilities for DynamoDB operations and response formatting
- `frontend/` - React frontend application with components and API service
- `template.yaml` - SAM template defining AWS resources
- `.github/workflows/deploy.yml` - CI/CD pipeline for automated deployment

### AWS Resources
- **DynamoDB Table** (`ItemsTable`) - Stores items with `id` as primary key
- **Lambda Functions** - Five functions handling CRUD operations:
  - `GetItemsFunction` - GET /items (list all items)
  - `GetItemFunction` - GET /items/{id} (get specific item)
  - `CreateItemFunction` - POST /items (create new item)
  - `UpdateItemFunction` - PUT /items/{id} (update existing item)
  - `DeleteItemFunction` - DELETE /items/{id} (delete item)
- **API Gateway** - REST API exposing Lambda functions as HTTP endpoints

### Data Model
Items have the following structure:
```json
{
  "id": "uuid",
  "name": "string (required)",
  "description": "string (optional)",
  "tags": ["array of strings (optional)"],
  "created_at": "ISO datetime",
  "updated_at": "ISO datetime"
}
```

### GitHub Actions CI/CD
The workflow includes:
- Testing on pull requests and main branch pushes
- Automated deployment to development environment on main branch
- Manual approval required for production deployment
- Requires AWS credentials configured as GitHub secrets

## Frontend Development

The project includes a React frontend in the `frontend/` directory:

```bash
# Install frontend dependencies
cd frontend && npm install

# Configure API URL
cp .env.example .env
# Edit .env: REACT_APP_API_URL=https://your-api-gateway-url

# Start development server
npm start
```

The frontend provides a complete web interface for the CRUD API with:
- Form to create/edit items with name, description, and tags
- Card-based layout showing all items
- Edit and delete actions for each item
- Real-time updates and error handling
- Responsive design for mobile and desktop

## Required GitHub Secrets
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `AWS_ACCOUNT_ID`