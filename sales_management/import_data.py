import json
from django.core.management.base import BaseCommand
from sales_management.data_importer import DataImporter

class Command(BaseCommand):
    help = 'Import test data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('directory_path', type=str, help='Path to the JSON file containing test data')

    def setUp(self):
        self.load_test_data()

    def handle(self, *args, **options):
        directory_path = options['directory_path']
        self.stdout.write(self.style.SUCCESS(f'Importing test data from {directory_path}'))
        DataImporter().import_data_files(directory_path=directory_path)
        self.stdout.write(self.style.SUCCESS('Successfully imported test data'))
