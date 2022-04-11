import random
from string import Template
class baze_of_records:         #КАЛЬКУЛЯТОР ДЛЯ пирамиды из банок
    """Здесь хранятся данные о
    бюджете,цене за бутылку,
    общем чеке,кол-ве банок
    и уровне,на котором они стоят"""

    def __init__(self,bonus,price):
        self.bonus = bonus
        self.price = price
        self.check = 0
        self.banki = 0
        self.plita = 0

def beeramid():
    """Функция калькулятор"""
    """Количество банок на уровне = №-уровня возведённый в квадрат"""
    class_ = baze_of_records(bonus=int(input('Каков бюджет?\n')),price=int(random.randint(2,5)))
    information_of_price= f'Цена сегодня:$today'
    print(Template(information_of_price).substitute(today = class_.price))
    while class_.bonus - class_.check >= 0:           #пока кошель не опустел,сидим до талого
        class_.plita +=1                       #можем попробовать собрать новый уровень
        class_.banki = class_.plita**2                #высчитываем банки
        class_.check += class_.banki * class_.price          #нам считают чек
        if(class_.bonus - class_.check < 0):          #если по итогу не хватило...
            class_.plita -= 1                  #уровень,на который замахнулись,не засчитывается
        else:
            pass                        #пропуск если хватило
    return class_.plita

m = beeramid()
print(m)