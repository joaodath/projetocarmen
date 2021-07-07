#This function gets the string,splits and print it letter by letter using
#the sleep function from time library as the speedometer
def print_slow(str):
    from time import sleep
    from os import sys 
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.07)

#This function checks if the answer is between the values that the system
#is waiting for. If not, returns a warning in portuguese and waits for 
#the new answer.
def check_input(text, options):
    choice = int(input(text))

    while choice not in options:
        print_slow('Não entendi. Tente novamente.\n')
        choice = int(input(text))

    return choice

#This function checks if the answer is between the values that the system
#is waiting for. If not, returns a warning in english and waits for 
#the new answer.
def check_input_en(text, options):
    choice = int(input(text))

    while choice not in options:
        print_slow('I could\'nt understand. Try again.\n')
        choice = int(input(text))

    return choice

#Character class
class Character():
    def __init__(self, language = 2, name='Carmen Sandiego'):
        self.__name = name
        self.__energy = 3
        self.__hunger = False
        self.__budget = 3
        self.language = language

    def create_character(self):
        if self.language == 2:
            text = '''
    Sua personagem é Carmen Sandiego.
    Você quer alterar o nome da sua personagem?
    
    [1] Sim
    [2] Não
    
    Digite sua opção: '''

            if check_input(text, [1, 2]) == 1:
                self.__name = input(
                    '''
    Por favor, digite o nome da sua personagem: ''').strip().title()

        else:
            text = '''
    Your character name is Carmen Sandiego.
    Você quer alterar o nome da sua personagem?

    [1] Sim
    [2] Não

    Digite sua opção: '''

            if check_input(text, [1, 2]) == 1:
                self.__name = input(
                    '''
    Por favor, digite o nome da sua personagem: ''').strip().title()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

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