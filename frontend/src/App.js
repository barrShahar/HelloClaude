import React, { useState, useEffect } from 'react';
import './App.css';
import ItemList from './components/ItemList';
import ItemForm from './components/ItemForm';
import ApiService from './services/api';

function App() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingItem, setEditingItem] = useState(null);

  useEffect(() => {
    loadItems();
  }, []);

  const loadItems = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await ApiService.getAllItems();
      setItems(response.items || []);
    } catch (err) {
      setError('Failed to load items: ' + err.message);
      console.error('Error loading items:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateItem = async (itemData) => {
    try {
      setError(null);
      const response = await ApiService.createItem(itemData);
      setItems(prev => [...prev, response.item]);
      return true;
    } catch (err) {
      setError('Failed to create item: ' + err.message);
      return false;
    }
  };

  const handleUpdateItem = async (id, itemData) => {
    try {
      setError(null);
      const response = await ApiService.updateItem(id, itemData);
      setItems(prev => prev.map(item => 
        item.id === id ? response.item : item
      ));
      setEditingItem(null);
      return true;
    } catch (err) {
      setError('Failed to update item: ' + err.message);
      return false;
    }
  };

  const handleDeleteItem = async (id) => {
    if (!window.confirm('Are you sure you want to delete this item?')) {
      return;
    }

    try {
      setError(null);
      await ApiService.deleteItem(id);
      setItems(prev => prev.filter(item => item.id !== id));
    } catch (err) {
      setError('Failed to delete item: ' + err.message);
    }
  };

  const handleEditItem = (item) => {
    setEditingItem(item);
  };

  const handleCancelEdit = () => {
    setEditingItem(null);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>HelloClaude Item Manager</h1>
        <p>AWS SAM CRUD API Frontend</p>
      </header>

      <main className="App-main">
        {error && (
          <div className="error-message">
            {error}
            <button onClick={() => setError(null)}>×</button>
          </div>
        )}

        <section className="form-section">
          <h2>{editingItem ? 'Edit Item' : 'Create New Item'}</h2>
          <ItemForm
            item={editingItem}
            onSubmit={editingItem ? 
              (data) => handleUpdateItem(editingItem.id, data) : 
              handleCreateItem
            }
            onCancel={editingItem ? handleCancelEdit : null}
          />
        </section>

        <section className="items-section">
          <h2>Items ({items.length})</h2>
          {loading ? (
            <div className="loading">Loading items...</div>
          ) : (
            <ItemList
              items={items}
              onEdit={handleEditItem}
              onDelete={handleDeleteItem}
            />
          )}
        </section>
      </main>
    </div>
  );
}

export default App;