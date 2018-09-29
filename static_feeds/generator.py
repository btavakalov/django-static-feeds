import logging
from django.test import Client, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.core.files.base import ContentFile
from static_feeds import conf
from static_feeds.util import _lazy_load

logger = logging.getLogger()


class FeedsGenerator(object):
    def __init__(self, verbosity):
        self.verbosity = verbosity
        self.has_changes = False
        self.request = RequestFactory().get('/')
        self.request.user = AnonymousUser()
        try:
            self.storage = _lazy_load(conf.STORAGE_CLASS)(location=conf.ROOT_DIR)
        except TypeError:
            self.storage = _lazy_load(conf.STORAGE_CLASS)()

        self.feeds = conf.FEEDS_URLS

    def out(self, string, min_level=1):
        if self.verbosity >= min_level:
            print(string)

    def write(self, path, output):
        self.out('Writing feed %s' % path, 2)
        self.storage.save(path.strip('/'), ContentFile(output))

    def generate(self):
        self.out('Generating feeds.', 1)
        for url in self.feeds:
            feed_content = self.get_feed(url)
            if feed_content:
                self.write(url, feed_content)
            else:
                self.out('Failed get feed %s' % url, 2)
        self.out('Finished generating feeds.', 1)

    def get_feed(self, path):
        self.storage.delete(path.strip('/'))
        response = Client().get(path)
        if response.status_code == 200:
            return response.content
        else:
            return False
