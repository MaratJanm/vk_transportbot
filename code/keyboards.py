keyboard_start = {
    "one_time": False,  # неисчезающий
    "buttons": [

        [new_button(label="Заказать автобус", color="positive")],
        [new_button(label="Подробнее", color="negative")]

    ]
}
keyboard_start = json.dumps(keyboard_start, ensure_ascii=False).encode('utf-8')
keyboard_start = str(keyboard_start.decode('utf-8'))

keyboard_to_home = {
    "one_time": False,  # неисчезающий
    "buttons": [

        [new_button(label="Домой", color="negative")]

    ]
}
keyboard_to_home = json.dumps(keyboard_to_home, ensure_ascii=False).encode('utf-8')
keyboard_to_home = str(keyboard_to_home.decode('utf-8'))

keyboard_city_kazan = {
    "one_time": False,  # исчезающий
    "buttons": [

        [new_button(label="Набережные Челны", color="primary")],
        [new_button(label="Буинск", color="primary")],
        [new_button(label="Домой", color="negative")]

    ]
}
keyboard_city_kazan = json.dumps(keyboard_city_kazan, ensure_ascii=False).encode('utf-8')
keyboard_city_kazan = str(keyboard_city_kazan.decode('utf-8'))

keyboard_city = {
    "one_time": False,  # исчезающий
    "buttons": [

        [new_button(label="Казань", color="primary")],
        [new_button(label="Набережные Челны", color="primary")],
        [new_button(label="Буинск", color="primary")],
        [new_button(label="Домой", color="negative")]

    ]
}
keyboard_city = json.dumps(keyboard_city, ensure_ascii=False).encode('utf-8')
keyboard_city = str(keyboard_city.decode('utf-8'))

keyboard_city_chelny = {
    "one_time": False,  # исчезающий
    "buttons": [

        [new_button(label="Казань", color="primary")],
        [new_button(label="Домой", color="negative")]

    ]
}
keyboard_city_chelny = json.dumps(keyboard_city_chelny, ensure_ascii=False).encode('utf-8')
keyboard_city_chelny = str(keyboard_city_chelny.decode('utf-8'))

keyboard_city_buinsk = {
    "one_time": False,  # исчезающий
    "buttons": [
        [new_button(label="Казань", color="primary")],
        [new_button(label="Домой", color="negative")]

    ]
}
keyboard_city_buinsk = json.dumps(keyboard_city_buinsk, ensure_ascii=False).encode('utf-8')
keyboard_city_buinsk = str(keyboard_city_buinsk.decode('utf-8'))

keyboard_stop_kazan_to_chelny = {
    "one_time": False,  # исчезающий
    "buttons": [

        [new_button(label="Автовокзал Восточный", color="primary"),
         new_button(label="ЖД Вокзал", color="primary")],
        [new_button(label="Театр Камала", color="primary"),
         new_button(label="ТЦ Кольцо", color="primary")],
        [new_button(label="Парк Горького", color="primary"),
         new_button(label="Советская площадь", color="primary")],
        [new_button(label="Клыки Причал", color="primary"),
         new_button(label="Эдельвейс", color="primary")],
        [new_button(label="Домой", color="negative")]

    ]
}
keyboard_stop_kazan_to_chelny = json.dumps(keyboard_stop_kazan_to_chelny, ensure_ascii=False).encode('utf-8')
keyboard_stop_kazan_to_chelny = str(keyboard_stop_kazan_to_chelny.decode('utf-8'))

keyboard_stop_kazan_to_buinsk = {
    "one_time": False,  # исчезающий
    "buttons": [

        [new_button(label="Автостанция, Яхина 5а", color="primary"),
         new_button(label="Речной техникум", color="primary")],
        [new_button(label="Ягодная слобода", color="primary"),
         new_button(label="Фрунзе", color="primary")],
        [new_button(label="Идель", color="primary"),
         new_button(label="Школа", color="primary")],
        [new_button(label="Телевышка", color="primary"),
         new_button(label="Бахетле", color="primary")],
        [new_button(label="Домой", color="negative")]

    ]
}
keyboard_stop_kazan_to_buinsk = json.dumps(keyboard_stop_kazan_to_buinsk, ensure_ascii=False).encode('utf-8')
keyboard_stop_kazan_to_buinsk = str(keyboard_stop_kazan_to_buinsk.decode('utf-8'))

keyboard_stop_chelny = {
    "one_time": False,  # исчезающий
    "buttons": [
        [new_button(label="кафе «Уют»", color="primary"),
        new_button(label="30 комплекс", color="primary"),
        new_button(label="Школа", color="primary")],
        [new_button(label="ДК Камаз", color="primary"),
        new_button(label="ШШК", color="primary"),
        new_button(label="Парк Победы", color="primary")],
        [new_button(label="Молодежная", color="primary"),
        new_button(label="Театр Кукол", color="primary"),
        new_button(label="Райисполком", color="primary")],
        [new_button(label="6 комплекс", color="primary"),
        new_button(label="Ершова", color="primary"),
        new_button(label="УВД", color="primary")],
        [new_button(label="7 комплекс", color="primary"),
        new_button(label="Студенческий квартал", color="primary"),
        new_button(label="КамПи", color="primary")],
        [new_button(label="Мед.городок", color="primary"),
        new_button(label="Детский медицинский центр", color="primary"),
        new_button(label="Электротехников", color="primary")],
        [new_button(label="Нариманова", color="primary"),
        new_button(label="Орловка", color="primary"),
        new_button(label="Пед.институт", color="primary")],
        [new_button(label="Бумажников", color="primary"),
        new_button(label="Центральная", color="primary"),
        new_button(label="Универсам", color="primary")],
        [new_button(label="Студенческая", color="primary"),
        new_button(label="Парк Культуры", color="primary"),
        new_button(label="Поликлиника", color="primary")],
        [new_button(label="Домой", color="negative")]

    ]
}
keyboard_stop_chelny = json.dumps(keyboard_stop_chelny, ensure_ascii=False).encode('utf-8')
keyboard_stop_chelny = str(keyboard_stop_chelny.decode('utf-8'))

keyboard_stop_buinsk = {
    "one_time": False,  # исчезающий
    "buttons": [

        [new_button(label="«Встреча»", color="primary"),
         new_button(label="Магазин Альбина", color="primary")],
        [new_button(label="Медресе", color="primary"),
         new_button(label="Мечеть", color="primary")],
        [new_button(label="Ледовый дворец", color="primary"),
         new_button(label="Магазин Айдар", color="primary")],
        [new_button(label="Больница", color="primary"),
         new_button(label="Магазин Татьяна", color="primary")],
        [new_button(label="Кольцо", color="primary"),
         new_button(label="Моторный завод", color="primary")],
        [new_button(label="Домой", color="negative")]

    ]
}
keyboard_stop_buinsk = json.dumps(keyboard_stop_buinsk, ensure_ascii=False).encode('utf-8')
keyboard_stop_buinsk = str(keyboard_stop_buinsk.decode('utf-8'))

keyboard_people = {
    "one_time": True,  # исчезающий
    "buttons": [

        [new_button(label="Один человек", color="primary"),
        new_button(label="Два человека", color="primary")],
        [new_button(label="Три человека", color="primary"),
        new_button(label="Четыре человека", color="primary")],
        [new_button(label="Больше", color="primary")],
        [new_button(label="Домой", color="negative")]

    ]
}
keyboard_people = json.dumps(keyboard_people, ensure_ascii=False).encode('utf-8')
keyboard_people = str(keyboard_people.decode('utf-8'))




def keyboardsStopsKznCh(buStop):
    boardKzn = {
        "one_time": False,  # исчезающий
        "buttons": [

            [new_button(label=kznCh[buStop][0], color="primary"),
            new_button(label=kznCh[buStop][1], color="primary"),
            new_button(label=kznCh[buStop][2], color="primary")],
            [new_button(label=kznCh[buStop][3], color="primary"),
            new_button(label=kznCh[buStop][4], color="primary"),
            new_button(label=kznCh[buStop][5], color="primary")],
            [new_button(label=kznCh[buStop][6], color="primary"),
            new_button(label="Домой", color="negative")]

        ]
    }
    boardKzn = json.dumps(boardKzn, ensure_ascii=False).encode('utf-8')
    boardKzn = str(boardKzn.decode('utf-8'))
    return boardKzn
def keyboardsStopsBua(buStop): #времена отправления с конкретной остановки
    boardBua = {
        "one_time": False,  # исчезающий
        "buttons": [

            [new_button(label=buKzn[buStop][0], color="primary"),
            new_button(label=buKzn[buStop][1], color="primary"),
            new_button(label=buKzn[buStop][2], color="primary")],
            [new_button(label=buKzn[buStop][3], color="primary"),
            new_button(label="Домой", color="negative")]

        ]
    }
    boardBua = json.dumps(boardBua, ensure_ascii=False).encode('utf-8')
    boardBua = str(boardBua.decode('utf-8'))
    return boardBua

def keyboardsStopsTimesChelny(chStop): #времена отправления с конкретной остановки
    boardChelny = {
        "one_time": False,  # исчезающий
        "buttons": [

            [new_button(label=chelnyKazan[chStop][0], color="primary"),
             new_button(label=chelnyKazan[chStop][1], color="primary"),
             new_button(label=chelnyKazan[chStop][2], color="primary")],
            [new_button(label=chelnyKazan[chStop][3], color="primary"),
             new_button(label=chelnyKazan[chStop][4], color="primary"),
             new_button(label=chelnyKazan[chStop][5], color="primary")],
            [new_button(label=chelnyKazan[chStop][6], color="primary"),
             new_button(label="Домой", color="negative")]

        ]
    }
    boardChelny = json.dumps(boardChelny, ensure_ascii=False).encode('utf-8')
    boardChelny = str(boardChelny.decode('utf-8'))
    return boardChelny

def keyboardsStopsKazanBua(buStop):
    boardKazanBua = {
        "one_time": False,  # исчезающий
        "buttons": [

            [new_button(label=kazanBua[buStop][0], color="primary"),
            new_button(label=kazanBua[buStop][1], color="primary"),
            new_button(label=kazanBua[buStop][2], color="primary")],
            [new_button(label=kazanBua[buStop][3], color="primary"),
            new_button(label="Домой", color="negative")]

        ]
    }
    boardKazanBua = json.dumps(boardKazanBua, ensure_ascii=False).encode('utf-8')
    boardKazanBua = str(boardKazanBua.decode('utf-8'))
    return boardKazanBua


