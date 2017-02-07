from django.core.management.base import BaseCommand, CommandError
import csv
from .utils import process


class Command(BaseCommand):
    help = 'Import VOA data from a CSV file'

    def __init__(self, skip_header=False, encoding=None):
        self.skip_header = skip_header
        self.encoding = encoding

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def process_row(self, row):
        pass

    def handle(self, *args, **options):
        csv_file_name = options.get('csv_file')

        if csv_file_name:
            with open(
                    csv_file_name,
                    newline='', encoding=self.encoding) as csvfile:

                reader = csv.reader(csvfile, delimiter='*', quotechar='"')

                for record in process(reader):
                    print(record)
