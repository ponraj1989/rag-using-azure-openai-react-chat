import React, { useState } from 'react';

const QuestionInput = ({ onSubmit }) => {
    const [question, setQuestion] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (question.trim()) {
            onSubmit(question);
            setQuestion('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask your question..."
                required
            />
            <button type="submit">Submit</button>
        </form>
    );
};

export default QuestionInput;