from django.core.management import BaseCommand
import json
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('categories.json', 'r', encoding="utf-8") as c_file:
            c_data = c_file.read()
            categories_list = json.loads(c_data)
            return categories_list


    @staticmethod
    def json_read_products():
        with open('product.json', 'r', encoding="utf-8") as p_file:
            p_data = p_file.read()
            products_list = json.loads(p_data)
            return products_list

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        categories_for_create = []
        products_for_create = []

        for category_item in Command.json_read_categories():
            categories_for_create.append(Category(**category_item['fields']))

        Category.objects.bulk_create(categories_for_create)

        for product_item in Command.json_read_products():
            products_for_create.append(Product(name=product_item['fields']['name'],
                                               description=product_item['fields']['description'],
                                               image=product_item['fields']['image_preview'],
                                               category=Category.objects.get(pk=product_item['fields']['category']),
                                               price=product_item['fields']['price']))

        Product.objects.bulk_create(products_for_create)