import random
from code.keyboards import *
from code.methods_vk import *

bibl = False
# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Логика ответа
            # когда попытка перепрыгнуть, бросает на первое окно

            if order.time != "none" and bibl:
                vk.method("messages.send",
                          {"peer_id": event.user_id, "message": "Введите ваш номер телефона:",
                           "random_id": random.randint(100000, 999999), "keyboard": keyboard_to_home})
                order.number_of_passengers = request
                bibl = False
            else:
                bibl = False
                if "ривет" in request:
                    vk.method("messages.send",
                              {"peer_id": event.user_id, "message": "Привет =)",
                               "random_id": random.randint(100000, 999999)})
                elif "ачать" in request or "tart" in request:
                    vk.method("messages.send",
                              {"peer_id": event.user_id, "message": "Привет",
                               "random_id": random.randint(100000, 999999),
                               "keyboard": keyboard_start})
                elif request == "Домой" or request == "домой":
                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Вы в лавном меню. Для заказа автобуса наберите слово «заказ»",
                               "random_id": random.randint(100000, 999999), "keyboard": keyboard_start})
                    order.reset(order)


                # Если получено "Заказать автобус"
                elif "аказ" in request:
                    vk.method("messages.send",
                              {"peer_id": event.user_id, "message": "Выберите город отправления:",
                               "random_id": random.randint(100000, 999999)})
                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Доступные города: Казань, Набережные Челны, Буинск.",
                               "random_id": random.randint(100000, 999999), "keyboard": keyboard_city})
                    order.reset(order)
                # Если нажали "Подробнее"
                elif "одробнее" in request:
                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Заказ автобусов в Казань, Набережные Челны и Буинск. Отправка каждый час от вашей остановки. Стоимость проезда 400 рублей. Студентам скидка 50 рублей.",
                               "random_id": random.randint(100000, 999999), "keyboard": keyboard_start})
                    order.reset(order)
                elif ("Казан" in request or "казан" in request):
                    if order.city1 == "none":
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Заказ автобуса из Казани. Выберите город прибытия:",
                                   "random_id": random.randint(100000, 999999)})
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Доступные города: Набережные Челны, Буинск.",
                                   "random_id": random.randint(100000, 999999), "keyboard": keyboard_city_kazan})
                        order.city1 = "Казань"
                    elif order.city1 == "Челны":
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Заказ автобуса в Казань.",
                                   "random_id": random.randint(100000, 999999)})
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Выберите остановку: кафе «Уют», 30 комплекс, Школа, ДК Камаз, ШШК, Парк Победы, Молодежная, Театр Кукол, Райисполком, 6 комплекс, Ершова, УВД, 7 комплекс, Студенческий квартал, КамПи, Мед.городок, Детский медицинский центр Электротехников, Нариманова, Орловка, Пед.институт, Бумажников, Центральная, Универсам, Студенческая, Парк Культуры, Поликлиника",
                                   "random_id": random.randint(100000, 999999), "keyboard": keyboard_stop_chelny})
                        order.city2 = "Казань"
                    elif order.city1 == "Буинск":
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Заказ автобуса в Казань.",
                                   "random_id": random.randint(100000, 999999)})
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Выберите остановку: «Встреча», Магазин Альбина, Медресе, Мечеть, Ледовый дворец, Магазин Айдар, Больница, Магазин Татьяна, Кольцо, Моторный завод",
                                   "random_id": random.randint(100000, 999999), "keyboard": keyboard_stop_buinsk})
                        order.city2 = "Казань"

                elif "Челны" in request or "челны" in request or "Чаллы" in request:
                    if order.city1 == "none":
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Заказ автобуса из Набережных Челнов.",
                                   "random_id": random.randint(100000, 999999)})
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Выберите город прибытия: Казань",
                                   "random_id": random.randint(100000, 999999), "keyboard": keyboard_city_chelny})
                        order.city1 = "Челны"
                    else:
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Заказ автобуса в Набережные Челны.",
                                   "random_id": random.randint(100000, 999999)})
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Выберите остановку: Автовокзал Восточный, ЖД Вокзал, Театр Камала, ТЦ Кольцо, Парк Горького, Советская площадь, Клыки Причал, Эдельвейс.",
                                   "random_id": random.randint(100000, 999999),
                                   "keyboard": keyboard_stop_kazan_to_chelny})
                        order.city2 = "Челны"

                elif "Буинск" in request or "буинск" in request or "Буа" in request:
                    if order.city1 == "none":  # едем из Буинска
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Заказ автобуса из Буинска.",
                                   "random_id": random.randint(100000, 999999)})
                        vk.method("messages.send",
                                  {"peer_id": event.user_id,
                                   "message": "Выберите город прибытия: Казань",
                                   "random_id": random.randint(100000, 999999), "keyboard": keyboard_city_buinsk})
                        order.city1 = "Буинск"
                    else:  # едем в Буинск
                        if order.city1 != "Буинск":
                            vk.method("messages.send",
                                      {"peer_id": event.user_id,
                                       "message": "Заказ автобуса в Буинск.",
                                       "random_id": random.randint(100000, 999999)})
                            vk.method("messages.send",
                                      {"peer_id": event.user_id,
                                       "message": "Выберите осстановку: Автостанция, Яхина 5а, Речной техникум, Ягодная слобода, Фрунзе, Идель, Школа, Телевышка, Бахетле.",
                                       "random_id": random.randint(100000, 999999),
                                       "keyboard": keyboard_stop_kazan_to_buinsk})
                            order.city2 = "Буинск"
                # Если получено время
                elif is_time(request) and order.city1 != "none" and order.city2 != "none":
                    vk.method("messages.send",
                              {"peer_id": event.user_id, "message": "Сколько нужно мест?",
                               "random_id": random.randint(100000, 999999), "keyboard": keyboard_people})
                    order.time = request
                    bibl = True


                # Если пришло "Ввести количество" (людей)
                # код...

                # Если прислали телефонный номер
                elif is_phoneNumber(request):
                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Заказ принят! Автобус будет ожидать вас на выбранной остановке.",
                               "random_id": random.randint(100000, 999999), "keyboard": keyboard_start})
                    order.phone_number = request
                    # отправка заказа в базу данных
                    # код...
                    order.reset(order)

                # Вывод информации для админа
                elif request == "info":
                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": order.city1 + " " + order.city2 + " " + order.time + " " + order.number_of_passengers + " " + order.phone_number,
                               "random_id": random.randint(100000, 999999)})

                elif isInKazanCh(request) and order.city1 == "Казань":
                    print("зашло в Казань-Челны")
                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Вы выбрали остановку: " + searchInKazanCh(request) + ".",
                               "random_id": random.randint(100000, 999999)})

                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Выберите время: " + kznCh[searchInKazanCh(request)][0] + ", " +
                                          kznCh[searchInKazanCh(request)][1] + ", " + kznCh[searchInKazanCh(request)][
                                              2] + ", " + kznCh[searchInKazanCh(request)][3] + ", " +
                                          kznCh[searchInKazanCh(request)][4] + ", " + kznCh[searchInKazanCh(request)][
                                              5] + ".",
                               "random_id": random.randint(100000, 999999),
                               "keyboard": keyboardsStopsKznCh(searchInKazanCh(request))})
                elif isInBuinsk(request) and order.city1 == "Буинск":
                    print("сработало elif Буинск")
                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Вы выбрали остановку: " + searchInBuinsk(request) + ".",
                               "random_id": random.randint(100000, 999999)})

                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Выберите время: " + buKzn[searchInBuinsk(request)][0] + ", " +
                                          buKzn[searchInBuinsk(request)][1] + ", " + buKzn[searchInBuinsk(request)][
                                              2] + ", " + buKzn[searchInBuinsk(request)][3] + ".",
                               "random_id": random.randint(100000, 999999),
                               "keyboard": keyboardsStopsBua(searchInBuinsk(request))})

                elif isInChelnyKazan(request) and order.city1 == "Челны":
                    print("сработало elif Челны-Казань")
                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Вы выбрали остановку: " + searchInChelnyKazan(request) + ".",
                               "random_id": random.randint(100000, 999999)})

                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Выберите время: " + chelnyKazan[searchInChelnyKazan(request)][0] + ", " +
                                          chelnyKazan[searchInChelnyKazan(request)][1] + ", " + chelnyKazan[searchInChelnyKazan(request)][
                                              2] + ", " + chelnyKazan[searchInChelnyKazan(request)][3] + ", " + chelnyKazan[searchInChelnyKazan(request)][4] + ", " + chelnyKazan[searchInChelnyKazan(request)][5] + ", " + chelnyKazan[searchInChelnyKazan(request)][6] + ".",
                               "random_id": random.randint(100000, 999999),
                               "keyboard": keyboardsStopsTimesChelny(searchInChelnyKazan(request))})

                elif isInKazanBua(request) and order.city1 == "Казань":
                    print("сработало elif Казань-Буинск")
                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Вы выбрали остановку: " + searchInKazanBua(request) + ".",
                               "random_id": random.randint(100000, 999999)})
                    #print("сработал searchInKazanBua")

                    vk.method("messages.send",
                              {"peer_id": event.user_id,
                               "message": "Выберите время: " + kazanBua[searchInKazanBua(request)][0] + ", " +
                                          kazanBua[searchInKazanBua(request)][1] + ", " +
                                          kazanBua[searchInKazanBua(request)][2] + ", " +
                                          kazanBua[searchInKazanBua(request)][3] + ".",
                               "random_id": random.randint(100000, 999999),
                               "keyboard": keyboardsStopsKazanBua(searchInKazanBua(request))})

                else:
                    # write_msg(event.user_id, "Не поняла вашего ответа... Для возврата в главное меню наберите "Домой")
                    vk.method("messages.send", {"peer_id": event.user_id,
                                                "message": "Не поняла вашего ответа... Для возврата в главное меню наберите слово «домой»",
                                                "random_id": random.randint(1, 999999)})
