import os
from flask import Flask
import flask
import random
import requests
import json
import requests_oauthlib
from requests_oauthlib import OAuth1Session

app = Flask(__name__)

@app.route('/')
def index():
    
    #Twitter API Search for Tweets
    twitter_search = "https://api.twitter.com/1.1/search/tweets.json?q=yummy%20donuts&src=typed_query"
    
    #Twitter Retrieval from Search
    twitter_response = random.randint(0,9)
    
    
    #Authorization
    oauth = requests_oauthlib.OAuth1(
    "qukgAQr6KLxBk6wwvImUMvAsx", 
    "58BO5DB0gmL1edgdRXnxXpEgrOMoo1KzMt4oOx7NCiUxONDEka",
    "1223192085756596225-UIVDa9WQSMyp3IqJgz7poKxvppykg2",
    "DjzlFxxcCxJ4sP2QSXem9KANGFHKi1RgIIBSa9JPPKlof"
    )

    response = requests.get(twitter_search, auth=oauth)
    json_body = response.json()

    donut_tweets = json_body['statuses'][twitter_response]['text']
    
    
    #Spoonacular API Search for Donuts
    spoonacular_donut_search = "https://api.spoonacular.com/recipes/search?query=donuts&apiKey=e226375de4794ef1ac1174ffde8bdeb9"

    
    response_1 = requests.get(spoonacular_donut_search)
    json_body_1 = response_1.json()

    
    #Recipe Title
    recipe_title = json_body_1['results'][twitter_response]['title']
    
    #Prep Time
    prep_time = json_body_1['results'][twitter_response]['readyInMinutes']
    
    #Servings
    serving_size = json_body_1['results'][twitter_response]['servings']
    
    #ID (for ingredients & image)
    donut_id = json_body_1['results'][twitter_response]['id']    
    
    
    #Spoonacular API Search for Donut Information
    spoonacular_donut_info = "https://api.spoonacular.com/recipes/{}/information?includeNutrition=false&apiKey=e226375de4794ef1ac1174ffde8bdeb9".format(donut_id)
    
    response_2 = requests.get(spoonacular_donut_info)
    json_body_2 = response_2.json()

    #Image
    donut_image = json_body_2["image"]
    
    #Recipe Link
    donut_source_url = json_body_2["sourceUrl"]
    

    return flask.render_template("index.html",
                                recipe_title = recipe_title,
                                prep_time = prep_time,
                                serving_size = serving_size,
                                donut_image = donut_image,
                                donut_source_url = donut_source_url,
                                donut_tweets = donut_tweets
                                )




app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))