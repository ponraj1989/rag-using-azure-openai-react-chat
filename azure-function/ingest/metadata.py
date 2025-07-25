from typing import Dict, Any

def extract_metadata(document: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extracts domain-specific metadata from the provided document.

    Args:
        document (Dict[str, Any]): The document from which to extract metadata.

    Returns:
        Dict[str, Any]: A dictionary containing the extracted metadata.
    """
    metadata = {
        "turbine_name": document.get("turbine_name"),
        "model": document.get("model"),
        "location": document.get("location"),
        "maintenance_type": document.get("maintenance_type"),
        "filename": document.get("filename"),
    }
    return {key: value for key, value in metadata.items() if value is not None}