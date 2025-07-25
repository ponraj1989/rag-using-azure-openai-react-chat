from azure.storage.blob import BlobServiceClient
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os
import json

def extract_text_and_metadata(blob_url):
    form_recognizer_endpoint = os.getenv("FORM_RECOGNIZER_ENDPOINT")
    form_recognizer_key = os.getenv("FORM_RECOGNIZER_KEY")
    
    document_analysis_client = DocumentAnalysisClient(
        endpoint=form_recognizer_endpoint,
        credential=AzureKeyCredential(form_recognizer_key)
    )

    poller = document_analysis_client.begin_read_url(blob_url, language="en")
    result = poller.result()

    text_content = ""
    metadata = {}

    for page_result in result.analyze_result.read_results:
        for line in page_result.lines:
            text_content += line.text + "\n"

    # Extract domain-specific metadata (example extraction logic)
    # This should be customized based on the document structure
    metadata['turbine_name'] = extract_metadata(text_content, "Turbine Name:")
    metadata['model'] = extract_metadata(text_content, "Model:")
    metadata['location'] = extract_metadata(text_content, "Location:")
    metadata['maintenance_type'] = extract_metadata(text_content, "Maintenance Type:")

    return text_content, metadata

def extract_metadata(text, key):
    # Simple extraction logic for demonstration purposes
    for line in text.splitlines():
        if line.startswith(key):
            return line.split(":", 1)[1].strip()
    return None

def upload_blob_to_storage(file_path):
    blob_service_client = BlobServiceClient.from_connection_string(os.getenv("AZURE_STORAGE_CONNECTION_STRING"))
    blob_client = blob_service_client.get_blob_client(container=os.getenv("BLOB_CONTAINER_NAME"), blob=os.path.basename(file_path))

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

def main(blob_url):
    text, metadata = extract_text_and_metadata(blob_url)
    # Further processing like chunking and embedding can be done here
    return text, metadata