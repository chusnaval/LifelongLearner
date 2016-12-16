import feedparser
import datetime
from pymongo import MongoClient
import json


RSS_URL = "https://www.infoq.com/feed?token=LhCCgUeJIoT4WBAIY9MnddUVLi6BTD28"

feed = feedparser.parse(RSS_URL)

client = MongoClient('mongodb://localhost:27017/')

class FeedObject:
    authors = None
    link = None
    published_date = None
    summary_detail = None
    tags = None
    title = None

    def __repr__(self, *args, **kwargs):
        return super().__repr__(*args, **kwargs)

    updated = None

    def __init__(self, authors_param, link_param, published_date_param, summary_detail_param, tags_param, title_param, update_param):
        self.authors = [author['name'] for author in authors_param]
        self.link = link_param
        self.published_date = published_date_param
        self.summary_detail = summary_detail_param
        self.tags = [tag['term'] for tag in tags_param]
        self.title = title_param
        self.updated = update_param


    def feed_dict_str(self, list):
        return "Authors: ["
        for element in list:
            rep += '"' + element + '",'
        length = len(rep) - 1
        return rep[0: length] + "]"

    def __str__(self, *args, **kwargs):
        rep = self.feed_dict_str(self.authors)
        rep += "\nLink: " + self.link + "\nPublished Date: " + self.published_date + "\nSummary: " + self.summary_detail
        rep += "\nTags: " + self.feed_dict_str(self.tags)
        rep += "\nTitle: " + self.title + "\nUpdated: " + self.updated
        return rep



def process(self):
    db = client['lifelongLearner']
    posts = db.posts
    post = posts.find_one({"_id": self.link})
    if not post:
        post = {"_id": self.link,
                "Title": self.title,
                "Authors": self.authors,
                "Published Date": self.published_date,
                "Summary": self.summary_detail,
                "Tags": self.tags,
                "Updated": self.updated,
                "Inserted": datetime.datetime.utcnow()}
        post_id = posts.insert_one(post).inserted_id


for item in feed['items']:
    fo = FeedObject(item['authors'], item['link'], item['published'], item['summary'], item['tags'], item['title'], item['updated'])
    process(fo)
    print(fo)


