from load_comments import get_comments  
from spliter import split  


data= get_comments('https://www.youtube.com/watch?v=i-Cy3SDxLzM&ab_channel=MadHat')
data= split(data)
print(len(data))

for i in data[:5]:
    print("\nChunks : ")
    print (i)