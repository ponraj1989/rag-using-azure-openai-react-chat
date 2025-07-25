def create_embeddings(text_chunks):
    import openai

    embeddings = []
    for chunk in text_chunks:
        response = openai.Embedding.create(
            input=chunk,
            model="text-embedding-ada-002"
        )
        embeddings.append(response['data'][0]['embedding'])
    
    return embeddings