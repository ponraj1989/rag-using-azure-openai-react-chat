# Frontend Documentation for Azure Document Search Application

## Overview
This project is a full-stack intelligent document search system built using Azure services. The frontend is developed using React and provides a user interface for querying documents and displaying results.

## Getting Started

### Prerequisites
- Node.js (version 14 or higher)
- npm (Node Package Manager)
- A running instance of the backend FastAPI application

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd azure-doc-search-app/frontend
   ```

2. Install the dependencies:
   ```
   npm install
   ```

3. Create a `.env` file based on the `.env.example` provided and configure the necessary environment variables.

### Running the Application
To start the development server, run:
```
npm start
```
This will launch the application in your default web browser at `http://localhost:3000`.

### Folder Structure
- `src/`: Contains the source code for the React application.
  - `components/`: Reusable components for the application.
  - `api/`: Functions for making API calls to the backend.
  - `styles/`: CSS styles for the application.
- `public/`: Contains the static files, including the main HTML file.
- `package.json`: Lists the project dependencies and scripts.

### Usage
- Enter your question in the input field.
- Use the filters to narrow down the search results based on metadata.
- View the results displayed along with relevant context.

### Deployment
For deployment instructions, refer to the main project README.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.