from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_all_feeds(feedurl):
  #get the url response
  url = requests.get(feedurl)
  #XML parsing with bs4's BeautifulSoup  
  soup = BeautifulSoup(url.content, 'xml')

  #for each parent tag get all attributes
  items = soup.find_all('item')
  feed_all_data =  []
  for item in items:
    feed_data =  {}
    feed_data['title'] = item.title.text
    feed_data['link'] = item.link.text
    #feed_data['description'] = item.description.text
    feed_data['source'] = item.source.text
    feed_data['source_url'] = item.source.get('url')
    feed_data['category'] =item.category.text
    feed_data['category_domain'] =  category.get('domain')
    feed_data['pubDate'] = item.pubDate.text
    feed_data['guid'] = item.guid.text
    feed_data['guid_isPermaLink'] =guid.get('isPermaLink')
    feed_all_data.append(feed_data)
  #get all data for the feeds in pandas data frame 
  feeds =  pd.DataFrame(feed_all_data)
  return feeds



def main():
    feeds = get_all_feeds('https://www.europarl.europa.eu/rss/doc/top-stories/en.xml')
    #data frame to csv file.. 
    feeds.to_csv('feeds.csv',index=False)
    
if __name__ == "__main__":
    main()


