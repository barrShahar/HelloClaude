const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://your-api-gateway-url.execute-api.us-east-1.amazonaws.com/Prod';

class ApiService {
  async makeRequest(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    };

    try {
      const response = await fetch(url, config);
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.error || `HTTP error! status: ${response.status}`);
      }
      
      return data;
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }

  async getAllItems() {
    return this.makeRequest('/items');
  }

  async getItem(id) {
    return this.makeRequest(`/items/${id}`);
  }

  async createItem(item) {
    return this.makeRequest('/items', {
      method: 'POST',
      body: JSON.stringify(item),
    });
  }

  async updateItem(id, item) {
    return this.makeRequest(`/items/${id}`, {
      method: 'PUT',
      body: JSON.stringify(item),
    });
  }

  async deleteItem(id) {
    return this.makeRequest(`/items/${id}`, {
      method: 'DELETE',
    });
  }
}

export default new ApiService();