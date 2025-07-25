import React from 'react';

interface ResultDisplayProps {
    results: Array<{
        content: string;
        metadata: {
            filename: string;
            turbine_name: string;
            model: string;
            location: string;
            maintenance_type: string;
        };
    }>;
}

const ResultDisplay: React.FC<ResultDisplayProps> = ({ results }) => {
    return (
        <div className="result-display">
            {results.length === 0 ? (
                <p>No results found.</p>
            ) : (
                results.map((result, index) => (
                    <div key={index} className="result-item">
                        <h3>{result.metadata.filename}</h3>
                        <p>{result.content}</p>
                        <div className="metadata">
                            <p><strong>Turbine Name:</strong> {result.metadata.turbine_name}</p>
                            <p><strong>Model:</strong> {result.metadata.model}</p>
                            <p><strong>Location:</strong> {result.metadata.location}</p>
                            <p><strong>Maintenance Type:</strong> {result.metadata.maintenance_type}</p>
                        </div>
                    </div>
                ))
            )}
        </div>
    );
};

export default ResultDisplay;