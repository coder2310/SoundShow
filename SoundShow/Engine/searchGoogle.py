API_KEY = 'c960fb6217584e66b72bf22ad257a3db'
import json
import requests
from datetime import datetime, timedelta


def process_response(url):
    #keys we care about 
    #status code - needs to be ok
    # totalResults - tells us how many results were retrieved. 
    # will decide later if we want to use it all
    # articles - list of objects which we will parse from
    #source[name]
    #title
    #description - only get the first hundred character followed by ...
    #url - might want to use  url_shortner for both urls
    #url_to_image
    response = requests.get(url)
    content = response.json()
    data = []
    if content['status'] == 'ok':
        for results in content['articles']:
            # print(type(results))
            entry = {
                'source' : None,
                'title' : None,
                'description': None,
                'url': None,
                'img_url': None
            }
            entry['source'] = results['source']['name']
            entry['title'] = results['title']
            if results['description']:
                entry['description'] = results['description'][0:100] + '...'
            else:
                entry['description'] = "No description"
            entry['url'] = results['url']
            entry['img_url'] = results['urlToImage']
            data.append(entry)
    return data

def get_all_trending():
    url = 'http://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(API_KEY)
    return process_response(url)

def get_trending_by_category(category):
    category = category.replace(' ', '+')
    url = 'http://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'.format(category, API_KEY)
    return process_response(url)


def get_trending_topic(topic):
    topic = topic.replace(' ', '+')
    url = 'http://newsapi.org/v2/top-headlines?q={}&apiKey={}'.format(topic, API_KEY)
    return process_response(url)

def get_trending_category_topic(category, topic):
    category, topic = category.replace(' ', '+') , topic.replace(' ', '+')
    url = 'http://newsapi.org/v2/top-headlines?category={}&q={}&apiKey={}'.format(category,topic, API_KEY)
    return process_response(url)

def get_all_articles(topic):
    topic = topic.replace(' ', '+')
    url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(topic, API_KEY)
    return process_response(url)

def get_recent_articles(topic):
    topic = topic.replace(' ', '+')
    today = datetime.now()
    three_days_ago = today - timedelta(days = 3)
    today, three_days_ago = str(datetime.date(today)), str(datetime.date(three_days_ago))
    url = 'https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy=popularity&apiKey={}'
    url = url.format(topic,three_days_ago, today,API_KEY)
    return process_response(url)

def process_users_interests(interests):
    # we will experiment with what functions to use  here but get_recent_articles
    # seems to yeild the most useful results
    return {topic: get_recent_articles(topic) for topic in interests}

