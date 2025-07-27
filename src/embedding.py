from sentence_transformers import SentenceTransformer   
 
#This is my embedding funtion :  
class MyEmbeddingFunction:
    def __init__(self): 
        self.model = SentenceTransformer("all-MiniLM-L6-v2")  # or any other model

    def __call__(self, input):
     
        return self.model.encode(input).tolist()

    def name(self):
        return "sentence-transformers_all-MiniLM-L6-v2"