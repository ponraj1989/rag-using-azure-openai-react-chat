import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

export const askQuestion = async (question, filters = {}) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/ask`, {
            question,
            filters,
        });
        return response.data;
    } catch (error) {
        console.error('Error asking question:', error);
        throw error;
    }
};