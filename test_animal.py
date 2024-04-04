
from animal import Animal, Cat, Dog, Eatable, Milk


def test_cat():
    siamese: Animal[Eatable] = Cat(energy=120, liquid=85)

    assert siamese.say() == "Meow"
    for _ in range(10):
        siamese.move()
    
    assert siamese.say() == "Meow Meow"
    for _ in range(5):
        siamese.eat(Milk(energy=10, liquid=5))

    assert siamese.say() == "Meow"

def test_dog():
    doberman: Animal[Eatable] = Dog(energy=130, liquid=75)

    assert doberman.say() == "Woof"
    for _ in range(10):
        doberman.move()

    assert doberman.say() == "Woof Woof"
    for _ in range(5):
        doberman.eat(Milk(energy=10, liquid=5))

    assert doberman.say() == "Woof"