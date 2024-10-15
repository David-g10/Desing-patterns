from abc import ABC, abstractmethod

class Observable(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def deattach(self, observer):
        pass

    @abstractmethod
    def notify(self, observer):
        pass

class Observer(ABC):
    _id = None

    @abstractmethod
    def update(self, data):
        pass

# Example: --------------------------------------------------------------------

class User(Observable):
    _array_observer = []
    _name = ""
    _addres = ""

    def attach(self, observer):
        self._array_observer.append(observer)

    def deattach(self, observer):
        self._array_observer.remove(observer)

    def notify(self):
        for elem in self._array_observer:
            elem.update(self)

    def change_address(self, new_address):
        self._address = new_address
        self.notify()

class Collection(Observer):
    def __init__(self, id):
        self._id = id

    def update(self, data):
        print("observable object changed", data._address, "id:", str(self._id))

obj_user = User()
obj_collection1 = Collection(0)
obj_collection2 = Collection(1)
obj_user.attach(obj_collection1)
obj_user.attach(obj_collection2)

obj_user.change_address("street 17")
obj_user.deattach(obj_collection1)

obj_user.change_address("street 18")
