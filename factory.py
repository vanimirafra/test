class AnimalSound(object):

    sound = ''

    def get_sound(self):
        return self.sound

class Dog(AnimalSound):

    sound = 'Bark'

class Cat(AnimalSound):

    sound = 'Meow'

class Cow(AnimalSound):

    sound = 'Moo'

class Goat(AnimalSound):

    sound = 'Bleat'

class AnimalSoundFactory():

    def get_animal(self, name):
        target = name.capitalize()
        return globals()[target]()

animal_obj = AnimalSoundFactory()
animals = ['dog', 'cat', 'goat','cow']
for animal in animals:
    print(animal_obj.get_animal(animal).get_sound())