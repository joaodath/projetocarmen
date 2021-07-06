
def check_input(text, options):
    choice = int(input(text))

    while choice not in options:
        print('Não entendi. Tente novamente.\n')
        choice = int(input(text))

    return choice


class Character():
    def __init__(self, language, name='Carmen Sandiego'):
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
<<<<<<< HEAD
    def naming(self):
        return self.__name_character

    @naming.setter
    def naming(self, name2):
        self.__name_character = name2
=======
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
>>>>>>> aab25ff24d23f270d6fd0760bd0b4a688fc08afb

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