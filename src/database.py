import chromadb 
from embedding import MyEmbeddingFunction 

embedding = MyEmbeddingFunction()  

def createDatabase(data: list[str]) -> None:
    client = chromadb.PersistentClient(path="chroma_persistent_storage")

    database = client.get_or_create_collection(
        name="YoutubeAnalyzisDatabase",  # Avoid spaces in collection names
        embedding_function=embedding    
    )

    idList = [str(i) for i in range(len(data))]  # Generate unique string IDs

    database.add(ids=idList, documents=data)

    print(f"Stored {database.count()} documents in ChromaDB.")
