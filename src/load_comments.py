#This file loads comments from  youtube vedio  
from googleapiclient.discovery import build
import re
 # -------- Config --------
API_KEY = 'AIzaSyCeBb-ZmKX78B63ob7g4wt3h69b_1oVijE' 

def get_video_id(url):
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None

def get_comments (url)->list: 
  

    VIDEO_URL = url #this is the vedio url 
    video_id = get_video_id(VIDEO_URL)

   
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    comments = []
    next_page_token = None

    while True:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            textFormat="plainText",
             order="relevance", 
            pageToken=next_page_token
        ).execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

#   print("Comments lenth : ",len(comments))
    return comments 

