import json
# from pathlib import Path

from django.core.management import BaseCommand

from catalog.models import Product, Category


# path = Path(__file__).resove().parent.absolute() / 'data.json'

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog_data.json', encoding='utf-8') as file:
            data = json.load(file)['property']
            #print(data)
        return [item for item in data if item['model'] == 'catalog.category']

    @staticmethod
    def json_read_products():
        with open('catalog_data.json', encoding='utf-8') as file:
            data = json.load(file)['property']
            #print()
        return [item for item in data if item['model'] == 'catalog.product']

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'],
                         name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product["pk"],
                        name=product["fields"]["name"],
                        description=product["fields"]["description"],
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        price=product["fields"]["price"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)