from collections import deque
from threading import Thread
import sys

# import Engine.searchGoogle
# import Engine.searchSpotify
# import Engine.searchGoogle
from Engine import searchGoogle, searchYoutube, searchSpotify

def g_interests(lst_interests):
    # each API now has its own function
    # this so we can return a list of dictionaries for each API
    # but more importantly this will allow us to run each funnction
    # concurrently since each API is seperate we can use threads to
    # make calls to each one of them speeding up the how fast the user
    # home a page loads
    content = []
    for elem in lst_interests:
        content.extend(searchGoogle.get_recent_articles(elem))
    return "google_search", content


# this version concurrently makes an api call for every user interest
# might end up being faster, want to test same for youtube and spotify
def g_interests_thread(lst_interests):
    deq = deque()
    content = []
    thread_list = []
    for elem in lst_interests:
        new_thread = Thread(target=lambda q, elem: q.append(searchGoogle.get_recent_articles(elem)),
                            args=(deq, elem))
        new_thread.start()
        thread_list.append(new_thread)
    for thread in thread_list:
        thread.join()

    while len(deq) > 0:
        res = deq.popleft()
        content.extend(res)
    return "google_search", content

def y_interests_thread(lst_interests):
    deq = deque()
    content = []
    thread_list = []
    for elem in lst_interests:
        new_thread = Thread(target=lambda q, elem: q.append(searchYoutube.extract_data(elem)),
                            args=(deq, elem))
        new_thread.start()
        thread_list.append(new_thread)
    for thread in thread_list:
        thread.join()
    while len(deq) > 0:
        res = deq.popleft()
        content.extend(res)
    return "youtube_search", content



def y_interests(lst_interests):
    content = []
    for elem in lst_interests:
        content.extend(searchYoutube.extract_data(elem))
    return "youtube_search", content


def s_interests(lst_interests):
    print("Inside spotify", file =sys.stdout)
    results = searchSpotify.artistForGenres(lst_interests)
    print(results, file = sys.stdout)
    return "spotify_search", results

def s_interests_thread(lst_interests):
    pass

def retrieve_content(lst_interests, has_spot = False):
    # we this the functions that will create threads
    # and return the dictionary
    # will use a deque to store the results

    resources = {
        "google_search": [],
        "youtube_search": []
    }
    # this is what we will use to store the thread results
    deq = deque()
    threads_list = []
    gt = Thread(target=lambda q, lst_interests: q.append(
        g_interests_thread(lst_interests)), args=(deq, lst_interests))
    # we create and start threed add it to the list and the results are then stored in the
    # deque
    gt.start()
    threads_list.append(gt)
    # yt = Thread(target=lambda q, lst_interests: q.append(y_interests(lst_interests)), args=(deq, lst_interests))
    # yt.start()
    # # # TODO add spotify thread when this done
    # threads_list.append(yt)
    if has_spot:
        resources["spotify_search"] = []
        st = Thread(target=lambda q, lst_interests: q.append(s_interests(lst_interests)), args=(deq, lst_interests))
        st.start()
        threads_list.append(st)
    for thread in threads_list:
        thread.join()  # we join execution for each one
    while len(deq) > 0:
        # since threads are nondeterminitstic we dont know which one
        # will finish first which is why we also will return the key that
        # the function representes int the dictionary
        # and we set it accordingly
        result = deq.popleft()
        resources[result[0]] = result[1]
    print("Spotify Search Results:", len(resources["spotify_search"]),file = sys.stdout)
    return resources
