# 6. Создать класс Отель. Класс хранит цены на разные комнаты.
#    Класс хранит количество забронированных комнат разного типа.
#    Выдавать количество свободных комнат. Создать метод "забронировать"

class Hotel:
    def __init__(self, tariff: int, quantity_room: int):

        self.tariff = tariff
        self.quatity = quantity_room

class TypeRoom(Hotel):
    def __init__(self, tarrif, quantity_room, class_badroom: str, how_places_do_you_want: int):
        Hotel.__init__(self, tarrif, quantity_room)
        self.class_badroom = class_badroom
        self.how_places = how_places_do_you_want

    def to_order(self):
        while self.quatity > self.how_places:
            self.quatity -= self.how_places
            room_tarrif_all_place = {self.class_badroom: {self.tariff: self.quatity}}
            for classe, quatity in room_tarrif_all_place.items():
                result = f'{self.class_badroom}: цена = {self.tariff} руб, количество свободных мест = {self.quatity}'
                return result

hotel1 = TypeRoom(200, 20, "Classe A", 1)
hotel2 = TypeRoom(120, 15, "Classe B", 4)
hotel3 = TypeRoom(300, 17, "Classe C", 5)
hotel4 = TypeRoom(600, 25, "Classe D", 23)
hotel5 = TypeRoom(1000, 33, "Classe E", 14)
hotel6 = TypeRoom(1200, 55, "Classe F", 8)
print(hotel1.to_order())
print(hotel2.to_order())
print(hotel3.to_order())
print(hotel4.to_order())
print(hotel5.to_order())
print(hotel6.to_order())

