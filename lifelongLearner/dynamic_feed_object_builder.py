from lifelongLearner.core import FeedObject
from lifelongLearner.feed_object_builder import feed_object_builder


class dynamic_feed_object_builder(feed_object_builder):

    def create_feed_object(item):
        fo = FeedObject()
        if item.has_key('authors'):
            fo.authors = [author['name'] for author in item['authors']]
        if item.has_key('link'):
            fo.link = item['link']
        if item.has_key('published'):
            fo.published_date = item['published']
        if item.has_key('summary'):
            fo.summary_detail = item['summary']
        if item.has_key('tags'):
            fo.tags = [tag['term'] for tag in item['tags']]
        if item.has_key('title'):
            fo.title = item['title']
        if item.has_key('updated'):
            fo.updated = item['updated']
        return fo



