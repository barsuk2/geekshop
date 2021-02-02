import json

from django.shortcuts import render
from mainapp.models import Product as P, ProductCategory as PS


# Create your views here.
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    # context = {'title': 'GeekShop - Каталог',
    #            'products': [{'title': 'Худи черного цвета с монограммами adidas Originals',
    #                          'desc': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
    #                          'price': '6 090,00', 'img': 'Adidas-hoodie.png'},
    #                         {'title': 'Синяя куртка The North Face',
    #                          'desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
    #                          'price': '23 725,00', 'img': 'Blue-jacket-The-North-Face.png'},
    #                         {'title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
    #                          'desc': 'Материал с плюшевой текстурой. Удобный и мягкий.', 'price': '3 390,00',
    #                          'img': 'Brown-sports-oversized-top-ASOS-DESIGN.png'},
    #                         {'title': 'Черный рюкзак Nike Heritage спортивный oversized-топ ASOS DESIGN',
    #                          'desc': 'Плотная ткань. Легкий материал.', 'price': '2 340,00',
    #                          'img': 'Black-Nike-Heritage-backpack.png'},
    #
    #                         {'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
    #                          'desc': 'Гладкий кожаный верх. Натуральный материал.', 'price': '13 590,00',
    #                          'img': 'Black-Dr-Martens-shoes.png'},
    #
    #                         {'title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
    #                          'desc': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'price': '2 890,00',
    #                          'img': 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}]}
    # with open('mainapp/fixtures/products.json') as f:
    #     context = json.load(f)
    # for item in context['products']:
    #     P.objects.create(name=item['title'], image= 'products_images/'+item['img'],short_description= item['desc'], price= int(item['price'].replace(' ','')[0:-3]))
    #
    category = PS.objects.all()
    products = P.objects.all()
    context = {'title': 'GeekShop-каталог', 'category': category, 'products':products}
    return render(request, 'mainapp/products.html', context=context)


