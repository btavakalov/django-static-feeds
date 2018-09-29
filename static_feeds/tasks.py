from datetime import timedelta

from celery.task import PeriodicTask

from static_feeds import conf
from static_feeds.generator import FeedsGenerator

if conf.CELERY_TASK_REPETITION:
    class GenerateFeeds(PeriodicTask):
        run_every = timedelta(minutes=conf.CELERY_TASK_REPETITION)

        def run(self, **kwargs):
            generator = FeedsGenerator(verbosity=2)
            generator.generate()
