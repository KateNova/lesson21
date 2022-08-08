from abc import ABC, abstractmethod


class Storage(ABC):

    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def capacity(self):
        pass

    @abstractmethod
    def add(self, item_name, item_number):
        pass

    @abstractmethod
    def remove(self, item_name, item_number):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):

    def __init__(self, items, capacity=100):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        self._capacity = new_capacity

    def add(self, item_name, item_number):
        if self.get_free_space() > item_number:
            if item_name in self.items:
                self._items[item_name] += item_number
            else:
                self._items[item_name] = item_number
            return True
        else:
            print('Количества места на складе не хватает чтобы хранить столько товара')
        return False

    def remove(self, item_name, item_number):
        if item_name in self.items:
            if item_number > self._items[item_name]:
                print('Не хватает на складе, попробуйте заказать меньше')
            elif item_number == self._items[item_name]:
                del self._items[item_name]
                return True
            else:
                self._items[item_name] -= item_number
                return True
        else:
            print('Нет такого товара на складе')
        return False

    def get_free_space(self):
        return self.capacity - sum([v for k, v in self.items.items()])

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())

    def __str__(self):
        res = ''
        for k, v in self.items.items():
            res += f'{k}: {v}\n'
        return res


class Shop(Store):

    MAX_ITEMS_TYPES = 5

    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, item_name, item_number):
        if self.get_free_space() > item_number:
            if item_name in self.items:
                self._items[item_name] += item_number
                return True
            else:
                if self.get_unique_items_count() < self.MAX_ITEMS_TYPES:
                    self._items[item_name] = item_number
                    return True
                else:
                    print('В магазине может храниться только 5 видов товаров, это 6')
        else:
            print('Количества места в магазине не хватает чтобы хранить столько товара')
        return False


class Request:

    def __init__(self, storage_list, user_string):
        self._storage_list = storage_list

        splited_string = user_string.split()

        self._xfrom = splited_string[4]
        self._to = splited_string[6]
        self._amount = int(splited_string[1])
        self._product = splited_string[2]

    @property
    def xfrom(self):
        return self._xfrom

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product
