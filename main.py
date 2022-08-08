from classes import Store, Shop, Request


def main():

    store_1 = Store(
        {
            'печеньки': 50,
            'шоколадки': 10,
            'машинки': 7,
            'жевачки': 5,
            'мармеладки': 4,
            'круасаны': 6,
        }
    )

    store_2 = Store(
        {
            'печеньки': 30,
            'шоколадки': 20,
            'жевачки': 10,
            'мармеладки': 7,
            'круасаны': 10,
        }
    )

    shop = Shop(
        {}
    )

    print('Добрый день!')
    while True:
        print('Пожалуйста, введите запрос на перемещение или СТОП чтобы выйти')

        userinput = input()
        if userinput == 'СТОП':
            break

        success = False

        try:
            request = Request([store_1, store_2, shop], userinput)
            if eval(request.xfrom).remove(request.product, request.amount):
                if eval(request.to).add(request.product, request.amount):
                    success = True
                else:
                    eval(request.xfrom).add(request.product, request.amount)
        except:
            print('Оформите строку в формате: "Доставить 3 печеньки из склад в магазин".')
            print('Используйте правильные названия пунктов.')

        if success:
            print(f'Нужное количество есть в {request.xfrom}')
            print(f'Курьер забрал {request.amount} {request.product} из {request.xfrom}')
            print(f'Курьер везет {request.amount} {request.product} из {request.xfrom} в {request.to}')
            print(f'Курьер доставил {request.amount} {request.product} в {request.to}')

            print(f'В {request.xfrom} хранится:')
            print(eval(request.xfrom))
            print(f'В {request.to} хранится:')
            print(eval(request.to))


if __name__ == "__main__":
    main()
