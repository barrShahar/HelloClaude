# HelloClaude - AWS SAM CRUD API

A serverless CRUD API built with AWS SAM (Serverless Application Model) that demonstrates:
- AWS Lambda functions with Python 3.12
- DynamoDB table operations 
- API Gateway REST endpoints
- Infrastructure-as-code with SAM templates
- GitHub Actions CI/CD pipeline

## Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Build and test locally**
   ```bash
   sam build
   sam local start-api
   ```

3. **Deploy to AWS**
   ```bash
   sam deploy --guided
   ```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/items` | List all items |
| GET | `/items/{id}` | Get specific item |
| POST | `/items` | Create new item |  
| PUT | `/items/{id}` | Update existing item |
| DELETE | `/items/{id}` | Delete item |

## Example Usage

**Create an item:**
```bash
curl -X POST https://your-api-url/items \
  -H "Content-Type: application/json" \
  -d '{"name": "My Item", "description": "Item description", "tags": ["tag1", "tag2"]}'
```

**Get all items:**
```bash
curl https://your-api-url/items
```

## Testing

Run unit tests:
```bash
python -m pytest tests/ -v
```

Test individual Lambda functions locally:
```bash
sam local invoke CreateItemFunction --event events/create-item.json
sam local invoke GetItemFunction --event events/get-item.json
```

## GitHub Actions Setup

Configure these secrets in your GitHub repository:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY` 
- `AWS_DEFAULT_REGION`
- `AWS_ACCOUNT_ID`

## Project Structure

```
├── src/                  # Backend Lambda functions
│   ├── handlers/         # Lambda function handlers
│   └── utils.py         # Shared utilities
├── frontend/            # React frontend application
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── services/    # API service layer
│   │   └── App.js      # Main application
│   └── package.json    # Frontend dependencies
├── tests/              # Backend unit tests
├── events/             # Sample events for local testing
├── template.yaml       # SAM template
└── .github/workflows/  # CI/CD pipeline
```

## Frontend Setup

The project includes a React frontend in the `frontend/` directory:

```bash
cd frontend
npm install
cp .env.example .env
# Edit .env with your API Gateway URL
npm start
```

The frontend provides a clean web interface to:
- Create, read, update, and delete items
- View items in organized cards with tags
- Edit items inline with form validation
- Handle errors and loading states gracefully# Pipeline test
