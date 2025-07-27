from load_comments import get_comments  
from spliter import split  
from database import createDatabase

data= get_comments('https://www.youtube.com/watch?v=i-Cy3SDxLzM&ab_channel=MadHat')
data= split(data) 
createDatabase(data)
print(len(data))

for i in data[:2]:
    print("\nChunks : ")
    print (i)