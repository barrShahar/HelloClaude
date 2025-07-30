# HelloClaude Frontend

React frontend for the HelloClaude AWS SAM CRUD API.

## Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Configure API URL**
   ```bash
   cp .env.example .env
   # Edit .env and set your API Gateway URL
   ```

3. **Start development server**
   ```bash
   npm start
   ```

4. **Build for production**
   ```bash
   npm run build
   ```

## Features

- ✅ Create new items with name, description, and tags
- ✅ View all items in a clean card layout  
- ✅ Edit existing items inline
- ✅ Delete items with confirmation
- ✅ Responsive design for mobile and desktop
- ✅ Error handling and loading states
- ✅ Real-time updates after CRUD operations

## Configuration

Set the `REACT_APP_API_URL` environment variable to your AWS API Gateway URL:

```
REACT_APP_API_URL=https://abc123.execute-api.us-east-1.amazonaws.com/Prod
```

## Usage

1. The app loads all items on startup
2. Use the form on the left to create new items
3. Click edit (✏️) to modify an item
4. Click delete (🗑️) to remove an item
5. All changes sync with your AWS backend

## Components

- `App.js` - Main application with state management
- `ItemForm.js` - Form for creating/editing items
- `ItemList.js` - Container for all item cards
- `ItemCard.js` - Individual item display with actions
- `services/api.js` - API service for backend communication