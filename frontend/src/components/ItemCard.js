import React from 'react';

function ItemCard({ item, onEdit, onDelete }) {
  const formatDate = (dateString) => {
    if (!dateString) return '';
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="item-card">
      <div className="item-header">
        <h3 className="item-name">{item.name}</h3>
        <div className="item-actions">
          <button 
            onClick={() => onEdit(item)}
            className="btn btn-edit"
            title="Edit item"
          >
            ✏️
          </button>
          <button 
            onClick={() => onDelete(item.id)}
            className="btn btn-delete"
            title="Delete item"
          >
            🗑️
          </button>
        </div>
      </div>

      {item.description && (
        <p className="item-description">{item.description}</p>
      )}

      {item.tags && item.tags.length > 0 && (
        <div className="item-tags">
          {item.tags.map((tag, index) => (
            <span key={index} className="tag">
              {tag}
            </span>
          ))}
        </div>
      )}

      <div className="item-meta">
        <small className="item-id">ID: {item.id}</small>
        {item.created_at && (
          <small className="item-date">
            Created: {formatDate(item.created_at)}
          </small>
        )}
        {item.updated_at && item.updated_at !== item.created_at && (
          <small className="item-date">
            Updated: {formatDate(item.updated_at)}
          </small>
        )}
      </div>
    </div>
  );
}

export default ItemCard;