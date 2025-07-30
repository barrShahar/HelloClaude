import React, { useState, useEffect } from 'react';

function ItemForm({ item, onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    tags: ''
  });
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    if (item) {
      setFormData({
        name: item.name || '',
        description: item.description || '',
        tags: item.tags ? item.tags.join(', ') : ''
      });
    } else {
      setFormData({
        name: '',
        description: '',
        tags: ''
      });
    }
  }, [item]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!formData.name.trim()) {
      alert('Item name is required');
      return;
    }

    setSubmitting(true);

    const submitData = {
      name: formData.name.trim(),
      description: formData.description.trim(),
    };

    if (formData.tags.trim()) {
      submitData.tags = formData.tags
        .split(',')
        .map(tag => tag.trim())
        .filter(tag => tag.length > 0);
    }

    const success = await onSubmit(submitData);
    
    if (success && !item) {
      setFormData({
        name: '',
        description: '',
        tags: ''
      });
    }
    
    setSubmitting(false);
  };

  return (
    <form onSubmit={handleSubmit} className="item-form">
      <div className="form-group">
        <label htmlFor="name">Name *</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
          disabled={submitting}
          placeholder="Enter item name"
        />
      </div>

      <div className="form-group">
        <label htmlFor="description">Description</label>
        <textarea
          id="description"
          name="description"
          value={formData.description}
          onChange={handleChange}
          disabled={submitting}
          placeholder="Enter item description"
          rows="3"
        />
      </div>

      <div className="form-group">
        <label htmlFor="tags">Tags</label>
        <input
          type="text"
          id="tags"
          name="tags"
          value={formData.tags}
          onChange={handleChange}
          disabled={submitting}
          placeholder="Enter tags separated by commas"
        />
      </div>

      <div className="form-actions">
        <button 
          type="submit" 
          disabled={submitting}
          className="btn btn-primary"
        >
          {submitting ? 'Saving...' : (item ? 'Update Item' : 'Create Item')}
        </button>
        
        {onCancel && (
          <button 
            type="button" 
            onClick={onCancel}
            disabled={submitting}
            className="btn btn-secondary"
          >
            Cancel
          </button>
        )}
      </div>
    </form>
  );
}

export default ItemForm;