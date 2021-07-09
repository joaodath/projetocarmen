from modules.extras import check_input, check_input_en

# Character class


class Character():
    def __init__(self, name='Carmen Sandiego', language=2, help_tigress=False,
                 trust_julia=False, missions_count=0):
        self.__name = name
        self.__language = language
        self.__energy = 3
        self.__persuasion = 3
        self.__lucky = 3
        self.__help_tigress = help_tigress
        self.__trust_julia = trust_julia
        self.__missions_count = missions_count

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
    Do you want to change the character name?

    [1] Yes
    [2] No

    Inform your choice: '''

            if check_input(text, [1, 2]) == 1:
                self.__name = input(
                    '''
    Please, inform the character name: ''').strip().title()


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

    def define_atributes(self):
        print('''
    Durante o jogo, você guiará a personagem em escolhas que afetam o resultado final
    da partida. Tais escolhas levam em conta três atributos específicos:

    - Persuasão (0-9)
    - Sorte     (0-9)
    - Energia   (0-9)
        
    Você tem 9 pontos disponíveis para distribuir entre tais atributos. Informe quantos pontos
    irão para cada atributo no passo abaixo.\n\n
        ''')

        while True:
            points = 9
            p = int(input(f'''
    Persuasão    ({points} pontos disponíveis): '''))
            points -= p
            s = int(input(f'''
    Sorte        ({points} pontos disponíveis): '''))
            points -= s
            e = int(input(f'''
    Energia      ({points} pontos disponíveis): '''))
            points -= e
            print('\n\n')

            if (p + s + e) != 9:
                print(f'''
    Opa! Parece que os valores informados não são válidos.
    Tente novamente!
                ''')
            else:
                self.persuasion = p
                self.lucky = s
                self.energy = e

                print(f'''
    Valores cadastrados com sucesso! Seu personagem possui:
    Persuasão    : {self.persuasion}
    Sorte        : {self.lucky}
    Energia      : {self.energy}
                ''')
                break
    

    def define_atributes_en(self):
        print('''
    During the game, you will guide the character in choices that will affect
    the final result of the match. These choices will take in consideration
    three specific attributes:
    
    - Persuasion (0-9)
    - Luck    (0-9)
    - Energy   (0-9)
    
    You have 9 points available to distribute between those attributes.
    Inform how many points will be given to each attribute below. \n\n
    ''')

        while True:
            points = 9
            p = int(input(f'''
    Persuasion    ({points} points available): '''))
            points -= p
            s = int(input(f'''
    Lucky         ({points} points available): '''))
            points -= s
            e = int(input(f'''
    Energy       ({points} points available): '''))
            points -= e
            print('\n\n')

            if (p + s + e) != 9:
                print(f'''
    Ops! It looks like the values informed are not valid.
    Try again!
                ''')
            else:
                self.persuasion = p
                self.lucky = s
                self.energy = e

                print(f'''
    Values saved successfully. Your character has:
    Persuasion   : {self.persuasion}
    Luck         : {self.lucky}
    Energy       : {self.energy}
                ''')
                break


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

    @property
    def missions_count(self):
        self.__missions_count

    def missions_up(self, value):
        self.__missions_count += value
