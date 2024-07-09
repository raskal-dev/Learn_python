from abc import ABC , abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Chien(Animal):
    def speak(self):
        return "Wouf Wouf"


class Chat(Animal):
    def speak(self):
        return "Miaou Miaou"


mon_chien = Chien()
mon_chat = Chat()

print(mon_chien.speak())
print(mon_chat.speak())