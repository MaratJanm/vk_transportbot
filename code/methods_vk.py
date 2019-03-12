import re
import vk_api
from code.config import *
from vk_api.longpoll import VkLongPoll, VkEventType

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token_vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})


# Работа с сообщениями
longpoll = VkLongPoll(vk)


class order:
    city1 = "none"
    city2 = "none"
    stop = "none"
    time = "none"
    number_of_passengers = "none"
    phone_number = "none"

    def reset(self):
        self.city1 = "none"
        self.city2 = "none"
        self.stop = "none"
        self.time = "none"
        self.number_of_passengers = "none"
        self.phone_number = "none"
        pass


def is_phoneNumber(request):
    if len(request) > 4 and (re.fullmatch('[0-9]*', request) or request[0] == '+'):
        return True
    else:
        return False
    pass


def is_time(request):
    #проверяет, имеет ли значение формат времени
    if len(request) > 2 and len(request) < 6 and re.search('[0-9]*', request) and re.search(':', request):
        return True
    else:
        return False
    pass


def isInKazanCh(request):
    #принимает "ольцо" возвращает есть ли похожая остановка
    for each in kznChKeys:
        if each in request:
            return True
    return False

def searchInKazanCh(request):
    #принимает "ольцо" возвращает "ТЦ Кольцо"
    for each in kznChKeys:
        if each in request:
            return kznChKeys[each]
    return False

def isInBuinsk(request):
    #принимает "ольцо" возвращает есть ли похожая остановка
    for each in buKznKeys:
        if each in request:
            return True
    return False

def searchInBuinsk(request):
    #принимает "ольцо" возвращает "ТЦ Кольцо"
    for each in buKznKeys:
        if each in request:
            return buKznKeys[each]
    return False

def isInKazanBua(request):
    #принимает "ольцо" возвращает есть ли похожая остановка
    for each in kazanBuaKeys:
        if each in request:
            return True
    return False

def searchInKazanBua(request):
    #принимает "ольцо" возвращает "ТЦ Кольцо"
    for each in kazanBuaKeys:
        if each in request:
            return kazanBuaKeys[each]
    return False
def isInChelnyKazan(request):
    for each in chelnyKazanKeys:
        if each in request:
            return True
    return False
def searchInChelnyKazan(request):
    #принимает "оликлиника" возвращает "Поликлиника"
    for each in chelnyKazanKeys:
        if each in request:
            return chelnyKazanKeys[each]
    return False

