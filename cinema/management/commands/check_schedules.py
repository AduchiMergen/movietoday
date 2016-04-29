from django.core.management.base import BaseCommand
from cinema.utils import check_schedules


class Command(BaseCommand):
    help = 'Check cinemas schedules'

    def handle(self, *args, **options):
        check_schedules()
