import time
from plyer import notification
from topnews import topStories

# Fetch news items
newsitems = topStories()

for newsitem in newsitems:
    # Show notification on screen
    notification.notify(
        title=newsitem['title'],
        message=newsitem['description'],
        timeout=10  # Notification timeout in seconds
    )

    # Short delay between notifications
    time.sleep(15)
