# azure-doc-search-app/azure-doc-search-app/azure-function/ingest/__init__.py

import logging
import azure.functions as func
from .extractor import extract_text_and_metadata
from .embeddings import create_embeddings
from .metadata import extract_domain_specific_metadata

def main(blob: func.InputStream):
    logging.info(f"Processing blob: {blob.name}, Size: {blob.length} bytes")
    
    # Extract text and metadata from the uploaded document
    text_content, raw_metadata = extract_text_and_metadata(blob)
    
    # Extract domain-specific metadata
    domain_metadata = extract_domain_specific_metadata(raw_metadata)
    
    # Create embeddings from the extracted text
    embeddings = create_embeddings(text_content)
    
    # Here you would typically store the embeddings and metadata in Azure Cognitive Search
    # This part is omitted for brevity and should be implemented as per your architecture
    logging.info("Ingestion process completed successfully.")