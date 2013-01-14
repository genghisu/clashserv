from optparse import make_option
import sys
import json
from os.path import join,  dirname,  normpath
import datetime

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand
from django.test.utils import get_runner
from django.core.exceptions import ObjectDoesNotExist

from core.models import State, Lottery, Drawing, StateLottery

month_dict = {"Jan":1,"Feb":2,"Mar":3,"Apr":4, "May":5, "Jun":6,
        "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}

def contruct_date(month, day, year):
    return datetime.datetime(int('20%s' % (str(year))), int(month_dict.get(month)), int(day)) 

class Command(BaseCommand):
    help = 'Load initial lottery data.'
    args = []

    requires_model_validation = True

    def handle(self, *test_labels, **options):
        PROJECT_ROOT = join(dirname(normpath(__file__)), '..')
        
        DATA_DIR = join(PROJECT_ROOT, '../../../data')
        
        filename = join(DATA_DIR, 'lottery.json')
        
        data_file = open(filename)
        
        for lottery in json.loads(data_file.read()):
            try:
                lottery_object = Lottery.objects.get(name__iexact = lottery.get('fields').get('name'))
                fields = lottery.get('fields')
                for k, v in fields.items():
                    if not k == 'pk' and not k == 'next_draw_date':
                        setattr(lottery_object, k, v)
                print lottery_object.as_dict()
                lottery_object.save()
            except ObjectDoesNotExist:
                print lottery.get('fields').get('name')