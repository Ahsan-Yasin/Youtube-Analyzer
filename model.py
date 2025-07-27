import groq 
from groq import Groq   
import chromadb 
from src.main import UseUrl  
from src.database import loadDatabase
from dotenv import load_dotenv
import os 
import re  
load_dotenv()   
api= os.getenv("GROQ_API_KEY") #add your own groq api key by going to groq website
client = Groq(api_key=api)
def makedb(url):  
    UseUrl('https://www.youtube.com/watch?v=i-Cy3SDxLzM&ab_channel=MadHat' ) 

def getSentiments():
    
    db = loadDatabase()    
    TotalData=db.get() 
    total_positive=0 
    total_negative=0
    jumpSequence=100
    for i in range(0,len(TotalData['documents']),jumpSequence):  
        var =TotalData['documents'][i:i+jumpSequence]   
        completion = client.chat.completions.create(
        model="moonshotai/kimi-k2-instruct",
        messages=[ 
        { 
            "role":"system" ,  
            "content":("You are a model that analyzes YouTube comments. "
                        "You have to check how many of these comments are negative vs positive:\n"
                        f"{var}\n"
                        "You have to give output like this:\n"
                        "positive: count\n"
                        "negative: count\n"
                        "That's all. No extra text.")
        }
        ],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=1,
        stream=True,
     
        )

        # for chunk in completion:
        #     print(chunk.choices[0].delta.content or "", end="")
        full_response = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
        #   print(content, end="")  # still show in terminal
            full_response += content
        match = re.findall(r"(positive|negative):\s*(\d+)", full_response.lower())
        for label, count in match:
            if label == "positive":
                total_positive += int(count)
            elif label == "negative":
                total_negative += int(count) 
        total=total_positive+total_negative  
    if total:  
        print(f"\nTOTAL : {total}")
        print(f"POSTIVE : {total_positive}")    
        print(f"NEGATIVE : {total_negative }") 
        print(f"{(total_positive/total)*100:.1f} % Positive ||  {(total_negative/total)*100:.1f} % Negative  ")    
    return total,total_positive ,total_negative
def inference(query:str ):   
    db=loadDatabase()   
    completion = client.chat.completions.create(
        model="moonshotai/kimi-k2-instruct",
        messages=[ 
        { 
            "role":"system" ,  
            "content":(
                    "You are an LLM that helps improve search queries for a YouTube comment database stored in ChromaDB.\n"
                    f"The original query is: \"{query}\"\n"
                    "Your task is to generate 3–4 expanded or related queries to retrieve maximum relevant results from the comment database.\n"
                    "Keep the output minimal and clean, like:\n"
                    "1. ...\n"
                    "2. ...\n"
                    "3. ...\n"
                    "4. ...\n"
                    "5. ....\n"
                    "Do not include any explanations or instructions. Just list the expanded queries."
                )
        }
        ],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=1,
        stream=True,
     
        )
    answer=""
    for chunk in completion:
        answer+=chunk.choices[0].delta.content or ""
    #print(answer)  
    stackQuery=answer+query
    result=db.query(query_texts=stackQuery   ,n_results=5 )  
    relevantData=result['documents'][0] 
    #print(relevantData) 
    completion = client.chat.completions.create(
        model="moonshotai/kimi-k2-instruct",
        messages=[ 
        { 
            "role":"system" ,  
            "content":(
                "You are a helpful assistant that analyzes viewer feedback from YouTube comments. "
                f"Always use only this  context : {relevantData}  to answer the question asked ."
                " Summarize your answer in 3–5 clear, short lines. Do not make assumptions beyond the given data if you cant find the answer say i dont know ."
                "Talk like an analyst but in a light easy tone  " 
                "Each line should be similar in length and use '\\n' to break lines for a rectangular shape."
                )
        }, 
        {  
                "role":"user", 
                "content":query 
        }
        ],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=1,
        stream=True,
     
        )
    Finalanswer=""
    for chunk in completion:
        Finalanswer+=chunk.choices[0].delta.content or ""

    return Finalanswer
#getSentiments()
 
answer= inference("What are the postive comments saying and whats the main concern of negative") 
print('\n\n\n',answer)