# get-rss-feed-to-csv




get-rss-feed-to-csv
=======

Python script to extract the RSS feed data from given URL and post it in csv file.

Requirements
------------
* Python 2.7.6 tested
* requests 2.2.1
* pandas 1.5
* bs4
* lxml

Installation
------------
Via PIP:
```bash
pip install pandas
pip install bs4
pip install lxml
```

Usage
-----
Downlaod the file get-rss-feed-to-csv.py in the project and 
Start by importing the module.
```python
from get-rss-feed-to-csv import get_all_feeds
feeds = get_all_feeds(url)
#data frame to csv file.. 
feeds.to_csv('feeds.csv',index=False)
```
Here ```url``` variable must contain a valid RSS Feed(https://www.europarl.europa.eu/rss/doc/top-stories/en.xml) string.


