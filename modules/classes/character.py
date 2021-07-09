from modules.extras import check_input, check_input_en

# Character class


class Character():
    def __init__(self, name='Carmen Sandiego', language=2, help_tigress=False,
                trust_julia=False):
        self.__name = name
        self.__language = language
        self.__energy = 3
        self.__persuasion = 3
        self.__lucky = 3
        self.__help_tigress = help_tigress
        self.__trust_julia = trust_julia

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

    @energy.setter
    def energy(self, energy):
        self.__energy = energy

    def energy_op(self, value):
        self.__energy += value

    @property
    def persuasion(self):
        return self.__persuasion

    @persuasion.setter
    def persuasion(self, persuasion):
        self.__persuasion = persuasion

    def persuasion_op(self, value):
        self.__persuasion += value

    @property
    def lucky(self):
        return self.__lucky

    @lucky.setter
    def lucky(self, lucky):
        self.__lucky = lucky

    def lucky_op(self, value):
        self.__lucky += value

    @property
    def help_tigress(self):
        self.__help_tigress

    @help_tigress.setter
    def help_tigress(self, value):
        if value == 0 or value == '0':
            self.__help_tigress = bool(False)
        elif value == 1 or value == '1':
            self.__help_tigress = bool(True)
    
    @property
    def trust_julia(self):
        self.__trust_julia

    @trust_julia.setter
    def trust_julia(self, value):
        if value == 0 or value == '0':
            self.__trust_julia = bool(False)
        elif value == 1 or value == '1':
            self.__trust_julia = bool(True)
