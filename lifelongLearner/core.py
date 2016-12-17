import feedparser
import datetime
from pymongo import MongoClient

import json

client = MongoClient('mongodb://localhost:27017/')


class FeedURL:
    url = None
    items = []
    type = None

    def __init__(self, url_param, items_param, type_param):
        self.url = url_param
        self.items = items_param
        self.type = type_param


class FeedObject:
    authors = None
    link = None
    published_date = None
    summary_detail = None
    tags = None
    title = None
    updated = None

    def __repr__(self, *args, **kwargs):
        return super().__repr__(*args, **kwargs)


    def feed_dict_str(self, list):
        rep = "Authors: ["
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



def insert_feed_objects(feed_objects):
    for feed_object in feed_objects:
        db = client['lifelongLearner3']
        posts = db.posts
        post = posts.find_one({"_id": feed_object.link})
        if not post:
            post = {"_id": feed_object.link,
                    "Title": feed_object.title,
                    "Authors": feed_object.authors,
                    "Published Date": feed_object.published_date,
                    "Summary": feed_object.summary_detail,
                    "Tags": feed_object.tags,
                    "Updated": feed_object.updated,
                    "Inserted": datetime.datetime.utcnow()}
            post_id = posts.insert_one(post).inserted_id


def obtain_feed_urls():
    feeds = []
    with open('feeds.json') as data_file:
        data = json.load(data_file)
        for item in iter(data['feeds']):
            feeds.append(FeedURL(item['url'], feedparser.parse(item['url'])['items'], item['type']))
    return  feeds


def convert_url_to_feed_object(feed_url):
    feed_objects = []
    for item in feed_url.items:
        from lifelongLearner.dynamic_feed_object_builder import dynamic_feed_object_builder
        fo = dynamic_feed_object_builder.create_feed_object(item)
        feed_objects.append(fo)
    return feed_objects


def process_feed_url(feed_url):
    feed_objects = convert_url_to_feed_object(feed_url)
    insert_feed_objects(feed_objects)
    print(feed_objects)


def main():
    feeds_urls = obtain_feed_urls()
    for feed_url in feeds_urls:
        process_feed_url(feed_url)

if __name__ == '__main__':
    main()
