from abc import ABC, abstractmethod

from excepts import NotEnoughSpaceStore, NotEnoughProductStore, NoProductInStore, TooManyDifferentProduct, \
    InvalidRequest


class AbstractStorage(ABC):
    @abstractmethod
    def add(self, name, amount):
        pass

    def remove(self, name, amount):
        pass

    def get_free_space(self):
        pass

    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass


class Store(AbstractStorage):
    def __init__(self, items: dict[str, int], capacity: int = 100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, amount):
        if self.get_free_space() < amount:
            raise NotEnoughSpaceStore

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name, amount):
        if self.__items[name] < amount:
            raise NotEnoughProductStore

        if name not in self.__items:
            raise NoProductInStore
        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value

        return self.__capacity - current_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)


class Shop(Store):
    def __init__(self, items: dict[str, int], capacity: int = 20):
        super().__init__(items=items, capacity=capacity)

    def add(self, name, amount):
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProduct

        super().add(name=name, amount=amount)


class Request:
    def __init__(self, request):
        splitted_request = request.lower().split(' ')
        if len(splitted_request) != 7:
            raise InvalidRequest

        self.amount = int(splitted_request[1])
        self.product = splitted_request[2]
        self.departure = splitted_request[4]
        self.destination = splitted_request[6]


class Courier:
    def __init__(self, request, store, shop):
        self.__request = request

        if self.__request.departure == 'склад':
            self.__from = store
        elif self.__request.departure == 'магазин':
            self.__from = shop

        if self.__request.destination == 'склад':
            self.__to = store
        elif self.__request.destination == 'магазин':
            self.__to = shop

    def move(self):
        self.__from.remove(name=self.__request.product, amount=self.__request.amount)
        print(f"Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.departure}")

        self.__to.add(name=self.__request.product, amount=self.__request.amount)
        print(f"Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}")
