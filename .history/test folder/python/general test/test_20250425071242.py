import time
from win10toast import ToastNotifier
from topnews import topStories

# Initialize the notifier
toaster = ToastNotifier()

# Fetch news items
newsitems = topStories()

for newsitem in newsitems:
    # Show notification on screen
    toaster.show_toast(
        title=newsitem['title'],
        msg=newsitem['description'],
        duration=10  # Notification duration in seconds
    )

    # Short delay between notifications
    time.sleep(15)
