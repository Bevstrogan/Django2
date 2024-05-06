from django.core.management import BaseCommand
from catalog.models import Category, Product
import json
from django.db import connection


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open("categories.json", encoding="UTF-8") as file:
            data = json.load(file)
            return data

    @staticmethod
    def json_read_products():
        with open("product.json", encoding="UTF-8") as file:
            data = json.load(file)
            return data

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    id=category["pk"],
                    name=category["fields"]["name"],
                    description=category["fields"]["description"],
                )
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    id=product["pk"],
                    name=product["fields"]["name"],
                    description=product["fields"]["description"],
                    category=Category.objects.get(pk=product["fields"]["category"]),
                    price=product["fields"]["price"],
                )
            )
        Product.objects.bulk_create(product_for_create)
