from django.core.management.base import BaseCommand, CommandError
from chat_ml.models import *
from django.db.models import F
from django.db.models.functions import Concat
from django.db.models import Value
class Command(BaseCommand):

    help = "update data"

    def handle(self, *args, **options):
        Jobs.objects.all().update(desc=Concat(F('desc'),Value(" For further information visit- http://www.soprasteria.in/careers/current-openings")))


