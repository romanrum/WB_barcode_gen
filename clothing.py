def rewrite(clothing):
    if clothing == 'Топы':
        return 'Топ'
    elif clothing == 'Рубашки':
        return 'Рубашка'
    elif clothing == 'Юбки':
        return 'Юбка'
    elif clothing == 'Футболки':
        return 'Футболка'
    elif clothing == 'Топы спортивные':
        return 'Топ'
    elif clothing == 'Блузки':
        return 'Блузка'
    elif clothing == 'Водолазки':
        return 'Водолазка'
    elif clothing == 'Костюмы':
        return 'Костюм'
    elif clothing == 'Костюмы спортивные':
        return 'Костюм'
    elif clothing == 'Куртки':
        return 'Куртка'
    elif clothing == 'Свитшоты':
        return 'Свитшот'
    elif clothing == 'Сумки':
        return 'Сумка'
    else:
        return clothing

def colors(color, *art):
    if color == '001P0':
        return 'зеленый'
    elif color == '002P0' or color == '002Р0':
        return 'сине-серый'
    elif color == '003P0':
        return 'желтая охра'
    elif color == '004P0':
        return 'вишневый'
    elif color == '005P0':
        if art == 'WTR5KSH':
            return 'серый меланж'
        else:
            return 'голубой'
    elif color == '005P1' or color == '005Р1':
        return 'голубой'
    elif color == '006P0' or color == '006Р0':
        return 'хаки'
    elif color == '007P0' or color == '007P0/46':
        return 'черный'
    elif color == '007P1':
        return 'черный'
    elif color == '008P0' or color == '008P0/46':
        return 'лавандовый'
    elif color == '008P1':
        return 'лавандовый'
    elif color == '009P0':
        return 'оранжевый'
    elif color == '010P0' or color == '010P0/46':
        return 'белый'
    elif color == '011P0' or color == '011Р0':
        return 'какао'
    elif color == '011P1' or color == '011Р1':
        return 'какао'
    elif color == '013P0' or color == '013Р0':
        return 'графит'
    elif color == '013P1':
        return 'графит'
    elif color == '014P0' or color == '014Р0':
        return 'кирпичный'
    elif color == '015P0' or color == '015Р0':
        return 'голубой туман'
    elif color == '018P0' or color == '018Р0':
        return 'кремовый'
    elif color == '019P0':
        if art == 'RZK23KK':
            return 'зелено-серый'
        else:
            return 'серый меланж'
    elif color == '020P0':
        return 'белый'
    elif color == '021P0':
        return 'бежевый'
    elif color == '021P1':
        return 'белый'
    elif color == '022P0' or color == '022Р0':
        return 'фуксия'
    elif color == '024P0':
        return 'желто-оранжевый'
    elif color == '025P0':
        return 'лососевый'
    elif color == '029P0' or color == '029Р0':
        return 'красный'
    elif color == '030P0':
        return 'пудровый'
    elif color == '031P0':
        return 'белый'
    elif color == '038P0':
        return 'жемчужный'
    elif color == '039P0':
        return 'бежевый'
    elif color == '040P1':
        return 'оливковый'
    elif color == '041P0' or color == '041Р0':
        return 'красный'
    elif color == '042P0':
        return 'бронзовый'
    elif color == 'P0':
        if art == 'KL50':
            return 'белый'
        elif art == 'KP50':
            return 'серый'
    elif color == 'black':
        return 'черный'
    elif color == 'роз':
        return 'розовая пудра'
    elif color == '123546854':
        return 'розовая пудра'
    elif color == '65458789':
        return 'розовая пудра'
    elif color == '321654':
        return 'шоколадный'
    else:
        return '-'

