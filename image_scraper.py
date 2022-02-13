"""
simple script to grab images from bing and save to a local path.
"""


import requests
import os
from bs4 import BeautifulSoup as soup

# parse args, which are the image search term, number of images to get


# make a new directory based on the search term argument


# construct a request from the search arg and get result from bing
query = 'dragons'
bing_url = "http://www.bing.com/images/search?q=" + query
import time
start = time.time()
result = requests.get(bing_url)
print('requests took', time.time() - start)

try:
  print(result.text)
except:
  print('cannot call result.text\n')
  pass

try:
  same_thing = result.text.encode('utf-8')
except:
  print('cannot assign')

try:
  print(result.json())
except:
  print('cannot call result.json()\n')
  pass

url = "http://www.bing.com/images/search?q=" + query + "&qft=+filterui:color2-bw+filterui:imagesize-large&FORM=R5IR3"
start = time.time()
result = requests.get(url)
print('requests took', time.time() - start)
# requests packages takes more than 2 minutes!!!
# curl via cmd line takes ~2 seconds
# convert this to a bash script, or find another library to handle get requests

# parse result to get list of image urls


# iterate through list, fetch and save images to image path

