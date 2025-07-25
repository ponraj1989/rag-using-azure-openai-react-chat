# Azure Function Ingestion README

## Overview

This directory contains the Azure Function responsible for ingesting documents uploaded to Azure Blob Storage. The function automatically triggers upon the upload of new documents and processes them to extract text content, domain-specific metadata, and create embeddings for vector search.

## Structure

- `ingest/__init__.py`: Initializes the Azure Function.
- `ingest/extractor.py`: Contains functions for extracting text and metadata from uploaded documents.
- `ingest/embeddings.py`: Includes functions for creating embeddings from text using Azure OpenAI.
- `ingest/metadata.py`: Defines functions for extracting and structuring domain-specific metadata.

## Setup Instructions

1. **Environment Variables**: 
   - Create a `.env` file based on the `.env.example` provided in this directory. Ensure all required variables are set.

2. **Dependencies**: 
   - Install the required Python packages listed in `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

3. **Deploying the Function**: 
   - Use the Azure CLI or Azure Functions Core Tools to deploy the function to your Azure account.

4. **Testing**: 
   - After deployment, upload a document to the configured Azure Blob Storage container to trigger the function and verify that the ingestion process works as expected.

## Usage

The Azure Function will automatically process documents as they are uploaded to Azure Blob Storage. Ensure that the Blob Storage trigger is correctly configured in `function.json`.

## Additional Resources

- [Azure Functions Documentation](https://docs.microsoft.com/en-us/azure/azure-functions/)
- [Azure Blob Storage Documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/)
- [Azure OpenAI Documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/openai/)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.