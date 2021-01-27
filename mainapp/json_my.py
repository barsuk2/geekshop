import json

from mainapp.models import Product

with open('mainapp/fixtures/products.json') as f:
    context = json.load(f)
for i in context['products']:

    print(i['title'])

