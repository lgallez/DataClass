from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import shutil
import time
import pandas as pd

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

url = "https://mars.nasa.gov/news/"
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')
article = soup.find("div", class_="list_text")
news_p = soup.article("div", class_="article_teaser_body").text
news_title = soup.find("div", class_="content_title").text
news_date = soup.find("div", class_="list_date").text
# print(news_date)
# print(news_title)
# print(news_p)

url2 = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url2)
# Scrape the browser into soup and use soup to find the image of mars
# Save the image url to a variable called `img_url`
html = browser.html
image_soup = bs(html, 'html.parser')
browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(5)
browser.click_link_by_partial_text('more info')
new_html = browser.html
new_image_soup = bs(new_html, 'html.parser')
new_html

img_url = new_image_soup.find('img', class_='main_image')
img_url_2 = img_url.get('src')

featured_image_url = "https://www.jpl.nasa.gov" + img_url_2

# print(featured_image_url)

url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
# print(mars_weather)

url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
df = tables[0]
# df.head()

# html_table = df.to_html()
# html_table.replace('\n', '')
