from modules.acts_pt import endings
from modules.extras import print_slow, check_input, clear_screen, check_sucess
from time import sleep

# Starts the game from act 01


def start(player):
    clear_screen()
    # Storytelling
    print_slow(f'''
    Player: O panorama de Xangai é composto por vários dos maiores 
    arranha-céus do mundo, incluindo uma das mais notórias 
    fortalezas da V.I.L.E.

    Pode ir, {player.name}!
    O último andar é onde achará o cofre.

    {player.name}: E os itens recém roubados da V.I.L.E. que estarão 
    neste cofre. Zack, Ivy, estão em posição?

    Ivy: Todo o perímetro está coberto, {player.name}!''')

    sleep(1)
    return building(player)


def building(player):
    clear_screen()
    # Storytelling
    print_slow(f'''
    {player.name}: O prédio com certeza é cheio de seguranças. 
    Qual é a melhor rota até o cofre?
    
    Player: Você pode entrar pelo último andar. Ou pelo primeiro andar.
    
    {player.name}:~ Entrar pelo último andar certamente exigirá manobras 
    arriscadas mas entrando pelo primeiro andar, posso enfrentar oposição. ~ 
    \n''')
    sleep(3)

    clear_screen()
    text = f'''
    Para descobrir o que a V.I.L.E. está escondendo, 
    preciso entrar nesta torre.

    Qual vai ser?

    [1] Último Andar
    [2] Térreo
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return top_building(player)
    else:
        sleep(1)
        return bottom_building(player)


def top_building(player):
    clear_screen()
    # Storytelling
    print(f'''
    {player.name} chega ao topo de um prédio vizinho e 
    prepara sua tirolesa para alcançar o topo do prédio da V.I.L.E.
    ''')
    sleep(3)

    print_slow(f'''
    {player.name}: Eu vou deslizando!''')

    print(f'''
    {player.name} usa um laser para cortar o vidro da fachada 
    do prédio e entrar. Ela cai no armário do zelador.
    ''')
    sleep(3)

    print_slow(f'''
    {player.name}: O armário do zelador???

    Player: Você pediu a rota mais “limpa”! 

    {player.name}: Só mostra o caminho do cofre para eu limpar logo.''')

    print(f'''
    Player envia a rota para {player.name}.''')
    sleep(2)

    return text_vile_vault(player)


def bottom_building(player):
    clear_screen()
    # Storytelling
    print(f'''
    {player.name} está subindo para o andar do cofre 
    usando o vão do elevador.''')

    sleep(2)
    print_slow(f'''
    Player: Sabe mesmo como entrar com estilo, {player.name}!

    {player.name}: Melhor que sorrir para as câmeras do elevador. 
    Eu vou ter cuidado com o vão.''')

    print(f'''
    {player.name} força a abertura da porta do elevador e 
    dá de cara com seguranças. Ela luta e os vence.''')
    sleep(3)

    print_slow(f'''

    ------------
    Vencer essa luta foi custosa!

    Energia: +{player.energy} (-1)
    ------------

    ''')

    print_slow(f'''
    {player.name}: Player, me guie. \n
    
    Player envia a rota para {player.name}.
    ''')
    sleep(1)

    return text_vile_vault(player)


def text_vile_vault(player):
    clear_screen()
    # Storytelling
    print_slow(f'''
    {player.name}: Cofre localizado. Fácil demais…''')

    print(f''' 
    O cofre está vazio, exceto por um pequeno tablet num pedestal 
    no centro do salão do cofre. {player.name} entra e consegue ouvir 
    os líderes da V.I.L.E. falando.''')

    sleep(2)
    print_slow(f'''
    Maelstrom: Bem vinda, {player.name}! Por favor, fique à vontade. 

    {player.name} toca no tablet e um telão é mostrado no cofre com 
    todos os líderes da V.I.L.E..

    {player.name}: Ora, ora. Todos os meus ex-instrutores da escola de crime! 

    Maelstrom: Você é sem dúvida a melhor ladra que já passou pelos 
    corredores da Academia V.I.L.E.. 

    Dra. Bellum: Por tanto, hoje finalmente poderemos brincar 
    de “{player.name}: agente da V.I.L.E.”. 

    {player.name}: Podemos pular para a parte que eu digo não?

    Treinadora Brunt: Oh, nem mesmo para salvar seus destemidos ajudantes?''')

    print('''
    O telão mostra Ivy e Zack, da equipe em terra, amarrados em algum lugar
    difícil de entender onde é.''')
    sleep(3)
    return vile_vault(player)


def vile_vault(player):
    clear_screen()
    print_slow(f'''
    Dra. Bellum: Recuse-se a fazer o nosso jogo e eu juro que vamos apagar a memória deles e 
    iremos reprogramar sua equipe para que se tornem agentes da V.I.L.E.! 

    Player: {player.name}: achei a van do Zack e da Ivy numa câmera de rua. 
    Está em movimento. Acha que consegue alcançar ela?

    {player.name}: ~ Posso tentar salvar o Zack e a Ivy agora, mas seria perigoso. 
    Ou, posso aceitar roubar para a V.I.L.E. até descobrir um jeito de ter a minha equipe de volta. ~
    ''')
    sleep(2)

    clear_screen()
    text = f'''
    O que eu faço?
    Preciso trazê-los de volta em segurança, de algum jeito. 

    [1] Resgatar equipe
    [2] Roubar um Guerreiro de Terracota
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(2)
        return rescue_team_vile_vault(player)
    else:
        sleep(2)
        return steal_statue(player)


def rescue_team_vile_vault(player):
    clear_screen()
    print(f'''
    {player.name} sai correndo do prédio da V.I.L.E. e pula usando o seu planador 
    para seguir a van em movimento.\n ''')
    sleep(3)

    print_slow(f'''
    {player.name}: Estou avistando a van. \n ''')

    print(f'''
    {player.name} consegue pular e entrar na van, mas descobre que 
    está sendo dirigida por controle remoto.''')
    sleep(3)

    print_slow(f'''
    {player.name}: Player, não tem ninguém aqui. \n ''')

    print('''
    A tela do controle remoto acende e mostra os líderes da V.I.L.E. ''')
    sleep(3)

    print_slow(f''' 
    Treinadora Brunt : Ora, ora. Não te disse que ela seria teimosa demais 
    para aceitar nossa proposta?

    Maelstrom: Sim, parece que eu lhe devo um jantar, Treinadora Brunt.
    
    Zack e Ivy são mostrados na tela. A memória deles será apagada em breve!
    ''')
    sleep(2)

    clear_screen()
    print_slow(f'''
    ------------
    Carambas, isso não é bom! A situação agora é irreversível. Entretanto, como
    último recurso, você utilizará sua persuasão para convencer a Treinadora
    Brunt a não apagar a memória dos seus amigos.

    Persuasão: +{player.persuasion}
    ------------
    ....''')

    sleep(3)

    if check_sucess(player.persuasion) == True:
        print_slow(f'''
        {player.name}: Ok, Treinadora Blunt. Você me pegou nessa. Entretanto, eu sou
        sua melhor escolha para o assalto. Eu aceito a proposta. Sem truques
        dessa vez.

        Treinadora Brunt respira fundo, relutante.

        Treinadora Brunt: OK... Você tem uma nova oportunidade. Espero que não a desperdice!
        ''')

        return steal_statue(player)
    else:
        print_slow(f'''
        {player.name}: Ok, Treinadora Blunt. Você me pegou nessa. Entretanto, eu sou
        sua melhor escolha para o assalto. Eu aceito a proposta. Sem truques
        dessa vez.

        Treinadora Brunt: Não cairei nessa ladainha novamente!
        ''')

        return endings.bad_ending_1()  # Used to be Bad Ending 01


def steal_statue(player):
    clear_screen()
    # Storytelling
    print_slow(f'''
    {player.name}: Está bem. Qual é o jogo? 

    Treinadora Brunt: Primeira rodada! Já ouviu falar nos 
    guerreiros de “terracota” chineses? Quero que roube uma estátua para mim.

    Player: O que nós vamos fazer?

    {player.name}: A única coisa que podemos: fazer o jogo da V.I.L.E. 
    até descobrirmos como acharmos Zack e Ivy. 

    Player: Então agora, acho que irá para Xi’ian na China. 
    O Imperador Qin era meio excêntrico. Ele exigiu ser enterrado 
    com milhares desses guerreiros de barro em tamanho real. 

    Você deve ir a um novo sítio de escavação onde recentemente 
    descobriram mais guerreiros.''')

    clear_screen()

    print(f'''
    {player.name} vai para o sítio de escavação.''')
    sleep(3)

    clear_screen()

    print_slow(f'''
    {player.name}: Minha arqui inimiga Tigresa decidiu aparecer. 

    Player: Por que a V.I.L.E. enviaria uma de suas agentes ?

    {player.name}: ~ Para me ajudar ou para me ferrar. Eu posso passar de fininho pela Tigresa
    ou posso falar com a Tigresa e ver se ela entrega onde eles podem estar mantendo Zack e Ivy. ~
    ''')
    sleep(2)

    clear_screen()
    text = f'''  
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
    clear_screen()

    print(f'''
    {player.name} passa de fininho por Tigresa e pula o 
    muro do sítio de escavação, mas encontra vários 
    cães de guarda raivosos.
    ''')
    sleep(4)

    print_slow(f'''
    ------------
    Lute com os cachorros mas mantenha a restrição! Para escapar sem dar
    de cara com a Tigresa, muita energia e sorte será necessária!

    Energia: +{player.energy}
    ------------
    .....
    ''')

    if check_sucess(player.energy) == True:
        print_slow(f'''
    Você consegue escapar dos cães raivosos miraculosamente. Tigresa
    não percebe sua entrada e você segue pelo túnel para o salão de
    escavação dos guerreiros de terracota.
        ''')
        sleep(2)
        return text_security_officer(player)

    print_slow(f'''
    {player.name}: Quando não é gato, é cachorro…
    ''')

    print(f'''
    {player.name} foge e cai do lado de fora do sítio de escavação, 
    de frente para Tigresa. \n''')
    sleep(3)

    print_slow(f'''
    Tigresa: Oh, aqueles cachorrinhos assustaram a valente {player.name}? 
    ''')
    sleep(2)
    return chit_chat_tigress(player)


def chit_chat_tigress(player):
    clear_screen()

    print_slow(f'''
    {player.name}: O que está fazendo aqui? 

    Tigresa: Os líderes acharam que poderia precisar de supervisão pra não 
    estragar sem querer seu próprio roubo. 

    {player.name}: Ou, imaginaram que posso precisar de apoio já que eles 
    sequestraram minha equipe e, portanto, eu estou supervisionando você.
    
    Tigresa: Aproveite enquanto pode.

    Player: Vermelha, achei um túnel na área de escavação. 
    Deve levar direto para os guerreiros.''')

    sleep(2)
    return tunnel_soldier(player)


def tunnel_soldier(player):
    clear_screen()

    print_slow(f'''
    {player.name}: Já que você está aqui. Por acaso saberia onde meus 
    amigos estão sendo mantidos? Eu gostaria de mandar um postal.

    Tigresa: Até parece que eu ia contar.''')

    print(f'''
    Tigresa ativa sem querer uma armadilha e tanto ela quanto {player.name} 
    caem num buraco. {player.name} é mais rápida e escapa. Tigresa fica presa.''')
    sleep(3)

    print_slow(f'''
    {player.name}: Uau! Eu achei que gatos sempre caíssem em pé.

    Tigresa: Me ajuda a sair daqui. Agora!
    
    {player.name}: ~ Só dessa vez eu poderia ajudar a Tigresa. Ou, eu posso deixar que
    ela se vire para sair. ~ ''')
    sleep(2)

    clear_screen()
    text = f''' 
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
    clear_screen()
    player.persuasion_op(+1)

    sleep(0.5)
    print(f'''
    {player.name} joga a corda de sua tirolesa para Tigresa poder sair.''')

    print_slow(f'''
    {player.name}: Vou te ajudar só dessa vez.''')

    print('''\n
    Lembrete: Tigresa vai se lembrar que você a ajudou a escapar.\n''')

    print_slow(f'''
    Tigresa: Ok, ok, obrigada.

    Tigresa acena, relutante. {player.name} se despede, se dirigindo a sua
    missão.''')
    sleep(2)

    clear_screen()

    print_slow(f'''
    ------------
    Parabéns! Sua atitude aumentou seus pontos de Persuasão.

    Persuasão: +{player.persuasion} (+1)
    ------------
    ....
    ''')
    sleep(1)

    player.help_tigress = 1
    return text_security_officer(player)


def leave_tigress(player):
    clear_screen()
    print_slow(f'''
    {player.name}: Eu soube que gatos são excelentes escavadores.''')

    print('''\n
    Lembrete: Tigresa vai se lembrar que você não a ajudou a escapar.\n''')

    print_slow(f'''
    Tigresa: Volta aqui! Tem insetos nesse buraco!

    {player.name}: Não estou te ouvindo! Estou num túnel. O sinal tá ruim…
    ''')
    sleep(2)
    return text_security_officer(player)


def text_security_officer(player):
    clear_screen()
    # Storytelling
    print(f'''
    {player.name} chega no salão de escavação dos guerreiros de terracota e
    faz uma chamada de vídeo para a Treinadora Brunt.''')
    sleep(3)

    print_slow(f'''
    Treinadora Brunt: Espero que seja para falar de um assunto bom.

    {player.name}: Entrei!

    Treinadora Brunt: Ótimo! Estou esperando há horas nessa esteira! 
    Mostra tudo para eu escolher um bom!
    ''')

    print(f'''
    {player.name} mostra os guerreiros para a vilã escolher.''')
    sleep(3)

    print_slow(f'''
    Treinadora Brunt: Aí! Esse aí! Não, o de barba! Não, o de bigode!

    {player.name}: Aceitei roubar pra você, Brunt. Não pra arrumar namorado.

    Treinadora Brunt: Tenho uma equipe de extração circulando na área. 
    Vou dar o sinal para a ação.''')
    sleep(1)

    return security_officer(player)


def security_officer(player):
    clear_screen()

    print(f'''
    A equipe de extração começa a içar a estátua para dentro de um helicóptero quando {player.name} 
    é vista por um segurança.''')

    sleep(3)
    print_slow(f'''
    Segurança: Hey! Quem está aí?

    {player.name}: Player, me flagraram!

    Player: Temos que tirar você daí!

    {player.name}: ~ Posso pular e pegar carona com a estátua ou me camuflar 
    e me esconder com os guerreiros. ~
    ''')
    sleep(3)

    clear_screen()
    text = f'''
    Pular ou camuflar?

    [1] Pegar carona com a estátua
    [2] Se esconder com os outros guerreiros
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return jump_statue(player)
    else:
        sleep(1)
        return hide_statue(player)


def jump_statue(player):
    clear_screen()
    print_slow(f'''
    {player.name} pega carona com a estátua, mas os guardas conseguem pular e 
    se pendurarem nas suas pernas!

    ------------
    Parece que você precisará de sorte para sair dessa sem quebrar a estátua.

    Sorte: +{player.lucky}
    ------------
    ....
    ''')

    if check_sucess(player.lucky) == True:
        print_slow(f'''
    Por sorte, você consegue se livrar dos seguranças e se esconder
    junto com a estátua!
        ''')
        sleep(3)
        return hide_statue(player)

    print_slow(f'''
    A estátua cai no telhado junto com os guardas e se quebra.
    {player.name} consegue fugir em seu planador. 
    ''')
    sleep(3)

    clear_screen()
    print(f'''
    {player.name} recebe uma chamada de vídeo.
    ''')
    sleep(2)

    print_slow(f'''
    Treinadora Brunt: Vejo que o meu noivo por encomenda não conseguiu 
    chegar até mim inteiro.

    {player.name}: Eu pego outro!

    Treinadora Brunt: Infelizmente não, filhinha. Então, vamos decidir os 
    codinomes para os nossos novos agentes? Eu gosto de Tico e Teco!
    ''')

    clear_screen()
    print_slow(f'''
    ------------
    Opa! Hora de utilizar seus dotes para convencer a Treinadora a não 
    limpar a mente dos seus amigos!

    Persuasão: +{player.persuasion}
    ------------
    ''')

    if check_sucess(player.persuasion) == True:
        print_slow(f'''
    {player.name}: Não toque neles! Quero uma segunda chance!

    Treinadora Brunt conversa com Dra. Bellum, aborrecida com
    o ocorrido.

    Dra. Bellum: Apenas mais uma segunda chance. Parece que tem sido
    dias de sorte para você {player.name}. A Treinadora está deveras
    compassiva! Faça uma chamada conosco assim que a poeira baixar.''')

        sleep(1)
        return choose_act_two(player)

    else:
        print_slow(f''')
    {player.name}: Não toque neles! Quero uma segunda chance!

    Treinadora Brunt: Hey, Dra! Hora de carregar o seu… 
    Como se chama mesmo essa coisa? 

    Dra. Bellum: Ele foi rebatizado: O DERRETE MENTES!''')

        sleep(1)
        return endings.bad_ending_2()


def hide_statue(player):
    clear_screen()
    print(f'''
    A estátua é carregada pela equipe de extração. 
    {player.name} está camuflada entre os guerreiros 
    e os seguranças não a encontram. 
    ''')
    sleep(3)
    # Storytelling
    print_slow(f'''
    Segurança: O ladrão fugiu! Vamos! ''')
    sleep(1)

    return choose_act_two(player)


def choose_act_two(player):
    clear_screen()
    # Storytelling
    print(f'''
    Após a missão em Xangai, {player.name} faz uma chamada de vídeo 
    com as líderes da V.I.L.E.
    ''')
    sleep(3)

    print_slow('''
    Condessa Cleo: Então, eu e a Dra Bellum chegamos a um acordo sobre a 
    sua próxima missão. Você que escolhe.

    Dra Bellum: Talvez goste da minha missão, já que envolve explorar 
    o passado distante da terra. 

    Condessa Cleo: Chato. Com o meu roubo, você irá a uma 
    festa extravagante  onde poderá cruzar com ricos e famosos. 
    ''')

    sleep(1)
    text = '''
    Qual missão deseja seguir?

    [1] Missão 1 - Condessa Cleo
    [2] Missão 2 - Dra. Bellum
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        from modules.acts_pt import act_2_m1
        sleep(1)
        return act_2_m1.start(player)
    else:
        from modules.acts_pt import act_2_m2
        sleep(1)
        return act_2_m2.start(player)
