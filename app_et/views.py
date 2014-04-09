from django.shortcuts import render
import feedparser
import pprint

# Create your views here.
def et(request):
  content = feedparser.parse("http://economictimes.indiatimes.com/rssfeedsdefault.cms")
  pprint.pprint(content)
  return render(request, 'et.html', {'results': content['entries']})

def et_home(request):
  content = feedparser.parse(rss_et_home)
  pprint.pprint(content)
  return render(request, 'et.html', {'results': content['entries']})

def et_top_stories(request):
  return feedparser.parse(rss_et_top_stories)

def et_news(request):
  return feedparser.parse(rss_et_news)

def et_market(request):
  return feedparser.parse(rss_et_market)

def et_personal_finance(request):
  return feedparser.parse(rss_et_personal_finance)

def et_infotech(request):
  return feedparser.parse(rss_et_infotech)

def et_job(request):
  return feedparser.parse(rss_et_job)

def et_opinion(request):
  return feedparser.parse(rss_et_opinion)

def et_features(request):
  return feedparser.parse(rss_et_features)

def et_environment(request):
  return feedparser.parse(rss_et_environment)

def et_nri(request):
  return feedparser.parse(rss_et_nri)
