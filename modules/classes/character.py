from modules.extras import check_input, check_input_en

# Character class


class Character():
    def __init__(self, language=2, name='Carmen Sandiego', help_tigress=False):
        self.__name = name
        self.__energy = 3
        self.__persuasion = 3
        self.__lucky = 3
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

    @energy.setter
    def energy(self, energy):
        self.__energy = energy

    @property
    def persuasion(self):
        return self.__persuasion

    @persuasion.setter
    def persuasion(self, persuasion):
        self.__persuasion = persuasion

    @property
    def lucky(self):
        return self.__lucky

    @lucky.setter
    def lucky(self, lucky):
        self.__lucky = lucky

    @property
    def help_tigress(self):
        self.__help_tigress

    @help_tigress.setter
    def help_tigress(self, value):
        if value == 0:
            self.__help_tigress = bool(False)
        elif value == 1:
            self.__help_tigress = bool(True)
