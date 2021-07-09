from modules.acts_pt import endings
from modules.extras import print_slow, check_input, clear_screen
from time import sleep

#Starts Act 02 from Mission 02
def start_m2(player):
    clear_screen()
    return in_the_lab(player)


def in_the_lab(player):
    clear_screen()
    #Storytelling
    print_slow(f'''{player.nome} O que você quer Dra Bellum? Códigos de lançamentos? Armas Biológicas? Repetição de vídeos de gatos?
        Dra Bellum - Eu quero que me traga um osso, e é por isso que vou lhe mandá-la a Hell Creek, Montana, EUA, para conseguir um osso de dinossauro. Tyrannosaurus Rex, para ser mais específica, um que foi descoberto com tecido mole intacto.

        {player.name} – Não vai clonar........ (Dra Bellum corta a fala da Carmen) 
     
        Dra Bellum – Se alguém vai tentar essa proeza da natureza, serei eu!
        {player.name} Ahhh eu Vou para Hell Creek.''')
    sleep(1)
    clear_screen() 
    print_slow(f''' Player - Montana significa montanha em espanhol. Há um bilhão de anos, muitos dinossauros vagaram por Hell Creek.

         {player.name} - Osso do quadril, osso da coxa. Onde está afinal esse T-Rex? 

         {player.name} - com seu binóculo detecta onde está o osso e tira uma foto e envia para o Player

        Player – E temos o osso de dinossauro

        {player.name} - Levaram para o avião. Consegui descobrir o destino?

        Player - Há um laboratório de pesquisa a 300km daí. Qual o seu plano?

      ''')
    sleep(1)
    clear_screen()
    text = '''
    Você irá se esconder da ACME ou fugir com o osso?

    [1] Esconder
    [2] Fugir

    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return hide(player)
    else:
        return run(player)


def hide(player):
    clear_screen()
    return endings.bad_ending_3(player)


def run(player):
    clear_screen()
    return vile_safebox(player)


def vile_safebox(player):
    clear_screen()
    #Storytelling
    print_slow(f'''{player.name}-Alguma pista onde está Zakk e Ivy? 
    Player – nada ainda estou procurando esse tipo de tijolos e janelas
    {player.name}-Estamos ficando sem tempo.''')
    sleep(1)
    clear_screen() 
    print_slow(f''' {player.name}- chama no comunicador a V.I.L.E e fala que não irá roubar mais se não tiver mais provas que os seus amigos estão bem.
    {player.name}- Consegui convencer um dos chefes da V.I.L.E a mostrar mais uma vez os seus amigos e logo após ela tira uma foto e manda para o Player.
    {player.name}- compare as duas imagens e veja o sol na janela. Quais são as chances de ter a mesma luminosidade em horários diferentes.
    Player - Pode ser Luz artificial
    {player.name}- ou eles estão no único lugar na terra em que sol brilha de dia e de noite nesta época do ano.
    Player-Buscando esconderijo da V.I.L.E no círculo ártico… Encontrei um local. O quer fazer vermelha?
    ''')
    text = '''
    Você irá resgatar seus amigos agora ou roubar mais uma vez?

    [1] Resgatar Equipe
    [2] Ir para próxima missão

    '''
    if check_input(text, [1, 2]) == 1:
        return rescue_team(player)
    else:
        return steel_again(player)


def rescue_team(player):
    clear_screen()
    return endings.good_ending_1(player)


def steel_again(player):
    clear_screen()
    return endings.bad_ending_4(player)
