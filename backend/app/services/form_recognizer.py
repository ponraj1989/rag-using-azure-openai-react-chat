from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os

class FormRecognizerService:
    def __init__(self):
        self.endpoint = os.getenv("FORM_RECOGNIZER_ENDPOINT")
        self.api_key = os.getenv("FORM_RECOGNIZER_API_KEY")
        self.client = DocumentAnalysisClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.api_key))

    def extract_text_and_metadata(self, document_url):
        poller = self.client.begin_read_document_from_url(document_url, language="en")
        result = poller.result()

        text_content = ""
        metadata = {}

        for page in result.analyze_result.read_results:
            for line in page.lines:
                text_content += line.text + "\n"

        # Example of extracting domain-specific metadata
        # This should be customized based on the document structure
        for key_value_pair in result.analyze_result.document_results[0].fields.items():
            key, value = key_value_pair
            if value.value_string:
                metadata[key] = value.value_string

        return text_content.strip(), metadata