import feedparser
import pprint

#et = feedparser.parse("http://economictimes.indiatimes.com/Markets/markets/rssfeeds/1977021501.cms")
et = feedparser.parse("http://economictimes.indiatimes.com/Markets/markets/")

pprint.pprint(et)

