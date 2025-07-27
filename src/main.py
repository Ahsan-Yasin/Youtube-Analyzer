from src.load_comments import get_comments  
from src.spliter import split  
from src.database import createDatabase

def UseUrl(url):
    data= get_comments(url)
    data= split(data) 
    createDatabase(data)
    print(len(data))
    
    # for i in data[:2]:
    #     print("\nChunks : ")
    #     print (i)