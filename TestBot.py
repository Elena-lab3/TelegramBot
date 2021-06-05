import telebot
import datetime
import DAO
from telebot import types

choice = 0
chat_id = 0

schedule_dao = DAO.ScheduleDAO()
myGroupUrl = 'https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup='
baseUrl = 'https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup='


class TimeTableGR1:
    def __init__(self, day, id):
        self.day = day
        self.id = id

    def info(self):
        if self.day == 0:
            bot.send_message(self.id,
                             '📚Понедельник:\n\n08:00 - 09:35\nМЛ(ЛК) Егорова Н. Г. \n108-4\n\n09:45 - 11:20\nФизК(ПЗ)\n\n11:40 - 13:15\nИнЯз(ПЗ)\n\n13:25 - 15:00(1 3)\nММА(ПЗ) Теслюк В. Н.\n321-4\n\n13:25 - 15:00(2 4)\nБелЯз КР(ПЗ) Дапиро Т. П.\n312-4')
        if self.day == 1:
            bot.send_message(self.id,
                             '📚Вторник:\n\n09:45 - 11:20\nКЧ(ПЗ) Клыбик П. М.\n111-4\n\n11:40 - 13:15\nМГиА(ЛК) Стройникова Е. Д.\n108-4\n\n13:25 - 15:00\nММА(ЛК) Анисимов В. Я.\n108-4')
        if self.day == 2:
            bot.send_message(self.id,
                             '📚Среда:\n\n08:00 - 09:35\nМЛ(ПЗ) Егорова Н. Г.\n322-4\n\n09:45 - 11:20\nФизК(ПЗ)\n\n11:40 - 13:15\nИнЯз(ПЗ)\n\n13:25 - 15:00\nММА(ПЗ) Теслюк В. Н.\n427-4')
        if self.day == 3:
            bot.send_message(self.id,
                             '📚Четверг:\n\n08:00 - 09:35(2 4)\nОАиП(ЛР) Пашук А. В.\n111-4\n\n09:45 - 11:20(2 4)\nПрогр-е(ЛР) Удовин И. А.\n221-5\n\n11:40 - 13:15(1 3)\nЛогика(ЛК) Дисько-Шуман М. Р.\n209-4\n\n11:40 - 13:15(2 4)\nММА(ЛК) Анисимов В. Я.\n209-4\n\n13:25 - 15:00\nПрогр-е(ЛК) Стаховский С. М.\n209-4')
        if self.day == 4:
            bot.send_message(self.id,
                             '📚Пятница:\n\n08:00 - 09:35(1 3)\nИСП(ЛК) Бережнов Д. Е.\n04-4\n\n08:00 - 09:35(2 4)\nОАиП(ЛК) Пашук А. В.\n04-4\n\n09:45 - 11:20(1 3)\nЛогика(ПЗ) Дисько-Шуман М. Р.\n301-4\n\n09:45 - 11:20(2 4)\nИСП(ЛР) Рынкевич С. В.\n402-5\n\n11:40 - 13:15\nМГиА(ПЗ) Стройникова Е. Д.\n321-4\n\n13:25 - 15:00(1 3)\nПрогр-е(ЛР)Удовин И. А.\n111-4')
        if self.day == 5:
            bot.send_message(self.id,
                             '⚰Суббота:\n\n08:00 - 09:35(2 4)\nОАиП(ЛР) Пашук А. В.\n111-4\n\n08:00 - 09:35(2 4)\nИСП(ЛР) Рынкевич С. В.\n112-4\n\n09:45 - 11:20(2 4)\nИСП(ЛР) Рынкевич С. В.\n112-4\n\n09:45 - 11:20(2 4)\nОАиП(ЛР) Пашук А. В.\n111-4')
        if self.day == 6:
            bot.send_message(self.id, '🍻Воскресенье:\nВ этот день никаких пар!')
            sti = open('stiker.jfif', 'rb')
            bot.send_sticker(self.id, sti)
        if self.day == 7:
            bot.send_message(self.id,
                             '11.06.2020\n\n13:00 - 14:00\nПрогр-е(Консультация) Стаховский С. М.\n402-5\n\n12.06.2020\n\n08:00 - 14:00\nПрогр-е(Экзамен) Стаховский С. М.\n402-5\n\n15.06.2020\n\n15:00 - 16:00\nММА(Консультация) Анисимов В. Я.\n308-5\n\n16.06.2020\n\n08:00 - 14:00\nММА(Экзамен) Анисимов В. Я.\n308-5\n\n19.06.2020\n\n16:00 - 17:00\nИнЯз(Консультация) Максимчук Р. Т.\n419-4\n\n16:00 - 17:00\nИнЯз(Консультация) Сидорович Е. И.\n516-4\n\n20.06.2020\n\n08:00 - 12:00\nИнЯз(Экзамен) Максимчук Р. Т.\n402-4\n\n12:00 - 16:00\nИнЯз(Экзамен) Сидорович Е. И.\n400-4\n\n25.06.2020\n\n15:00 - 16:00\nМГиА(Консультация) Стройникова Е. Д.\n311-4\n\n26.06.2020\n\n16:00 - 22:00\nМГиА(Экзамен) Стройникова Е. Д.\n318-4\n\n30.06.2020\n\n15:00 - 16:00\nОАиП(Консультация) Пашук А. В.\n308-5\n\n01.07.2020\n\n16:00 - 22:00\nОАиП(Экзамен) Пашук А. В.\n308-5')


class TimeTableGR2:
    def __init__(self, day, id):
        self.day = day
        self.id = id

    def info(self):
        if self.day == 0:
            bot.send_message(self.id, '📚Понедельник:\n\n08:00 - 09:35\nМЛ(ЛК) Егорова Н. Г.\n108-4\n\n09:45 - '
                                      '11:20\nФизК(ПЗ)\n\n11:40 - 13:15(1 3)\nММА(ПЗ) Теслюк В. Н.\n321-4\n\n13:25 - '
                                      '15:00(1 3)\nБелЯз КР(ПЗ) Дапиро Т. П.\n312-4')
        if self.day == 1:
            bot.send_message(self.id, '📚Вторник:\n\n08:00 - 09:35\nМЛ(ПЗ) Егорова Н. Г.\n322-4\n\n09:45 - '
                                      '11:20\nМГиА(ПЗ) Стройникова Е. Д.\n318-4\n\n11:40 - 13:15\nМГиА(ЛК) '
                                      'Стройникова Е. Д.\n108-4\n\n13:25 - 15:00\nММА(ЛК) Анисимов В. Я.\n108-4')
        if self.day == 2:
            bot.send_message(self.id, '📚Среда:\n\n08:00 - 09:35\nИнЯз(ПЗ) Сидорович Е. И.\n416-4\n\n09:45 - '
                                      '11:20\nФизК(ПЗ)\n\n11:40 - 13:15\nММА(ПЗ) Теслюк В. Н.\n427-4\n\n13:25 - '
                                      '15:00(1 3)\nПрогр-е(ЛР) Удовин И. А.\n402-5')
        if self.day == 3:
            bot.send_message(self.id, '📚Четверг:\n\n08:00 - 09:35\nИнЯз(ПЗ) Коваленко Р. И.\n410-4\n\n09:45 - 11:20('
                                      '1 3)\nЛогика(ПЗ) Лагунова Е. Н.\n301-4\n\n09:45 - 11:20(2 4)\nОАиП(ЛР) Пашук '
                                      'А. В.\n111-4\n\n11:40 - 13:15(1 3)\nЛогика(ЛК) Дисько-Шуман М. '
                                      'Р.\n209-4\n\n11:40 - 13:15(2 4)\nММА(ЛК) Анисимов В. Я.\n209-4\n\n13:25 - '
                                      '15:00\nПрогр-е(ЛК) Стаховский С. М.\n209-4')
        if self.day == 4:
            bot.send_message(self.id, '📚Пятница:\n\n08:00 - 09:35(1 3)\nИСП(ЛК) Бережнов Д. Е.\n04-4\n\n08:00 - '
                                      '09:35(2 4)\nОАиП(ЛК) Пашук А. В.\n04-4\n\n09:45 - 11:20\nИнЯз(ПЗ) Коваленко Р. '
                                      'И.\n409-5\n\n09:45 - 11:20\nИнЯз(ПЗ) Сидорович Е. И.\n319-4\n\n11:40 - '
                                      '13:15\nПрогр-е(ЛР) Удовин И. А.\n111-4\n\n13:25 - 15:00\nКЧ(ПЗ) Рогов М. '
                                      'Г.\n402-5')
        if self.day == 5:
            bot.send_message(self.id, '⚰Суббота:\n\n08:00 - 09:35(1 3)\nОАиП(ЛР) Пашук А. В.\n111-4\n\n08:00 - 09:35('
                                      '1 3)\nИСП(ЛР) Рынкевич С. В.\n112-4\n\n09:45 - 11:20(1 3)\nИСП(ЛР) Рынкевич С. '
                                      'В.\n112-4\n\n09:45 - 11:20(1 3)\nОАиП(ЛР) Пашук А. В.\n111-4\n\n11:40 - 13:15('
                                      '1 3)\nИСП(ЛР) Рынкевич С. В.\n112-4')
        if self.day == 6:
            bot.send_message(self.id, '🍻Воскресенье:\nВ этот день никаких пар!')
            sti = open('stiker.jfif', 'rb')
            bot.send_sticker(self.id, sti)
        if self.day == 7:
            bot.send_message(self.id, '🗿12.06.2020\n\n14:00 - 15:00\nПрогр-е(Консультация) Стаховский С. '
                                      'М.\n402-5\n\n🗿13.06.2020\n\n16:00 - 22:00\nПрогр-е(Экзамен) Стаховский С. '
                                      'М.\n402-5\n\n🗿17.06.2020\n\n16:00 - 17:00\nИнЯз(Консультация) Сидорович Е. '
                                      'И.\n402-4\n16:00 - 17:00\nИнЯз(Консультация) Коваленко Р. '
                                      'И.\n401-4\n\n🗿18.06.2020\n\n08:00 - 12:00\nИнЯз(Экзамен) Сидорович Е. '
                                      'И.\n402-4\n\n08:00 - 12:00\nИнЯз(Экзамен) Коваленко Р. '
                                      'И.\n401-4\n\n🗿20.06.2020\n\n14:00 - 15:00\nОАиП(Консультация) Пашук А. '
                                      'В.\n402-5\n\n🗿22.06.2020\n\n08:00 - 14:00\nОАиП(Экзамен) Пашук А. '
                                      'В.\n402-5\n\n🗿25.06.2020\n\n15:00 - 16:00\nММА(Консультация) Анисимов В. '
                                      'Я.\n409-4\n\n🗿26.06.2020\n\n16:00 - 22:00\nММА(Экзамен) Анисимов В. '
                                      'Я.\n409-4\n\n🗿29.06.2020\n\n15:00 - 16:00\nМГиА(Консультация) Стройникова Е. '
                                      'Д.\n311-4\n\n🗿30.06.2020\n\n09:00 - 14:00\nМГиА(Экзамен) Стройникова Е. '
                                      'Д.\n310-4')


class TimeTableGR3:
    def __init__(self, day, id):
        self.day = day
        self.id = id

    def info(self):
        if self.day == 0:
            bot.send_message(self.id,
                             '📚Понедельник:\n\n08:00 - 09:35\nМЛ(ЛК) Егорова Н. Г.\n108-4\n\n09:45 - 11:20ФизК(ПЗ)\n\n11:40 - 13:15(2 4)\nММА(ПЗ) Теслюк В. Н.\n321-4\n\n13:25 - 15:00(2 4)\nКЧ(ПЗ) Алексеев Ю. И.\n308-5')
        if self.day == 1:
            bot.send_message(self.id,
                             '📚Вторник:\n\n08:00 - 09:35\nИнЯз(ПЗ) Кравченко М. В.\n414-4\n\n09:45 - 11:20\nМЛ(ПЗ) Егорова Н. Г.\n322-4\n\n11:40 - 13:15\nМГиА(ЛК) Стройникова Е. Д.\n108-4\n\n13:25 - 15:00\nММА(ЛК) Анисимов В. Я.\n108-4')
        if self.day == 2:
            bot.send_message(self.id,
                             '📚Среда:\n\n08:00 - 09:35(2 4)\nИСП(ЛР) Рынкевич С. В.\n402-5\n\n09:45 - 11:20\nФизК(ПЗ)\n\n11:40 - 15:00\nПрогр-е(ЛР) Удовин И. А.\n402-5')
        if self.day == 3:
            bot.send_message(self.id,
                             '📚Четверг:\n\n08:00 - 09:35\nИнЯз(ПЗ) Кравченко М. В.\n414-4\n\n09:45 - 11:20\nММА(ПЗ) Теслюк В. Н.\n427-4\n\n11:40 - 13:15(1 3)\nЛогика(ЛК) Дисько-Шуман М. Р.\n209-4\n\n11:40 - 13:15(2 4)\nММА(ЛК) Анисимов В. Я.\n209-4\n\n13:25 - 15:00\nПрогр-е(ЛК) Стаховский С. М.\n209-4')
        if self.day == 4:
            bot.send_message(self.id,
                             '📚Пятница:\n\n08:00 - 09:35(1 3)\nИСП(ЛК) Бережнов Д. Е.\n04-4\n\n08:00 - 09:35(2 4)\nОАиП(ЛК) Пашук А. В.\n04-4\n\n09:45 - 11:20\nМГиА(ПЗ) Стройникова Е. Д.\n427-4\n\n11:40 - 13:15\nИнЯз(ПЗ) Максимчук Р. Т.\n415-4\n\n13:25 - 15:00(1 3)\nКЧ(ПЗ) Алексеев Ю. И.\n308-5')
        if self.day == 5:
            bot.send_message(self.id,
                             '⚰Суббота:\n\n08:00 - 09:35\nИнЯз(ПЗ) Максимчук Р. Т.\n402-4\n\n09:45 - 11:20(1 3)\nОАиП(ЛР) Алексеев Ю. И.\n308-5\n\n09:45 - 11:20(2 4)\nБелЯз КР(ПЗ) Дапиро Т. П.\n320-4\n\n11:40 - 13:15(1 3)\nЛогика(ПЗ) Лагунова Е. Н.\n301-4\n\n11:40 - 13:15(2 4)\nИСП(ЛР) Рынкевич С. В.\n112-4')
        if self.day == 6:
            bot.send_message(self.id, '🍻Воскресенье:\nВ этот день никаких пар!')
            sti = open('stiker.jfif', 'rb')
            bot.send_sticker(self.id, sti)
        if self.day == 7:
            bot.send_message(self.id,
                             '\n\n🗿11.06.2020\n\n14:00 - 15:00\nММА(Консультация) Анисимов В. Я.\n111-4\n\n🗿12.06.2020\n\n08:00 - 14:00\nММА(Экзамен) Анисимов В. Я.\n111-4\n\n🗿15.06.2020\n\n15:00 - 16:00\nМГиА(Консультация) Стройникова Е. Д.\n322-4\n\n🗿16.06.2020\n\n09:00 - 14:00\nМГиА(Экзамен) Стройникова Е. Д.\n322-4\n\n🗿19.06.2020\n\n15:00 - 16:00\nОАиП(Консультация) Пашук А. В.\n402-5\n\n🗿20.06.2020\n\n08:00 - 14:00\nОАиП(Экзамен) Пашук А. В.\n402-5\n\n🗿23.06.2020\n\n15:00 - 16:00\nИнЯз(Консультация)\n\n🗿24.06.2020\n\n08:00 - 12:00\nИнЯз(Экзамен)\n\n🗿29.06.2020\n\n15:00 - 16:00\nПрогр-е(Консультация) Стаховский С. М.\n902-5\n\n🗿30.06.2020\n\n16:00 - 22:00\nПрогр-е(Экзамен) Стаховский С. М.\n112-4')


class TimeTableGR4:
    def __init__(self, day, id):
        self.day = day
        self.id = id

    def info(self):
        if self.day == 0:
            bot.send_message(self.id,
                             '📚Понедельник:\n\n08:00 - 09:35\nМЛ(ЛК) Егорова Н. Г.\n108-4\n\n09:45 - 11:20\nФизК(ПЗ)\n\n11:40 - 13:15\nМЛ(ПЗ) Рябов Д. А.\n322-4')
        if self.day == 1:
            bot.send_message(self.id,
                             '📚Вторник:\n\n08:00 - 09:35\nИнЯз(ПЗ)\n514-4\n\n09:45 - 11:20\nММА(ПЗ) Анисимов В. Я.\n409-4\n\n11:40 - 13:15\nМГиА(ЛК) Стройникова Е. Д.\n108-4\n\n13:25 - 15:00\nММА(ЛК) Анисимов В. Я.\n108-4')
        if self.day == 2:
            bot.send_message(self.id,
                             '📚Среда:\n\n08:00 - 09:35\nКЧ(ПЗ) Анисимов В. Я.\n111-4\n\n09:45 - 11:20\nФизК(ПЗ)\n\n11:40 - 13:15\nМГиА(ПЗ) Стройникова Е. Д.\n409-4\n\n13:25 - 15:00(1 3)\nЛогика(ПЗ) Лагунова Е. Н.\n419-4')
        if self.day == 3:
            bot.send_message(self.id,
                             '📚Четверг:\n\n09:45 - 11:20(2 4)\nММА(ПЗ) Анисимов В. Я.\n420-4\n\n11:40 - 13:15(1 3)\nЛогика(ЛК) Дисько-Шуман М. Р.\n209-4\n\n11:40 - 13:15(2 4)\nММА(ЛК) Анисимов В. Я.\n209-4\n\n13:25 - 15:00\nПрогр-е(ЛК) Стаховский С. М.\n209-4')
        if self.day == 4:
            bot.send_message(self.id,
                             '📚Пятница:\n\n08:00 - 09:35(1 3)\nИСП(ЛК) Бережнов Д. Е.\n04-4\n\n08:00 - 09:35(2 4)\nОАиП(ЛК) Пашук А. В.\n04-4\n\n09:45 - 11:20(1 3)\nПрогр-е(ЛР) Клыбик П. М.\n112-4\n\n09:45 - 11:20(2 4)\nБелЯз КР(ПЗ) Дапиро Т. П.\n901-5\n\n11:40 - 13:15\nПрогр-е(ЛР) Клыбик П. М.\n112-4')
        if self.day == 5:
            bot.send_message(self.id,
                             '⚰Суббота:\n\n08:00 - 09:35\nИнЯз(ПЗ) Коваленко Р. И.\n400-4\n\n08:00 - 09:35\nИнЯз(ПЗ) Карпик Л. С.\n516-4\n\n09:45 - 11:20(1 3)\nИСП(ЛР) Фарафонов М. П.\n402-5\n\n09:45 - 11:20(2 4)\nОАиП(ЛР) Алексеев Ю. И.\n308-5\n\n11:40 - 13:15(1 3)\nОАиП(ЛР) Алексеев Ю. И.\n308-5\n\n13:25 - 15:00\nИСП(ЛР) Фарафонов М. П.\n318-5')
        if self.day == 6:
            bot.send_message(self.id, '🍻Воскресенье:\nВ этот день никаких пар!')
            sti = open('stiker.jfif', 'rb')
            bot.send_sticker(self.id, sti)
        if self.day == 7:
            bot.send_message(self.id,
                             '🗿12.06.2020\n\n16:00 - 17:00\nИнЯз(Консультация) Коваленко Р. И.\n414-4\n\n17:00 - 18:00\nИнЯз(Консультация) Карпик Л. С.\n400-4\n\n🗿13.06.2020\n\n08:00 - 12:00\nИнЯз(Экзамен) Карпик Л. С.\n433-1\n\n16:00 - 20:00\nИнЯз(Экзамен) Коваленко Р. И.\n414-4\n\n🗿16.06.2020\n\n14:00 - 15:00\nПрогр-е(Консультация) Стаховский С. М.\n112-4\n\n🗿17.06.2020\n\n08:00 - 14:00\nПрогр-е(Экзамен) Стаховский С. М.\n112-4\n\n🗿20.06.2020\n\n14:00 - 15:00\nМГиА(Консультация) Стройникова Е. Д.\n321-4\n\n🗿22.06.2020\n\n09:00 - 14:00\nМГиА(Экзамен) Стройникова Е. Д.\n320-4\n\n🗿25.06.2020\n\n15:00 - 16:00\nОАиП(Консультация) Пашук А. В.\n111-4\n\n🗿26.06.2020\n\n16:00 - 22:00\nОАиП(Экзамен) Пашук А. В.\n111-4\n\n🗿29.06.2020\n\n15:00 - 16:00\nММА(Консультация) Анисимов В. Я.\n111-4\n\n🗿30.06.2020\n\n08:00 - 14:00\nММА(Экзамен) Анисимов В. Я.\n111-4')


class TimeTableGR5:
    def __init__(self, day, id):
        self.day = day
        self.id = id

    def info(self):
        if self.day == 0:
            bot.send_message(self.id,
                             '📚Понедельник:\n\n08:00 - 09:35\nМЛ(ЛК) Егорова Н. Г.\n108-4\n\n09:45 - 11:20\nФизК(ПЗ)\n\n11:40 - 13:15(1 3)\nКЧ(ПЗ) Протько М. И.\n112-4\n\n11:40 - 13:15(2 4)\nММА(ПЗ) Анисимов В. Я.\n311-4\n\n13:25 - 15:00(2 4)\nКЧ(ПЗ) Протько М. И.\n402-5')
        if self.day == 1:
            bot.send_message(self.id,
                             '📚Вторник:\n\n11:40 - 13:15\nМГиА(ЛК) Стройникова Е. Д.\n108-4\n\n13:25 - 15:00\nММА(ЛК) Анисимов В. Я.\n108-4')
        if self.day == 2:
            bot.send_message(self.id,
                             '📚Среда:\n\n09:45 - 11:20\nФизК(ПЗ)\n\n11:40 - 13:15(1 3)\nОАиП(ЛР) Алексеев Ю. И.\n112-4\n\n11:40 - 13:15(2 4)\nПрогр-е(ЛР) Клыбик П. М.\n111-4\n\n13:25 - 15:00\nМГиА(ПЗ) Стройникова Е. Д.\n312-4\n\n15:20 - 16:55\nИнЯз(ПЗ) Сидорович Е. И.\n402-4\n\n15:20 - 16:55\nИнЯз(ПЗ) Максимчук Р. Т.\n414-4')
        if self.day == 3:
            bot.send_message(self.id,
                             '📚Четверг:\n\n09:45 - 11:20(2 4)\nЛогика(ПЗ) Лагунова Е. Н.\n301-4\n\n11:40 - 13:15(1 3)\nЛогика(ЛК) Дисько-Шуман М. Р.\n209-4\n\n11:40 - 13:15(2 4)\nММА(ЛК) Анисимов В. Я.\n209-4\n\n13:25 - 15:00\nПрогр-е(ЛК) Стаховский С. М.\n209-4\n\n15:20 - 16:55\nИнЯз(ПЗ) Максимчук Р. Т.\n414-4\n\n15:20 - 16:55\nИнЯз(ПЗ) Сидорович Е. И.\n413-4')
        if self.day == 4:
            bot.send_message(self.id,
                             '📚Пятница:\n\n08:00 - 09:35(1 3)\nИСП(ЛК) Бережнов Д. Е.\n04-4\n\n08:00 - 09:35(2 4)\nОАиП(ЛК) Пашук А. В.\n04-4\n\n09:45 - 11:20\nМЛ(ПЗ) Рябов Д. А. \n409-4\n\n11:40 - 13:15\nММА(ПЗ) Анисимов В. Я.\n322-4\n\n13:25 - 15:00(1 3)\nПрогр-е(ЛР) Клыбик П. М.\n112-4')
        if self.day == 5:
            bot.send_message(self.id,
                             '⚰Суббота:\n\n08:00 - 09:35(2 4)\nБелЯз КР(ПЗ)Дапиро Т. П.\n320-4\n\n09:45 - 11:20(2 4)\nИСП(ЛР) Фарафонов М. П.\n221-5\n\n11:40 - 13:15\nИСП(ЛР) Фарафонов М. П.\n221-5\n\n13:25 - 15:00(1 3)\nОАиП(ЛР) Алексеев Ю. И.\n308-5\n\n13:25 - 15:00(2 4)\nИСП(ЛР) Фарафонов М. П.\n221-5')
        if self.day == 6:
            bot.send_message(self.id, '🍻Воскресенье:\nВ этот день никаких пар!')
            sti = open('stiker.jfif', 'rb')
            bot.send_sticker(self.id, sti)
        if self.day == 7:
            bot.send_message(self.id,
                             '🗿11.06.2020\n\n13:00 - 14:00\nПрогр-е(Консультация) Стаховский С. М.\n402-5\n\n🗿12.06.2020\n\n08:00 - 14:00\nПрогр-е(Экзамен) Стаховский С. М.\n402-5\n\n🗿15.06.2020\n\n15:00 - 16:00\nММА(Консультация) Анисимов В. Я.\n308-5\n\n🗿16.06.2020\n\n08:00 - 14:00\nММА(Экзамен) Анисимов В. Я.\n308-5\n\n🗿19.06.2020\n\n16:00 - 17:00\nИнЯз(Консультация) Максимчук Р. Т.\n419-4\n\n16:00 - 17:00\nИнЯз(Консультация) Сидорович Е. И.\n516-4\n\n🗿20.06.2020\n\n08:00 - 12:00\nИнЯз(Экзамен) Максимчук Р. Т.\n402-4\n\n12:00 - 16:00\nИнЯз(Экзамен) Сидорович Е. И.\n400-4\n\n🗿25.06.2020\n\n15:00 - 16:00\nМГиА(Консультация) Стройникова Е. Д.\n311-4\n\n🗿26.06.2020\n\n16:00 - 22:00\nМГиА(Экзамен) Стройникова Е. Д.\n318-4\n\n🗿30.06.2020\n\n15:00 - 16:00\nОАиП(Консультация) Пашук А. В.\n308-5\n\n🗿01.07.2020\n\n16:00 - 22:00\nОАиП(Экзамен) Пашук А. В.\n308-5')


class TimeTableGR6:
    def __init__(self, day, id):
        self.day = day
        self.id = id

    def info(self):
        if self.day == 0:
            bot.send_message(self.id,
                             '📚Понедельник:\n\n08:00 - 09:35\nМЛ(ЛК) Егорова Н. Г. \n108-4\n\n09:45 - 11:20\nФизК(ПЗ)\n\n11:40 - 13:15\nБелЯз КР(ПЗ) Дапиро Т. П.\n316-4\n\n13:25 - 15:00\nММА(ПЗ) Анисимов В. Я. \n321-4\n\n15:20 - 16:55\nКЧ(ПЗ)Шиманский В. В.\n112-4')
        if self.day == 1:
            bot.send_message(self.id,
                             '📚Вторник:\n\n09:45 - 11:20\nИнЯз(ПЗ)\n\n11:40 - 13:15\nМГиА(ЛК) Стройникова Е. Д.\n108-4\n\n13:25 15:00\nММА(ЛК) Анисимов В. Я.\n108-4')
        if self.day == 2:
            bot.send_message(self.id,
                             '📚Среда:\n\n09:45 - 11:20\nФизК(ПЗ)\n\n11:40 - 13:15\nПрогр-е(ЛР) Клыбик П. М.\n111-4\n\n11:40 - 13:15\nОАиП(ЛР) Алексеев Ю. И.\n112-4\n\n13:25 - 15:00\nОАиП(ЛР) Алексеев Ю. И.\n112-4')
        if self.day == 3:
            bot.send_message(self.id,
                             '📚Четверг: \n\n08:00 - 09:35\nЛогика(ПЗ) Лагунова Е. Н. \n427-4\n\n09:45 - 11:20\nИнЯз(ПЗ)\n\n11:40 - 13:15\nММА(ЛК)Анисимов В. Я.\n209-4\n\n13:25 - 15:00\nПрогр-е(ЛК) Стаховский С. М.\n209-4')
        if self.day == 4:
            bot.send_message(self.id,
                             '📚Пятница:\n\n08:00 - 09:35\nИСП(ЛК)Бережнов Д. Е. \n04-4\n\n09:45 - 11:20\nММА(ПЗ)Анисимов В. Я.\n322-4\n\n11:40 - 13:15\nМЛ(ПЗ) Рябов Д. А.\n409-4\n\n13:25 - 15:00\nМГиА(ПЗ) Стройникова Е. Д.\n321-4')
        if self.day == 5:
            bot.send_message(self.id,
                             '⚰Суббота:\n\n08:00 - 09:35\nИСП(ЛР)Чмуров М. В.\n402-5\n\n09:45 - 11:20\nИСП(ЛР)Чмуров М. В. \n402-5\n\n11:40 - 13:15\nИСП(ЛР)Чмуров М. В.\n402-5')
        if self.day == 6:
            bot.send_message(self.id, '🍻Воскресенье:\nВ этот день никаких пар!')
            sti = open('stik.jfif', 'rb')
            bot.send_sticker(self.id, sti)
        if self.day == 7:
            bot.send_message(self.id,
                             '🗿11.06.2020\n\n14:00 - 15:00\nПрогр-е(Консультация) Стаховский С. М.\n402-5\n\n🗿12.06.2020\n\n16:00 - 22:00\nПрогр-е(Экзамен) Стаховский С. М.\n402-5\n\n🗿15.06.2020\n\n15:00 - 16:00\nИнЯз(Консультация)\n\n🗿16.06.2020\n\n12:00 - 16:00\nИнЯз(Экзамен)\n\n🗿19.06.2020\n\n15:00 - 16:00\nММА(Консультация)Анисимов В. Я.\n112-4\n\n🗿20.06.2020\n\n08:00 - 14:00\nММА(Экзамен) Анисимов В. Я.\n112-4\n\n🗿23.06.2020\n\n15:00 - 16:00\nМГиА(Консультация)\n322-4\n\n🗿24.06.2020\n\n09:00 - 14:00\nМГиА(Экзамен) Стройникова Е. Д.\n322-4\n\n🗿29.06.2020\n\n15:00 - 16:00\nОАиП(Консультация) Пашук А. В.\n308-5\n\n🗿30.06.2020\n\n16:00 - 22:00\nОАиП(Экзамен) Пашук А. В.\n308-5')


class TimeTablePK:
    def __init__(self, day, id):
        self.day = day
        self.id = id

    def info(self):
        if self.day == 0:
            bot.send_message(self.id, '📚Понедельник\nСегодня у Вас нет занятий. ')
        if self.day == 1:
            bot.send_message(self.id, '📚Вторник: \n09:45 - 11:20\nКЧ(ПЗ) 953501\n111-4')
        if self.day == 2:
            bot.send_message(self.id,
                             '📚Среда:\n11:40 - 13:15\nПрогр-е(ЛР) 953505\n111-4\n\n13:25 - 15:00\nПрогр-е(ЛР) 953506\n111-4')
        if self.day == 3:
            bot.send_message(self.id, '📚Четверг: \nСегодня у Вас нет занятий.')
        if self.day == 4:
            bot.send_message(self.id,
                             '📚Пятница: \n09:45 - 11:20\nПрогр-е(ЛР) 953504\n112-4\n\n11:40 - 13:15\nПрогр-е(ЛР)953504\n112-4\n\n13:25 - 15:00\nПрогр-е(ЛР) 953505\n112-4')
        if self.day == 5:
            bot.send_message(self.id, '⚰Суббота: \nСегодня у Вас нет занятий.')
        if self.day == 6:
            bot.send_message(self.id, '🍻Воскресенье:\nВ этот день никаких пар!')
            sti = open('stiker.jfif', 'rb')
            bot.send_sticker(self.id, sti)
        if self.day == 7:
            bot.send_message(self.id, 'А нет у Вас больше сессии, сдали уже все давно')


TOKEN = '1184188087:AAFKedtw2Jibjuv2A-axphY7cOT8qWakQaU'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    global chat_id
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Я Максим Генадьевич")
    item2 = types.KeyboardButton("Я студент группы 953506")
    item3 = types.KeyboardButton("Я студент группы 953505")
    item4 = types.KeyboardButton("Я студент группы 953504")
    item5 = types.KeyboardButton("Я студент группы 953503")
    item6 = types.KeyboardButton("Я студент группы 953502")
    item7 = types.KeyboardButton("Я студент группы 953501")

    markup.add(item7, item6, item5, item4, item3, item2, item1)
    bot.send_message(message.chat.id,
                     "Здравствуйте, {0.first_name}!\n\nВыберите интересующую Вас группу потока первого курса "
                     "«Информатики и Технологии Программирования», чтобы узнать расписание на "
                     "сегодня/завтра/неделю/ближайшую сессию.\n\nЕсли Вы Павел Клыбик, подтвердите это, нажав на Ваше "
                     "имя, чтобы узнать Ваше расписание на сегодня/завтра/неделю/ближайшую сессию.\n\nЕсли Вы хотите "
                     "узнать расписание другой группы, просто введите её номер в строку ввода сообщений. ".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def who(message):
    global choice
    if message.chat.type == 'private':
        if message.text == 'Я Максим Генадьевич':
            choice = 1
        elif message.text == 'Я студент группы 953506':
            choice = 2
        elif message.text == 'Я студент группы 953505':
            choice = 3
        elif message.text == 'Я студент группы 953504':
            choice = 4
        elif message.text == 'Я студент группы 953503':
            choice = 5
        elif message.text == 'Я студент группы 953502':
            choice = 6
        elif message.text == 'Я студент группы 953501':
            choice = 7
        elif message.text == '6':
            URL = baseUrl + message.text
            lessons = schedule_dao.get_todays_schedule(URL)
            msg = message_schedule1('Сегодня', lessons)
            bot.send_message(message.chat.id, msg)
        elif choice != 0:
            date = datetime.datetime.today()
            if message.text == 'на сегодня':
                if choice == 1:
                    TimeTablePK.info(TimeTablePK(date.weekday(), message.chat.id))
                elif choice == 2:
                    TimeTableGR6.info(TimeTableGR6(date.weekday(), message.chat.id))
                elif choice == 3:
                    TimeTableGR5.info(TimeTableGR5(date.weekday(), message.chat.id))
                elif choice == 4:
                    TimeTableGR4.info(TimeTableGR4(date.weekday(), message.chat.id))
                elif choice == 5:
                    TimeTableGR3.info(TimeTableGR3(date.weekday(), message.chat.id))
                elif choice == 6:
                    TimeTableGR2.info(TimeTableGR2(date.weekday(), message.chat.id))
                elif choice == 7:
                    TimeTableGR1.info(TimeTableGR1(date.weekday(), message.chat.id))
            elif message.text == 'на завтра':
                if choice == 1:
                    TimeTablePK.info(TimeTablePK(date.weekday() + 1, message.chat.id))
                elif choice == 2:
                    TimeTableGR6.info(TimeTableGR6(date.weekday() + 1, message.chat.id))
                elif choice == 3:
                    TimeTableGR5.info(TimeTableGR5(date.weekday() + 1, message.chat.id))
                elif choice == 4:
                    TimeTableGR4.info(TimeTableGR4(date.weekday() + 1, message.chat.id))
                elif choice == 5:
                    TimeTableGR3.info(TimeTableGR3(date.weekday() + 1, message.chat.id))
                elif choice == 6:
                    TimeTableGR2.info(TimeTableGR2(date.weekday() + 1, message.chat.id))
                elif choice == 7:
                    TimeTableGR1.info(TimeTableGR1(date.weekday() + 1, message.chat.id))
            elif message.text == 'на сессию':
                if choice == 1:
                    TimeTablePK.info(TimeTablePK(7, message.chat.id))
                elif choice == 2:
                    TimeTableGR6.info(TimeTableGR6(7, message.chat.id))
                elif choice == 3:
                    TimeTableGR5.info(TimeTableGR5(7, message.chat.id))
                elif choice == 4:
                    TimeTableGR4.info(TimeTableGR4(7, message.chat.id))
                elif choice == 5:
                    TimeTableGR3.info(TimeTableGR3(7, message.chat.id))
                elif choice == 6:
                    TimeTableGR2.info(TimeTableGR2(7, message.chat.id))
                elif choice == 7:
                    TimeTableGR1.info(TimeTableGR1(7, message.chat.id))
            elif message.text == 'на неделю':
                if choice == 1:
                    weekday = [0, 1, 2, 3, 4, 5, 6]
                    for number in weekday:
                        TimeTablePK.info(TimeTablePK(number, message.chat.id))
                elif choice == 2:
                    weekday = [0, 1, 2, 3, 4, 5, 6]
                    for number in weekday:
                        TimeTableGR6.info(TimeTableGR6(number, message.chat.id))
                elif choice == 3:
                    weekday = [0, 1, 2, 3, 4, 5, 6]
                    for number in weekday:
                        TimeTableGR5.info(TimeTableGR5(number, message.chat.id))
                elif choice == 4:
                    weekday = [0, 1, 2, 3, 4, 5, 6]
                    for number in weekday:
                        TimeTableGR4.info(TimeTableGR4(number, message.chat.id))
                elif choice == 5:
                    weekday = [0, 1, 2, 3, 4, 5, 6]
                    for number in weekday:
                        TimeTableGR3.info(TimeTableGR3(number, message.chat.id))
                elif choice == 6:
                    weekday = [0, 1, 2, 3, 4, 5, 6]
                    for number in weekday:
                        TimeTableGR2.info(TimeTableGR2(number, message.chat.id))
                elif choice == 7:
                    weekday = [0, 1, 2, 3, 4, 5, 6]
                    for number in weekday:
                        TimeTableGR1.info(TimeTableGR1(number, message.chat.id))
            elif message.text == 'на какой-либо день':
                markup = types.InlineKeyboardMarkup(row_width=7)
                item1 = types.InlineKeyboardButton("Пн", callback_data='Mon')
                item2 = types.InlineKeyboardButton("Вт", callback_data='Tue')
                item3 = types.InlineKeyboardButton("Ср", callback_data='Wed')
                item4 = types.InlineKeyboardButton("Чт", callback_data='Thu')
                item5 = types.InlineKeyboardButton("Пт", callback_data='Fri')
                item6 = types.InlineKeyboardButton("Сб", callback_data='Sat')
                item7 = types.InlineKeyboardButton("Вс", callback_data='Sun')

                markup.add(item1, item2, item3, item4, item5, item6, item7)

                bot.send_message(message.chat.id, 'Выбери день недели', reply_markup=markup)

                @bot.callback_query_handler(func=lambda call: True)
                def callback_inline(call):
                    try:
                        if call.message:
                            if call.data == 'Mon':
                                if choice == 1:
                                    TimeTablePK.info(TimeTablePK(0, message.chat.id))
                                elif choice == 2:
                                    TimeTableGR6.info(TimeTableGR6(0, message.chat.id))
                                elif choice == 3:
                                    TimeTableGR5.info(TimeTableGR5(0, message.chat.id))
                                elif choice == 4:
                                    TimeTableGR4.info(TimeTableGR4(0, message.chat.id))
                                elif choice == 5:
                                    TimeTableGR3.info(TimeTableGR3(0, message.chat.id))
                                elif choice == 6:
                                    TimeTableGR2.info(TimeTableGR2(0, message.chat.id))
                                elif choice == 7:
                                    TimeTableGR1.info(TimeTableGR1(0, message.chat.id))
                            elif call.data == 'Tue':
                                if choice == 1:
                                    TimeTablePK.info(TimeTablePK(1, message.chat.id))
                                elif choice == 2:
                                    TimeTableGR6.info(TimeTableGR6(1, message.chat.id))
                                elif choice == 3:
                                    TimeTableGR5.info(TimeTableGR5(1, message.chat.id))
                                elif choice == 4:
                                    TimeTableGR4.info(TimeTableGR4(1, message.chat.id))
                                elif choice == 5:
                                    TimeTableGR3.info(TimeTableGR3(1, message.chat.id))
                                elif choice == 6:
                                    TimeTableGR2.info(TimeTableGR2(1, message.chat.id))
                                elif choice == 7:
                                    TimeTableGR1.info(TimeTableGR1(1, message.chat.id))
                            elif call.data == 'Wed':
                                if choice == 1:
                                    TimeTablePK.info(TimeTablePK(2, message.chat.id))
                                elif choice == 2:
                                    TimeTableGR6.info(TimeTableGR6(2, message.chat.id))
                                elif choice == 3:
                                    TimeTableGR5.info(TimeTableGR5(2, message.chat.id))
                                elif choice == 4:
                                    TimeTableGR4.info(TimeTableGR4(2, message.chat.id))
                                elif choice == 5:
                                    TimeTableGR3.info(TimeTableGR3(2, message.chat.id))
                                elif choice == 6:
                                    TimeTableGR2.info(TimeTableGR2(2, message.chat.id))
                                elif choice == 7:
                                    TimeTableGR1.info(TimeTableGR1(2, message.chat.id))
                            elif call.data == 'Thu':
                                if choice == 1:
                                    TimeTablePK.info(TimeTablePK(3, message.chat.id))
                                elif choice == 2:
                                    TimeTableGR6.info(TimeTableGR6(3, message.chat.id))
                                elif choice == 3:
                                    TimeTableGR5.info(TimeTableGR5(3, message.chat.id))
                                elif choice == 4:
                                    TimeTableGR4.info(TimeTableGR4(3, message.chat.id))
                                elif choice == 5:
                                    TimeTableGR3.info(TimeTableGR3(3, message.chat.id))
                                elif choice == 6:
                                    TimeTableGR2.info(TimeTableGR2(3, message.chat.id))
                                elif choice == 7:
                                    TimeTableGR1.info(TimeTableGR1(3, message.chat.id))
                            elif call.data == 'Fri':
                                if choice == 1:
                                    TimeTablePK.info(TimeTablePK(4, message.chat.id))
                                elif choice == 2:
                                    TimeTableGR6.info(TimeTableGR6(4, message.chat.id))
                                elif choice == 3:
                                    TimeTableGR5.info(TimeTableGR5(4, message.chat.id))
                                elif choice == 4:
                                    TimeTableGR4.info(TimeTableGR4(4, message.chat.id))
                                elif choice == 5:
                                    TimeTableGR3.info(TimeTableGR3(4, message.chat.id))
                                elif choice == 6:
                                    TimeTableGR2.info(TimeTableGR2(4, message.chat.id))
                                elif choice == 7:
                                    TimeTableGR1.info(TimeTableGR1(4, message.chat.id))
                            elif call.data == 'Sat':
                                if choice == 1:
                                    TimeTablePK.info(TimeTablePK(5, message.chat.id))
                                elif choice == 2:
                                    TimeTableGR6.info(TimeTableGR6(5, message.chat.id))
                                elif choice == 3:
                                    TimeTableGR5.info(TimeTableGR5(5, message.chat.id))
                                elif choice == 4:
                                    TimeTableGR4.info(TimeTableGR4(5, message.chat.id))
                                elif choice == 5:
                                    TimeTableGR3.info(TimeTableGR3(5, message.chat.id))
                                elif choice == 6:
                                    TimeTableGR2.info(TimeTableGR2(5, message.chat.id))
                                elif choice == 7:
                                    TimeTableGR1.info(TimeTableGR1(5, message.chat.id))
                            elif call.data == 'Sun':
                                if choice == 1:
                                    TimeTablePK.info(TimeTablePK(6, message.chat.id))
                                elif choice == 2:
                                    TimeTableGR6.info(TimeTableGR6(6, message.chat.id))
                                elif choice == 3:
                                    TimeTableGR5.info(TimeTableGR5(6, message.chat.id))
                                elif choice == 4:
                                    TimeTableGR4.info(TimeTableGR4(6, message.chat.id))
                                elif choice == 5:
                                    TimeTableGR3.info(TimeTableGR3(6, message.chat.id))
                                elif choice == 6:
                                    TimeTableGR2.info(TimeTableGR2(6, message.chat.id))
                                elif choice == 7:
                                    TimeTableGR1.info(TimeTableGR1(6, message.chat.id))

                            # remove inline buttons
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text="После выбранного дня",
                                                  reply_markup=None)

                            # show alert
                            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                                      text="Загружается...")

                    except Exception as e:
                        print(repr(e))
            else:
                URL = baseUrl + message.text
                lessons = schedule_dao.get_todays_schedule(URL)
                msg = message_schedule1(message.text, lessons)
                bot.send_message(message.chat.id, msg)
        else:
            URL = baseUrl + message.text
            lessons = schedule_dao.get_todays_schedule(URL)
            msg = message_schedule1(message.text, lessons)
            bot.send_message(message.chat.id, msg)

    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("на сегодня")
    item2 = types.KeyboardButton("на завтра")
    item3 = types.KeyboardButton("на сессию")
    item4 = types.KeyboardButton("на неделю")
    item5 = types.KeyboardButton("на какой-либо день")
    markup1.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, "Хотите посмотреть расписание на...", reply_markup=markup1)


def message_schedule1(title: str, lessons: list) -> str:
    msg = f'Расписание группы {title} на сегодня: \n\n'

    for lesson in lessons:
        msg += f"📚 {lesson['lessonTime']} \n {lesson['subject']}({lesson['lessonType']}) \nАудитория: {lesson['auditory']}\n\n "

    return msg


# RUN
bot.polling(none_stop=True)
