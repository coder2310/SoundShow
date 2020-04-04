API_KEY = "AIzaSyA7sdo-57bTeW5Gl_M4KD078vDdpp8lkk4"
import json

from googleapiclient.discovery import build 

# Arguments that need to passed to the build function 
DEVELOPER_KEY = "AIzaSyA7sdo-57bTeW5Gl_M4KD078vDdpp8lkk4"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating Youtube Resource Object 
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                        developerKey = DEVELOPER_KEY) 


def youtube_search_keyword(query, max_results = 10): 
    
    # calling the search.list method to 
    # retrieve youtube search results 
    search_keyword = youtube_object.search().list(q = query, part = "id, snippet", 
                                            maxResults = max_results).execute() 
    
    # extracting the results from search response 
    results = search_keyword.get("items", []) 
    # print("Result Length:", type(results))
    # print("results:", type(results))
    # empty list to store video, 
    # channel, playlist metadata 
    videos = [] 
    playlists = [] 
    channels = [] 
    # for result in results:
    #     print("Result:", type(result))
    
    # extracting required info from each result object 
    for result in results: 
        # video result object 
        if result['id']['kind'] == "youtube# video": 
            videos.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"], 
                            result["id"]["videoId"], result['snippet']['description'], 
                            result['snippet']['thumbnails']['default']['url'])) 

        # playlist result object 
        elif result['id']['kind'] == "youtube# playlist": 
            playlists.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"], 
                                result["id"]["playlistId"], 
                                result['snippet']['description'], 
                                result['snippet']['thumbnails']['default']['url'])) 

        # channel result object 
        elif result['id']['kind'] == "youtube# channel": 
            channels.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"], 
                                result["id"]["channelId"], 
                                result['snippet']['description'], 
                                result['snippet']['thumbnails']['default']['url']))
        return {
            "results": results,
            "videos" : videos,
            "playlists": playlists,
            "channels" : channels
        }
    
        
def extract_data(search_term):
    #Object will be simialar that for news
    # title
    # desctiption 
    # link
    # defualt thumbnail
    # chanel title
    # Chananel link
    data =  []
    results = youtube_search_keyword(search_term)
    for element in results["results"]:
        entry = {
            "title": None,
            "description": None,
            "link": None,
            "image": None,
            "channel": None,
            "channel_link": "https://www.youtube.com/channel/{}"
        }

        entry["title"] = element["snippet"]["title"]
        entry["description"] = element["snippet"]["description"][0:100]  
        if element["id"]["kind"] == "youtube#video":
            link = "https://www.youtube.com/watch?v={}".format(element["id"]["videoId"])
            entry["link"] = link
        entry["image"] = element["snippet"]["thumbnails"]["medium"]["url"]
        entry["channel"] = element["snippet"]["channelTitle"]
        entry["channel_link"] = entry["channel_link"].format(element["snippet"]["channelId"])
        data.append(entry)
    return data






    


