from django.shortcuts import render


# Create your views here.

def main_page(request):
    title = 'videogames.net'
    main_p = 'Главная страница'
    main = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'title': title,
        'main_p': main_p,
        'main': main,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'main_page.html', context)


def shop_page(request):
    title = 'videogames.net'
    main = 'Игры'
    game1 = 'FarCause 9'
    game2 = 'JustCry 8'
    game3 = 'Call of Battlefield 15'
    buy = 'Купить!'
    back = 'Вернуться на главную'
    context = {
        'title': title,
        'main': main,
        'game1': game1,
        'game2': game2,
        'game3': game3,
        'buy': buy,
        'back': back
    }
    return render(request, 'shop_page.html', context)


def cart_page(request):
    title = 'videogames.net'
    main = 'Товары в корзине'
    none = 'Извините, но ваша корзина пуста'
    back = 'Вернуться на главную'
    context = {
        'title': title,
        'main': main,
        'none': none,
        'back': back
    }
    return render(request, 'cart_page.html', context)
