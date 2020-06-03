import webbrowser
from selenium import webdriver
import requests
import re

# connect to the url
website = requests.get("https://fmovies.wtf/film/friends.vv866")

# read html
html = website.text

# use re.findall to grab all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

# output links
for link in links:
    print(link[0])
# driver = webdriver.Chrome('/Applications/chromedriver')
# driver.get("https://fmovies.wtf/film/friends.vv866")
# element = driver.find_element_by_xpath("Episode 02")
# print(element)
# element.click()