import time
from win10toast import ToastNotifier
import requests
import xml.etree.ElementTree as ET

def topStories():
    """
    Fetch top news stories from the RSS feed.
    """
    # RSS feed URL
    url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

    # Send a GET request to fetch the RSS feed
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch news.")
        return []

    # Parse the RSS feed
    root = ET.fromstring(response.content)
    newsitems = []

    # Extract news items
    for item in root.findall('./channel/item'):
        news = {
            'title': item.find('title').text if item.find('title') is not None else 'No Title',
            'description': item.find('description').text if item.find('description') is not None else 'No Description'
        }
        newsitems.append(news)

    return newsitems

# Initialize the notifier
toaster = ToastNotifier()

# Fetch news items
newsitems = topStories()

for newsitem in newsitems:
    # Extract title and description
    title = newsitem.get('title', 'No Title')
    description = newsitem.get('description', 'No Description')

    # Show notification on screen
    toaster.show_toast(
        title=title,
        msg=description,
        duration=10  # Notification duration in seconds
    )

    # Short delay between notifications
    time.sleep(15)