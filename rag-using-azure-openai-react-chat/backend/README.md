# Azure Document Search Application - Backend

## Overview
This backend service is built using FastAPI and is responsible for handling document ingestion, processing user queries, and interacting with various Azure services such as Azure Cognitive Search, Azure OpenAI, and Azure Redis.

## Project Structure
- **app/**: Contains the main application code.
  - **main.py**: Entry point for the FastAPI application.
  - **api/**: Contains API route definitions.
    - **ask.py**: Defines the `/ask` endpoint for user queries.
  - **services/**: Contains service layer code for interacting with external services.
    - **cognitive_search.py**: Functions for Azure Cognitive Search.
    - **openai.py**: Functions for Azure OpenAI.
    - **redis_cache.py**: Functions for caching with Redis.
    - **form_recognizer.py**: Functions for Azure Form Recognizer.
  - **models/**: Contains Pydantic models for request and response schemas.
    - **schemas.py**: Defines the data schemas.
  - **utils/**: Utility functions for the application.
    - **chunking.py**: Functions for chunking text.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd azure-doc-search-app/backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Copy the `.env.example` to `.env` and fill in the required values.

5. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API**
   The API will be available at `http://localhost:8000`. You can access the `/ask` endpoint to interact with the document search system.

## Additional Notes
- Ensure that all Azure services are properly configured and accessible.
- For production deployment, consider using Docker and Azure App Service.

## License
This project is licensed under the MIT License. See the LICENSE file for details.