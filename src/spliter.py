#This file converts the comments into chunks 

def split(data:list[str])->list:   
    return [c.strip() for c in data if c.strip()]
     