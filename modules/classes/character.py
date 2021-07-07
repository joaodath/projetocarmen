from modules.extras import check_input, check_input_en

# Character class


class Character():
    def __init__(self, language=2, name='Carmen Sandiego', help_tigress=False):
        self.__name = name
        self.__energy = 3
        self.__persuasao = 3
        self.__language = language
        self.__help_tigress = help_tigress

    def create_character(self):
        if self.__language == 2:
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

    @property
    def help_tigress(self):
        self.__help_tigress

    @help_tigress.setter
    def help_tigress(self, value):
        if value == 0:
            self.__help_tigress = bool(False)
        elif value == 1:
            self.__help_tigress = bool(True)
