import chromadb 
from src.embedding import MyEmbeddingFunction 

embedding = MyEmbeddingFunction()  

def createDatabase(data: list[str],flag=True) -> None:
    client = chromadb.PersistentClient(path="chroma_persistent_storage")

    database = client.get_or_create_collection(
        name="YoutubeAnalyzisDatabase",  
        embedding_function=embedding    
    )
    if flag:   #if a new url is passed we will delete the old data but if user says to keep the old data we will keep the whole database 
        delId=[str(i) for i in range(database.count())] 
        if delId:
            database.delete(ids= delId)  
        else:
            print("Database is empty")
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