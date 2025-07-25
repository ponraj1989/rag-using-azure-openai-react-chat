def chunk_text(text, chunk_size=1000, overlap=100):
    """
    Splits the input text into chunks of specified size with overlap.
    
    Args:
        text (str): The text to be chunked.
        chunk_size (int): The maximum size of each chunk.
        overlap (int): The number of overlapping characters between chunks.
        
    Returns:
        list: A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def chunk_and_embed(text, chunk_size=1000, overlap=100, embed_function=None):
    """
    Chunks the text and creates embeddings for each chunk.
    
    Args:
        text (str): The text to be chunked and embedded.
        chunk_size (int): The maximum size of each chunk.
        overlap (int): The number of overlapping characters between chunks.
        embed_function (callable): A function to create embeddings for a chunk.
        
    Returns:
        list: A list of tuples containing chunks and their embeddings.
    """
    chunks = chunk_text(text, chunk_size, overlap)
    embeddings = [(chunk, embed_function(chunk)) for chunk in chunks] if embed_function else [(chunk, None) for chunk in chunks]
    return embeddings