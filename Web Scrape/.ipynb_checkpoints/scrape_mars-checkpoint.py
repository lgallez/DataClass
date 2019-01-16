{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import shutil\n",
    "import time\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {\"executable_path\": \"/usr/local/bin/chromedriver\"}\n",
    "browser = Browser(\"chrome\", **executable_path, headless=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "December 19, 2018\n",
      "NASA's InSight Places First Instrument on Mars\n",
      "In deploying its first instrument onto the surface of Mars, the lander completes a major mission milestone.\n"
     ]
    }
   ],
   "source": [
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "article = soup.find(\"div\", class_=\"list_text\")\n",
    "news_p = article.find(\"div\", class_=\"article_teaser_body\").text\n",
    "news_title = article.find(\"div\", class_=\"content_title\").text\n",
    "news_date = article.find(\"div\", class_=\"list_date\").text\n",
    "print(news_date)\n",
    "print(news_title)\n",
    "print(news_p)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA20057_hires.jpg\n"
     ]
    }
   ],
   "source": [
    "url2 = \"https://jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(url2)\n",
    "# Scrape the browser into soup and use soup to find the image of mars\n",
    "# Save the image url to a variable called `img_url`\n",
    "html = browser.html\n",
    "image_soup = bs(html, 'html.parser')\n",
    "browser.click_link_by_partial_text('FULL IMAGE')\n",
    "time.sleep(5)\n",
    "browser.click_link_by_partial_text('more info')\n",
    "new_html = browser.html\n",
    "new_image_soup = bs(new_html, 'html.parser')\n",
    "new_html\n",
    "\n",
    "img_url = new_image_soup.find('img', class_='main_image')\n",
    "img_url_2 = img_url.get('src')\n",
    "\n",
    "featured_image_url = \"https://www.jpl.nasa.gov\" + img_url_2\n",
    "\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sol 2288 (2019-01-12), high -7C/19F, low -68C/-90F, pressure at 8.23 hPa, daylight 06:45-18:55pic.twitter.com/Or8q1l3tka\n"
     ]
    }
   ],
   "source": [
    "url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "mars_weather = soup.find(\"p\", class_=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\").text\n",
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.52 AU)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.42 x 10^23 kg (10.7% Earth)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.52 AU)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://space-facts.com/mars/'\n",
    "tables = pd.read_html(url)\n",
    "df = tables[0]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th></th>      <th>0</th>      <th>1</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Equatorial Diameter:</td>      <td>6,792 km</td>    </tr>    <tr>      <th>1</th>      <td>Polar Diameter:</td>      <td>6,752 km</td>    </tr>    <tr>      <th>2</th>      <td>Mass:</td>      <td>6.42 x 10^23 kg (10.7% Earth)</td>    </tr>    <tr>      <th>3</th>      <td>Moons:</td>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>4</th>      <td>Orbit Distance:</td>      <td>227,943,824 km (1.52 AU)</td>    </tr>    <tr>      <th>5</th>      <td>Orbit Period:</td>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>6</th>      <td>Surface Temperature:</td>      <td>-153 to 20 °C</td>    </tr>    <tr>      <th>7</th>      <td>First Record:</td>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>8</th>      <td>Recorded By:</td>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "html_table = df.to_html()\n",
    "html_table.replace('\\n', '')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
