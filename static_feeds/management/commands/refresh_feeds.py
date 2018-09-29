from django.core.management.base import BaseCommand
from static_feeds.generator import FeedsGenerator


class Command(BaseCommand):
    command = None
    help = 'Generates feeds to a predefined directory.'

    def handle(self, *args, **options):
        generator = FeedsGenerator(int(options.get('verbosity', 2)))
        generator.generate()
