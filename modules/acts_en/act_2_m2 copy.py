from modules.acts_pt import endings
from modules.extras import print_slow, check_input, clear_screen
from time import sleep

# Starts Act 02 from Mission 02


def start_m2(player):
    player.missions_up(1)
    return in_the_lab(player)


def in_the_lab(player):
    clear_screen()
    # Storytelling
    print_slow(f'''
    {player.name} O que você quer Dra Bellum? Códigos de lançamentos?
    Armas Biológicas? Uma máquina de repetição de vídeos de gatos?

    Dra Bellum - Eu quero que me traga um osso, e é por isso que 
    vou lhe mandá-la a Hell Creek, Montana, EUA, para conseguir 
    um osso de dinossauro. Tyrannosaurus Rex, para ser mais específica,
    um que foi descoberto com tecido mole intacto.

    {player.name} – Você não quer clonar...
    
    Dra Bellum – Se alguém vai tentar essa proeza da natureza, serei eu!

    {player.name}: Player, eu vou para Hell Creek.
    ''')
    sleep(2)
    clear_screen()
    print_slow(''' 
    Player - Montana significa montanha em espanhol. Há um bilhão de anos, 
    muitos dinossauros vagaram por Hell Creek.
    ''')
    sleep(1)

    print(f'''
    {player.name} chega à Hell Creek e está observando o 
    sítio arqueológico de longe. 
    ''')
    sleep(3)

    print_slow(f'''
    {player.name} - Osso do quadril, osso da coxa. 
    Onde está afinal esse T-Rex? 

    {player.name} - com seu binóculo detecta onde está o osso, 
    tira uma foto e envia para o Player

    Player – E temos o osso de dinossauro!

    {player.name} - Levaram para o avião. Consegue descobrir o destino?

    Player - Há um laboratório de pesquisa a 300km daí. Qual o seu plano?
    
    {player.name}: Parece que vamos fazer uma visitinha ao laboratório.
    ''')
    sleep(1)

    clear_screen()

    print(f'''
    Dra Bellum liga para {player.name}.''')
    sleep(3)

    print_slow(f'''
    Dra Bellum: Tic Tac Srta {player.name}. Você está em Montana a tarde toda 
    e ainda não conseguiu o osso do dinossauro. 
    Como consegue nos superar tantas vezes se é tão ineficiente? 

    {player.name}: Não costumo trabalhar sozinha. 

    Dra Bellum: Não pensei que dependia tanto dos seus ajudantes. 

    {player.name}: Eles não são meus agentes. São meus amigos. 

    Dra Bellum: Pensei que estivesse brincando. Muito bem. 
    Vou enviar El Topo para ajudar. 
    ''')
    sleep(2)

    clear_screen()

    print(f'{player.name} chega ao laboratório')
    sleep(3)

    print_slow(f'''
    {player.name}: Que laboratório é esse? 

    Player: Museu e parque de dinossauros. 
    Convenientemente fechado à noite. 

    {player.name}: O osso está lá dentro. El Topo está atrasado.
    ''')
    sleep(1)

    print('''
    El Topo aparece saindo de dentro de um túnel de esgoto.''')
    sleep(3)

    print_slow(f'''
    El Topo: Perdão pelo atraso. Estava pesquisando possíveis rotas de fuga. 
    
    {player.name}: Vamos acabar logo com isso. El Topo, você me dá cobertura.
    Player, me guie.
    ''')
    sleep(1)

    print(f'''
    {player.name} está entrando no laboratório.
    El Topo avisa que a ACME já está no lugar.
    ''')
    sleep(3)

    clear_screen()

    text = '''
    Você irá se esconder da ACME ou correr para roubar o osso?

    [1] Esconder
    [2] Fugir

    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return hide(player)
    else:
        sleep(1)
        return run(player)


def hide(player):
    print_slow(f'''
    {player.name}: Droga! Perdi a oportunidade de capturar o osso!

    {player.name} recebe uma ligação da Dra Bellum.

    Dra Bellum: Ora ora. Já lhe dei muitas oportunidades. Dessa vez, será
    sua última!

    {player.name}: Não!''')

    clear_screen()
    return endings.bad_ending_3(player)


def run(player):
    clear_screen()

    print(f''''
    {player.name} corre para pegar o osso.
    ''')
    sleep(3)

    print(f'''
    Ela encontra o osso e consegue fugir com a ajuda de El Topo. 
    {player.name} liga para Dra Bellum.
    ''')
    sleep(3)

    print_slow(f'''
    {player.name}:O osso está comigo. 
    Dra Bellum: Fantástico. Entrarei em contato para maiores informações. 
    ''')
    sleep(1)

    return vile_safebox(player)


def vile_safebox(player):
    clear_screen()

    print_slow(f'''
    {player.name}: Player, alguma pista de onde está Zack e Ivy?

    Player: {player.name}, achei um sinal!
    Buscando esconderijos da V.I.L.E no Círculo Ártico. 
    Encontrei um. O que quer fazer?

    {player.name}: ~ Posso tentar resgatar minha equipe agora ou posso roubar
    para a V.I.L.E. uma última vez. Uma nova missão pode ser arriscada,
    mas também pode ser uma chance de manter as aparências até conseguir
    recuperar a equipe. ~
    ''')
    sleep(1)

    clear_screen()

    text = '''
    Você irá resgatar seus amigos agora ou roubar mais uma vez?

    [1] Resgatar Equipe
    [2] Roubar mais uma vez para a V.I.L.E.
    '''
    if check_input(text, [1, 2]) == 1:
        return rescue_team(player)
    else:
        return steel_again(player)


def rescue_team(player):
    clear_screen()
    from modules.acts_pt import act_3a
    return act_3a.start_3a(player)


def steel_again(player):
    clear_screen()
    if player.missions_count == 2:
        clear_screen()
        print_slow(f'''
    Todas as missões já foram realizadas. Prosseguindo para o Resgate de
    seus amigos...

        ''')
        sleep(5)
        from modules.acts_pt import act_3b
        return act_3b.start_3b(player)
    else:
        from modules.acts_pt import act_2_m1
        return act_2_m1.start_m1(player)
