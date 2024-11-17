from django.core.management.base import BaseCommand
from .utils import get_holidays_from_site, save_holidays_to_db

class Command(BaseCommand):
    help = "Fetch and save holidays"

    def handle(self, *args, **kwargs):
        url = 'https://site-com-feriados.com'
        holidays = get_holidays_from_site(url)
        save_holidays_to_db(holidays)
        self.stdout.write(self.style.SUCCESS)