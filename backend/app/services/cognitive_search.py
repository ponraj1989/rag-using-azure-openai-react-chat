from azure.search.documents import SearchClient
from azure.search.documents.models import SearchQuery, SearchOptions
from azure.core.credentials import AzureKeyCredential
import os

class CognitiveSearchService:
    def __init__(self):
        self.search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        self.search_api_key = os.getenv("AZURE_SEARCH_API_KEY")
        self.index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
        self.search_client = SearchClient(endpoint=self.search_endpoint,
                                          index_name=self.index_name,
                                          credential=AzureKeyCredential(self.search_api_key))

    def search_documents(self, query, filters=None):
        search_options = SearchOptions(filter=filters)
        results = self.search_client.search(search_text=query, options=search_options)
        return [result for result in results]

    def index_document(self, document):
        self.search_client.upload_documents(documents=[document])