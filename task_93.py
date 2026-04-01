from datetime import datetime
from typing import List, Optional, Union


class Room:
    def __init__(self, number: int, price: int) -> None:
        self.number: int = number
        self.price: int = price

    def get_price(self) -> int:
        return self.price

    def __repr__(self) -> str:
        return f'Номер {self.number} $ {self.get_price()}'


class LuxuryRoom(Room):
    def __init__(self, number: int, price: int, multiplayer: float = 1.5) -> None:
        super().__init__(number, price)
        self.multiplayer: float = multiplayer

    def get_price(self) -> int:
        return int(self.price * self.multiplayer)

    def __repr__(self) -> str:
        return f'Номер {self.number} $ {self.get_price()}'


class Booking:
    def __init__(self, room: Room, start_date: str, end_date: str) -> None:
        self.room: Room = room
        self.start_date: datetime = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date: datetime = datetime.strptime(end_date, "%Y-%m-%d")

    def overlaps(self, start: str, end: str) -> bool:
        req_start: datetime = datetime.strptime(start, "%Y-%m-%d")
        req_end: datetime = datetime.strptime(end, "%Y-%m-%d")
        return req_start < self.end_date and req_end > self.start_date


class Hotel:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rooms: List[Room] = []
        self.bookings: List[Booking] = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def get_available_rooms(self, start: str, end: str) -> List[Room]:
        booked_rooms: List[Room] = [b.room for b in self.bookings if b.overlaps(start, end)]
        return [r for r in self.rooms if r not in booked_rooms]

    def book_room(self, numbers: int, start: str, end: str) -> str:
        available: List[Room] = self.get_available_rooms(start, end)
        for room in available:
            if room.number == numbers:
                new_booking: Booking = Booking(room, start, end)
                self.bookings.append(new_booking)
                return f'Успешно {room} забронирован с {start} по {end}'
        return 'Ошибка: номер занят или не существует'

    def cancel_booking(self, number: int) -> str:
        self.bookings = [b for b in self.bookings if b.room.number != number]
        return f'Бронирование номера {number} отменено'


my_hotel = Hotel("Grand Hotel")
my_hotel.add_room(Room(101, 100))
my_hotel.add_room(LuxuryRoom(201, 200))

print("Доступно на завтра:", my_hotel.get_available_rooms("2024-05-01", "2024-05-05"))
print(my_hotel.book_room(201, "2024-05-01", "2024-05-05"))
print("Забронировано:", [b.room for b in my_hotel.bookings])
print("Доступно (пересечение дат):", my_hotel.get_available_rooms("2024-05-03", "2024-05-07"))






