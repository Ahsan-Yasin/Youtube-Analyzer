import chromadb 
from embedding import MyEmbeddingFunction 

embedding = MyEmbeddingFunction()  

def createDatabase(data: list[str]) -> None:
    client = chromadb.PersistentClient(path="chroma_persistent_storage")

    database = client.get_or_create_collection(
        name="YoutubeAnalyzisDatabase",  
        embedding_function=embedding    
    )

    idList = [str(i) for i in range(len(data))]  

    database.add(ids=idList, documents=data)

    print(f"Stored {database.count()} documents in ChromaDB.")
def loadDatabase(): 
    client = chromadb.PersistentClient(path="chroma_persistent_storage")
     
    database = client.get_or_create_collection(
        name="YoutubeAnalyzisDatabase",  
        embedding_function=embedding
    )
    
    return database