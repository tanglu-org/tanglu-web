import feedparser

from django import template

register = template.Library()

# SafeWrap template filter
def safewrap(val, arg):
    return val.format(arg)

register.filter('safewrap', safewrap)
safewrap.is_safe = True

# Feed Parser template tag
class Feed:
    "Class that stores rss feed's informations"
    title = "No Title Set"
    link = "#"
    hasEntries = False
    entries = []


def feed(feedLocation):
    maxEntries = 5

    # Parse the feed XML
    feedData = feedparser.parse(feedLocation)

    # Instantiate a Feed object
    feed = Feed()

    # Check the HTTP status. If not 200, return a default Feed object
    if feedData.status != 200:
        return Feed()

    try:
        # Set feed title and link attributes
        feed.title = feedData.feed.title
        feed.link = feedData.feed.link

        feed.entries = []

        if feedData.version == "rss20":
            # Append the entries to the Feed object
            for entry in feedData.entries:
                if maxEntries == 0:
                    break

                feed.entries.append({
                    'title': entry.title,
                    'link': entry.link,
                    'published': entry.published,
                })

                maxEntries -= 1
        elif feedData.version == "rss10":
            # Append the entries to the Feed object
            for entry in feedData.entries:
                if maxEntries == 0:
                    break

                print entry

                feed.entries.append({
                    'title': entry.title,
                    'link': entry.link,
                    'published': "",
                })

                maxEntries -= 1

        # Set hasEntries to True in Feed object
        if feed.entries:
            feed.hasEntries = True
    except:
        pass

    # Return the feed object
    return feed

register.assignment_tag(feed)
