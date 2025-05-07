
class Room:
    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price

    def __str__(self):
        return f'Room {self.number} ({self.room_type}) - ${self.price}/night'


class Hotel:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.rooms = []

    def add_room(self, number, room_type, price):
        self.rooms.append(Room(number, room_type, price))

    def list_rooms(self):
        return self.rooms

    def __str__(self):
        return f'{self.name} in {self.city} - {len(self.rooms)} rooms'


class HotelNetwork:
    def __init__(self):
        self.hotels = []

    def add_hotel(self, name, city):
        hotel = Hotel(name, city)
        self.hotels.append(hotel)
        return hotel

    def list_hotels(self):
        return self.hotels


def main():
    network = HotelNetwork()

    # Додавання готелів
    h1 = network.add_hotel("Grand Hotel", "Kyiv")
    h2 = network.add_hotel("Sea Breeze", "Odesa")

    # Додавання номерів
    h1.add_room(101, "Single", 100)
    h1.add_room(102, "Double", 150)

    h2.add_room(201, "Suite", 300)

    # Перегляд усіх готелів
    print("Hotels in network:")
    for hotel in network.list_hotels():
        print(hotel)
        for room in hotel.list_rooms():
            print("   ", room)


if __name__ == "__main__":
    main()
