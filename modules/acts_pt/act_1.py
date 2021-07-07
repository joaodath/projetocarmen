from modules.acts_pt import endings
from modules.extras import print_slow, check_input, clear_screen
from time import sleep

#Starts the game from act 01
def start(player):
    clear_screen()
    #Storytelling
    print_slow(f'''
    Player: O panorama de Xangai é composto por vários dos maiores 
    arranha-céus do mundo, incluindo uma das mais notórias 
    fortalezas da V.I.L.E.

    Câmeras de segurança desativadas e….

    Pode ir, Vermelha!
    O último andar é onde achará o cofre.

    {player.nome}: E os itens recém roubados da V.I.L.E. que estarão 
    neste cofre. Zack, Ivy, estão em posição?

    Ivy: Todo o perímetro está coberto, {player.nome}!

    Zack: Mas vê se toma cuidado lá em cima. 

    {player.nome}: Sempre! Por que hoje seria diferente?

    Zack: A gente tá em Xangai. Ninguém quer que você seja raptada 
    por um dragão chinês, né? 

    Ivy: Nem por ninguém!

    {player.nome}: Eu amo vocês também, equipe em terra. Mantenham o motor 
    ligado e fiquem preparados. 

    ''')
    sleep(1)
    return building(player)


def building(player):
    clear_screen()
    #Storytelling
    print_slow(f'''
    {player.nome}: O prédio com certeza é cheio de seguranças. 
    Qual é a melhor rota até o cofre?
    
    Player: Você pode entrar pelo último andar. Ou pelo primeiro andar.
    
    {player.nome}: Entrar pelo último andar certamente exigirá manobras 
    arriscadas mas entrando pelo primeiro andar, posso enfrentar oposição. 
    
    ''')
    text = f'''
    Para descobrir o que a V.I.L.E. está escondendo, 
    preciso entrar nesta torre.

    Qual vai ser?

    [1] Último Andar
    [2] Térreo
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        return top_building(player)
    else:
        return bottom_building(player)


def top_building(player):
    clear_screen()
    #Storytelling
    print(f'''
    {player.nome} chega ao topo de um prédio vizinho e 
    prepara sua tirolesa para alcançar o topo do prédio da V.I.L.E.
    ''')
    
    sleep(0.5)
    print_slow(f'''
    {player.nome}: Eu vou deslizando!''')
    
    sleep(0.5)
    print(f'''{player.nome} usa um laser para cortar o vidro da fachada 
    do prédio e entrar. Caímos no armário do zelador.''')
    
    sleep(0.5)
    print_slow(f'''
    {player.nome}: O armário do zelador???

    Player: Você pediu a rota mais “limpa”! 

    {player.nome}: Só mostra o caminho do cofre para eu limpar logo.
    ''')
    print(f'''Player envia a rota para {player.nome}.''')
    
    sleep(0.5)
    return vile_vault(player)


def bottom_building(player):
    clear_screen()
    #Storytelling
    print(f'''{player.nome} está subindo para o andar do cofre 
    usando o vão do elevador.
    ''')

    sleep(0.5)
    print_slow(f'''
    Player: Sabe mesmo como entrar com estilo, Vermelha!

    {player.nome}: Melhor que sorrir para as câmeras do elevador. 
    Eu vou ter cuidado com o vão.
    ''')

    sleep(0.5)
    print(f'''{player.nome} força a abertura da porta do elevador e 
    dá de cara com seguranças. 
    ''')
    print(f'''São dois seguranças contra {player.nome}. 
    É uma luta injusta. Para eles. {player.nome} derruba os seguranças.
    ''')

    sleep(0.5)
    print_slow(f''' {player.nome}: Player, me guie. \n''')
    print(f'''Player envia a rota para {player.nome}.''')
    sleep(0.5)
    return text_vile_vault(player)


def text_vile_vault(player):
    clear_screen()
    #Storytelling
    print_slow(f'''{player.nome}: Cofre localizado. Fácil demais…''')

    sleep(0.5)
    print(f''' O cofre está vazio, exceto por um pequeno tablet num pedestal 
    no centro do salão do cofre. {player.nome} entra e consegue ouvir 
    os líderes da V.I.L.E. falando.

    ''')

    sleep(0.5)
    print_slow(f'''
    Maelstrom: Bem vinda, {player.nome}! Por favor, fique à vontade. 

    {player.nome} toca no tablet e um telão é mostrado no cofre com 
    todos os líderes da V.I.L.E..

    {player.nome}: Ora, ora. Todos os meus ex-instrutores da escola de crime! 

    Maelstrom: Você é sem dúvida a melhor ladra que já passou pelos 
    corredores da Academia V.I.L.E.. 

    Condessa Cleo: Embora nós nunca tenhamos colhido os frutos de 
    termos ensinado cada habilidade de roubo que você sabe.

    Dra. Bellum: Por tanto, hoje finalmente poderemos brincar 
    de “{player.nome}: agente da V.I.L.E.”. 

    {player.nome}: Podemos pular para a parte que eu digo não? 
    Porque não sei bem que parte desse último ano os impediu de 
    compreender que eu NUNCA vou roubar para a V.I.L.E..

    Treinadora Brunt: Oh, nem mesmo para salvar seus destemidos ajudantes?
    ''')
    print('''O telão mostra Ivy e Zack, da equipe em terra, 
    amarrados em algum lugar difícil de entender onde é.''')
    return vile_vault(player)

def vile_vault(player):
    sleep(0.5)
    clear_screen()
    print_slow(f'''
    Dra. Bellum: Recuse-se a fazer o nosso jogo e eu juro que os seus 
    coleguinhas serão submetidos aos efeitos do LIMPADOR!

    Condessa Cleo: Você usará isso para limpar os parabrisas 
    ou as burradas deles?

    Dra. Bellum: A memória, Cleo! Se você me deixasse terminar…
    A questão é: depois que limparmos as suas memórias, iremos reprogramar a 
    equipe da {player.nome} para que se tornem agentes da V.I.L.E.! 

    Maelstrom: Então, você roubará para a gente ou serão eles?

    Player: Vermelha, achei a van do Zack e da Ivy numa câmera de rua. 
    Está em movimento. Acha que consegue alcançar ela? 
    ''')

    sleep(0.5)
    clear_screen()
    text = f'''  
    {player.nome}: Posso tentar salvar o Zack e a Ivy agora, mas estaria 
    arriscando a segurança deles. Ou, posso aceitar roubar para a V.I.L.E. 
    até descobrir um jeito de ter a minha equipe de volta.

    O que eu faço?
    Preciso trazê-los de volta em segurança, de algum jeito. 

    [1] Resgatar equipe
    [2] Roubar um Guerreiro de Terracota
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return rescue_team_vile_vault(player)
    else:
        sleep(1)
        return steal_statue(player)


def rescue_team_vile_vault(player):
    clear_screen()
    print(f'''
    {player.nome} sai correndo do prédio da V.I.L.E. e 
    pula usando o seu planador para seguir a van em movimento. \n ''')
    
    sleep(0.5)
    print_slow(f'''{player.nome}: Estou avistando a van. \n ''')
    print(f'''{player.nome} consegue pular e entrar na van, mas descobre que 
    está sendo dirigida por controle remoto.''')
    
    sleep(0.5)
    print_slow(f''' {player.nome}: Player, não tem ninguém aqui. \n ''')
    print('A tela do controle remoto acende e mostra os líderes da V.I.L.E. ')

    sleep(0.5)
    print_slow(f''' 
    Treinadora Brunt : Ora, ora. Não te disse que ela seria teimosa demais 
    para aceitar nossa proposta?

    Maelstrom: Sim, parece que eu lhe devo um jantar, Treinadora Brunt. \n ''')
    print('''Zack e Ivy são mostrados na tela. O Limpador é usado neles. 
    Fim de jogo. \n ''')

    sleep(1)
    print_slow(f'''Narradora: Uh, isso não é bom. {player.nome} merece outra 
    chance de resgatar a sua equipe. E, felizmente, você pode ter essa 
    segunda chance. Talvez ela possa roubar para a V.I.L.E. 
    até conseguir passar a perna neles. 
    ''')
    sleep(1)
    return vile_vault(player) #Used to be Bad Ending 01


def steal_statue(player):
    clear_screen()
    #Storytelling
    print_slow(f'''
    {player.nome}: Está bem. Qual é o jogo? 

    Treinadora Brunt: Primeira rodada! Já ouviu falar nos 
    guerreiros de “terraboda” chineses?

    {player.nome}: Terracota! Não acha que roubar oito mil estátuas 
    é exagerado, Treinadora Brunt? 

    Treinadora Brunt: Só uma já serve.

    {player.nome}: Aposto que vão fazer um belo vaso de terracota para você.

    Treinadora Brunt: Sapateira, na verdade. 
    Para minha bota de terra de treinamento. Agora, faça o que faz de melhor, 
    agente, e roube para a V.I.L.E. e não contra nós.

    Player: O que nós vamos fazer?

    {player.nome}: A única coisa que podemos: fazer o jogo da V.I.L.E. 
    até descobrirmos como acharmos Zack e Ivy. 

    Player: Então agora, acho que irá para Xi’ian na China. 
    O Imperador Qin era meio excêntrico. Ele exigiu ser enterrado 
    com milhares desses guerreiros de barro em tamanho real. 

    A tumba dele foi criada para ser uma cidade subterrânea com vários tipos 
    de túneis de fuga e armadilhas para afastar intrusos. 

    Você deve ir a um novo sítio de escavação onde recentemente 
    descobriram mais guerreiros.
    ''')
    print(f'{player.nome} vai para o sítio de escavação.')

    sleep(0.5)
    clear_screen()
    print_slow(f'''
    {player.nome}: Ou é a terça informal para a equipe de segurança ou 
    minha arqui inimiga Tigresa decidiu aparecer. 

    Player: Por que a V.I.L.E. enviaria uma de suas agentes se é você quem 
    deve fazer o roubo para eles?

    {player.nome}: Para me ajudar ou para me ferrar.
    ''')

    text = f'''  
    {player.nome}: Eu posso passar de fininho pela Tigresa já que não me 
    importo de saber isso ou posso falar com a Tigresa e ver se 
    ela entrega onde eles podem estar mantendo Zack e Ivy.

    Passar de fininho ou bater um papinho? 
    Preciso decidir antes que ela me veja.

    [1] Passar de fininho
    [2] Bater um papinho
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return sneak_tigress(player)
    else:
        sleep(1)
        return chit_chat_tigress(player)


def sneak_tigress(player):
    sleep(0.5)
    clear_screen()
    print(f'''
    {player.nome} passa de fininho por Tigresa e pula o 
    muro do sítio de escavação, mas encontra vários 
    cães de guarda raivosos. ''')
    print_slow(f'{player.nome}: Quando não é gato, é cachorro… \n')
    sleep(0.5)
    print(f'''
    {player.nome} foge e cai do lado de fora do sítio de escavação, 
    de frente para Tigresa. \n''')
    print_slow(f'''
    Tigresa: Oh, aqueles cachorrinhos assustaram a valente {player.nome}? 
    ''')
    return chit_chat_tigress(player)


def chit_chat_tigress(player):
    sleep(0.5)
    print_slow(f'''
    {player.nome}: O que está fazendo aqui? 

    Tigresa: Os líderes acharam que poderia precisar de supervisão pra não 
    estragar sem querer seu próprio roubo. 

    {player.nome}: Ou, imaginaram que posso precisar de apoio já que eles 
    sequestraram minha equipe e, portanto, eu estou supervisionando você.
    
    Tigresa: Aproveite enquanto pode.

    Player: Vermelha, achei um túnel na área de escavação. 
    Deve levar direto para os guerreiros.

    {player.nome}: Seja uma boa subordinada e fique de guarda. 
    Tenho trabalho a fazer.
    ''')

    return tunnel_soldier(player)


def tunnel_soldier(player):
    sleep(0.5)
    clear_screen()
    print_slow(f'''
    Tigresa: Que pena! Quando seus amigos tiverem os cérebros zerados, 
    não vão mais lembrar de você. 

    {player.nome}: Já que você está aqui. Por acaso saberia onde meus 
    amigos estão sendo mantidos? Eu gostaria de mandar um postal.

    Tigresa: Até parece que eu ia contar. Olha aqui, depois que ficarem 
    sem memória, acho que vou reprogramar os seus amigos para serem 
    MEUS amigos. “Mack” e “Lily” vão andar com a Tigresa! 
    ''')

    sleep(0.5)
    print(f'''
    Tigresa ativa sem querer uma armadilha e tanto ela quanto {player.nome} 
    caem num buraco. {player.nome} é mais rápida e usa sua tirolesa 
    automática para prender uma corda no teto do túnel e escapar. 
    Tigresa fica presa. 
    ''')
    print_slow(f'''
    {player.nome}: Uau! Eu achei que gatos sempre caíssem em pé.

    Tigresa: Me ajuda a sair daqui. Agora!
    ''')
    text = f''' 
    {player.nome}: Só dessa vez eu poderia ajudar a Tigresa. 
    Ou, eu posso deixar que ela se vire para sair. 
    Enfim, é a gata aqui que está no comando agora.

    [1] Ajudar Tigresa
    [2] Deixar Tigresa se virar

    Sua escolha: '''
    
    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return help_tigress(player)
    else:
        sleep(1)
        return leave_tigress(player)


def help_tigress(player):
    sleep(0.5)
    print(f'''
    {player.nome} joga a corda de sua tirolesa para Tigresa poder sair.
    ''')
    print_slow(f'{player.nome}: Vou te ajudar só dessa vez.')
    print('Lembrete: Tigresa vai se lembrar que você a ajudou a escapar.')
    print_slow(f'''
    Tigresa: Pera aí, o quê?

    {player.nome}: Eu sei que gatos gostam de linhas!
    ''')
    return 


def leave_tigress(player):
    sleep(0.5)
    print_slow(f'''
    {player.nome}: Eu soube que gatos são excelentes escavadores.
    ''')
    print('Lembrete:Tigresa vai se lembrar que você não a ajudou a escapar.')
    print_slow(f'''
    Tigresa: Volta aqui! Tem insetos nesse buraco!

    {player.nome}: Não estou te ouvindo! Estou num túnel. O sinal tá ruim…
    ''')
    return 

def security_officer(player):
    clear_screen()
    #Storytelling
    print_slow('''Storytelling aqui''')
    text = '''
    Um segurança te viu!

    Pular com estátua ou se camuflar? 
    
    [1] Pular com estátua
    [2] Se Camuflar
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return jump_statue(player)
    else:
        sleep(1)
        return hide_statue(player)


def jump_statue(player):
    clear_screen()
    sleep(1)
    return endings.bad_ending_2(player)


def hide_statue(player):
    clear_screen()
    #Storytelling
    print_slow('''
    Você se camuflou e conseguiu fugir!\n
    ''')
    sleep(1)
    return choose_act_two(player)


def choose_act_two(player):
    clear_screen()
    #Storytelling
    print_slow('''
    Agora você pode escolher entre a missão da Dra. Bellum ou a missão da Condessa Cleo.
    
    Na missão da Dra. Bellum, você irá explorar o passado do planeta.
    Na missão da Condessa Cleo, você irá para uma festa onde poderá cruzar com ricos e famosos!

    ''')
    sleep(1)
    text = '''
    Qual missão deseja seguir?

    [1] Missão 1 - Dra Bellum.
    [2] Missão 2 - Condessa Cleo.
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        from modules.acts_pt import act_2_m1
        sleep(1)
        return act_2_m1.start(player)
    else:
        from modules.acts_pt import act_2_m2
        sleep(1)
        return act_2_m2.start(player)
