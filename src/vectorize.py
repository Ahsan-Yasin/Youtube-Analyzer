#This file converts the comments into vectorized form 
import chromadb
from embedding import MyEmbeddingFunction  
def vectorize(data:list[str])->list: 
    embedder=MyEmbeddingFunction()  
    print(embedder("I am ahsan"))

vectorize(['a','sfds'])

     
