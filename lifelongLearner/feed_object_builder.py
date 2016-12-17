import abc


class feed_object_builder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_author(self, authors_param):
        self.authors = authors_param

    @abc.abstractmethod
    def add_link(self, link_param):
        self.link = link_param

    @abc.abstractmethod
    def add_published_date(self, published_date_param):
        self.published_date = published_date_param

    @abc.abstractmethod
    def add_summary_detail(self, summary_detail_param):
        self.summary_detail = summary_detail_param

    @abc.abstractmethod
    def add_tags(self, tags_param):
        self.tags = tags_param

    @abc.abstractmethod
    def add_title(self, title_param):
        self.title = title_param

    @abc.abstractmethod
    def add_updated(self, updated_param):
        self.updated = updated_param