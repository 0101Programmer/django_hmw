from django.shortcuts import render


# Create your views here.

def main_page(request):
    main_title = 'videogames.net'
    main_header = 'Главная страница'
    main = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'main_title': main_title,
        'main_header': main_header,
        'main': main,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'main_page.html', context)


def shop_page(request):
    shop_title = 'videogames.net'
    shop_header = 'Игры'
    main = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    games_list = [
        'FarCause 9',
        'JustCry 8',
        'Call of Battlefield 15'
    ]
    buy = 'Купить!'
    back = 'Вернуться на главную'
    context = {
        'shop_title': shop_title,
        'shop_header': shop_header,
        'games_list': games_list,
        'buy': buy,
        'back': back,
        'main': main,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'shop_page.html', context)


def cart_page(request):
    cart_title = 'videogames.net'
    cart_header = 'Товары в корзине'
    none = 'Извините, но ваша корзина пуста'
    back = 'Вернуться на главную'
    main = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'cart_title': cart_title,
        'cart_header': cart_header,
        'none': none,
        'back': back,
        'main': main,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'cart_page.html', context)

