import React, { useState } from 'react';
import QuestionInput from './components/QuestionInput';
import Filters from './components/Filters';
import ResultDisplay from './components/ResultDisplay';
import './styles/main.css';

const App = () => {
  const [query, setQuery] = useState('');
  const [filters, setFilters] = useState({});
  const [results, setResults] = useState([]);

  const handleQueryChange = (newQuery) => {
    setQuery(newQuery);
  };

  const handleFiltersChange = (newFilters) => {
    setFilters(newFilters);
  };

  const handleResultsChange = (newResults) => {
    setResults(newResults);
  };

  return (
    <div className="App">
      <h1>Intelligent Document Search</h1>
      <QuestionInput query={query} onQueryChange={handleQueryChange} onResultsChange={handleResultsChange} />
      <Filters filters={filters} onFiltersChange={handleFiltersChange} />
      <ResultDisplay results={results} />
    </div>
  );
};

export default App;