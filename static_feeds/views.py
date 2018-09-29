import os
from django.contrib.syndication.views import Feed
from django.http import HttpResponse
from static_feeds import conf
from static_feeds.util import _lazy_load


class StaticFeed(Feed):
    def __call__(self, request, *args, **kwargs):
        try:
            storage = _lazy_load(conf.STORAGE_CLASS)(location=conf.ROOT_DIR)
        except TypeError:
            storage = _lazy_load(conf.STORAGE_CLASS)()

        path = os.path.join(conf.ROOT_DIR, request.path.strip('/'))

        if not storage.exists(path):
            return super().__call__(request, *args, **kwargs)

        f = storage.open(path)
        content = f.readlines()
        f.close()

        return HttpResponse(content, content_type=self.feed_type.content_type)
