from abc import ABC, abstractmethod
from typing import Generic, TypeVar

class Eatable(ABC):
    pass

class Meal(Eatable):
    def __init__(self, energy: int):
        self._energy = energy

    @property
    def energy(self) -> int:
        return self._energy

class Water(Eatable):
    def __init__(self, liquid: int):
        self._liquid = liquid

    @property
    def liquid(self) -> int:
        return self._liquid
    
class Milk(Meal, Water):
    def __init__(self, energy: int, liquid: int):
        self._energy = energy
        self._liquid = liquid

T = TypeVar('T', bound=Eatable)

class Animal(ABC, Generic[T]):
    @abstractmethod
    def say(self) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def eat(self, food: T) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def move(self) -> None:
        raise NotImplementedError()
    

class Cat(Animal[Eatable]):
    def __init__(self, energy:int=110, liquid:int=90) -> None:
        self.energy = energy
        self.liquid = liquid

    def say(self) -> str:
        if self.is_hungry:
            return 'Meow Meow'
        else:
            return 'Meow'
    
    def eat(self, food: Eatable) -> None:
        if isinstance(food, Meal):
            self.energy += food.energy
        if isinstance(food, Water):
            self.liquid += food.liquid

    def move(self) -> None:
        self.energy -= 8
        self.liquid -= 5

    @property
    def is_hungry(self) -> bool:
        return self.energy < 50 or self.liquid < 60

class Dog(Animal[Eatable]):
    def __init__(self, energy:int=120, liquid:int=80) -> None:
        self.energy = 110
        self.liquid = 100

    def say(self) -> str:
        if self.is_hungry:
            return 'Woof Woof'
        else:
            return 'Woof'
    
    def eat(self, food: Eatable) -> None:
        if isinstance(food, Meal):
            self.energy += food.energy
        if isinstance(food, Water):
            self.liquid += food.liquid

    def move(self) -> None:
        self.energy -= 10
        self.liquid -= 6

    @property
    def is_hungry(self) -> bool:
        return self.energy < 55 or self.liquid < 50
