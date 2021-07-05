class Character():
    def __init__(self, name1 = 'Carmen Sandiego'):
        self.__name_character = name1
        self.__energy = 3
        self.__hunger = False
        self.__budget = 3

    @property
    def naming(self):
        return self.__name_character

    @naming.setter
    def naming(self, name2):
        self.__name_character = name2

    @property
    def energy(self):
        return self.__energy

    def increase_energy(self, value=1):
        self.__energy += value

    def decrease_energy(self, value=1):
        self.__energy -= value

    @property
    def hunger(self):
        return self.__hunger

    def eat_something(self):
        self.__hunger = False

    def be_hungry(self):
        self.__hunger = True

    @property
    def budget(self):
        return self.__budget

    def increase_budget(self, value):
        self.__budget += value

    def decrease_budget(self, value):
        self.__budget -= value