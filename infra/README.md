# Infrastructure Setup for Azure Document Search Application

This directory contains the infrastructure as code (IaC) templates and documentation for provisioning the necessary Azure resources for the Azure Document Search Application.

## Overview

The infrastructure is designed to support the following components:

1. **Azure Blob Storage**: For storing uploaded documents.
2. **Azure Function**: For processing document ingestion and triggering the extraction of text and metadata.
3. **Azure Cognitive Search**: For indexing and searching the extracted content and metadata.
4. **Azure OpenAI**: For generating responses based on user queries.
5. **Azure Redis**: (Optional) For caching search results to improve performance.

## Provisioning Resources

### ARM Templates

The `arm` directory contains ARM templates for provisioning the Azure resources. Each template is responsible for a specific resource:

- `blob-storage.json`: Template for Azure Blob Storage.
- `cognitive-search.json`: Template for Azure Cognitive Search.
- `openai.json`: Template for Azure OpenAI.
- `redis.json`: Template for Azure Redis.
- `function-app.json`: Template for Azure Function.

### Bicep Templates

The `bicep` directory contains Bicep templates, which provide a more concise syntax for provisioning Azure resources. Each Bicep file corresponds to an ARM template:

- `blob-storage.bicep`: Bicep template for Azure Blob Storage.
- `cognitive-search.bicep`: Bicep template for Azure Cognitive Search.
- `openai.bicep`: Bicep template for Azure OpenAI.
- `redis.bicep`: Bicep template for Azure Redis.
- `function-app.bicep`: Bicep template for Azure Function.

## Deployment Instructions

1. **Choose a Template**: Decide whether to use ARM or Bicep templates for provisioning.
2. **Set Up Azure CLI**: Ensure you have the Azure CLI installed and configured with your Azure account.
3. **Deploy the Template**:
   - For ARM: Use the following command:
     ```
     az deployment group create --resource-group <your-resource-group> --template-file <template-file>
     ```
   - For Bicep: Use the following command:
     ```
     az deployment group create --resource-group <your-resource-group> --template-file <template-file>.bicep
     ```
4. **Configure Environment Variables**: After provisioning, configure the necessary environment variables in your application to connect to the Azure resources.

## Additional Resources

- [Azure Documentation](https://docs.microsoft.com/en-us/azure/)
- [ARM Templates Documentation](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)
- [Bicep Documentation](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/)

## Conclusion

This infrastructure setup provides a robust foundation for the Azure Document Search Application, enabling efficient document ingestion, search, and response generation. Follow the instructions carefully to provision the required resources and ensure a smooth deployment process.