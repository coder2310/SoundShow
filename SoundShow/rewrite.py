import json
from Utilities import utilities

def re_write_google():
    with open("google.json") as goog:
        data = json.load(goog)
        new_data = []
        for entry in data:
            encoded_link = utilities.shorten_hash_link(entry["url"])
            entry["url"] = encoded_link[0]
            entry["hash_link"] = encoded_link[1]
            new_data.append(entry)
        for elem in new_data:
            print(elem, file = open("google_dump.txt", "a+"))
        with open("new_google.json", "w+") as new_goog:
            json.dump(new_data, new_goog)

def re_write_youtube():
    with open("tube.json") as tube:
        data = json.load(tube)
        new_data = []
        for entry in data:
            # print(entry, file = open("tube_dump.txt", "a+"))
            if entry["link"]:
                encoded_link =utilities.shorten_hash_link(entry["link"])
                entry["link"] = encoded_link[0]
                entry["hash_link"] = encoded_link[1]
            new_data.append(entry)
        for elem in new_data:
            print(elem, file = open("tube_dump.txt", "a+"))
        with open("new_tube.json", "w+") as new_tube:
            json.dump(new_data, new_tube)


def re_write_spot():
    with open("spot.json") as spot:
        data = json.load(spot)
        new_data = []
        for entry in data:
            encoded_link = utilities.shorten_hash_link(entry["link"])
            entry["link"] = encoded_link[0]
            entry["hash_link"] = encoded_link[1]
            new_data.append(entry)
        with open("new_spot.json", "w+") as new_spot:
            json.dump(new_data, new_spot)

        

