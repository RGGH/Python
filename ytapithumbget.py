# sudo pip install --upgrade google-api-python-client
import requests
import os
from apiclient.discovery import build
import apikey
import time

path = "/youtube_thumbnails/"

if not os.path.exists(path):
    time.sleep(1)	
    os.makedirs(path)

api_key = apikey.api_key

youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_videos(channel_id):
    
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while True:
        res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos

# MAIN #

if __name__ == "__main__":

	videos = get_channel_videos('UCVMoZ-gwrMEvGFUdeKDpVUg')

	for video in videos:
	    print(video['snippet']['title'])
	    #print(video['snippet']['description'])
	    

	for idx, image in enumerate(videos):

		print(image['snippet']['thumbnails']['high']['url'])
		url = (image['snippet']['thumbnails']['high']['url'])

		s_name = url.split('/')[-2]

		print(s_name)
		totalvids = (len(videos))
		print(f"Getting thumbnail number,{idx} of {totalvids}")
		print("*" * idx)
		r = requests.get(url, allow_redirects=True)

		open(path + s_name +".jpg", 'wb').write(r.content)

	print ("Done, now check you local directory for thumbnails")

	 #    #refer to : https://developers.google.com/youtube/v3/docs/videos#resource-representation

















