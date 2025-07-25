import React from 'react';

const Filters = ({ filters, setFilters }) => {
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFilters((prevFilters) => ({
            ...prevFilters,
            [name]: value,
        }));
    };

    return (
        <div className="filters">
            <label>
                Turbine Name:
                <input
                    type="text"
                    name="turbine_name"
                    value={filters.turbine_name}
                    onChange={handleChange}
                />
            </label>
            <label>
                Model:
                <input
                    type="text"
                    name="model"
                    value={filters.model}
                    onChange={handleChange}
                />
            </label>
            <label>
                Location:
                <input
                    type="text"
                    name="location"
                    value={filters.location}
                    onChange={handleChange}
                />
            </label>
            <label>
                Maintenance Type:
                <input
                    type="text"
                    name="maintenance_type"
                    value={filters.maintenance_type}
                    onChange={handleChange}
                />
            </label>
        </div>
    );
};

export default Filters;