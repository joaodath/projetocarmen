from modules.acts_pt import endings
from modules.extras import check_sucess, print_slow, check_input, clear_screen
from time import sleep

# Starts Mission 1 from Act 2


def start_m1(player):
    clear_screen()
    sleep(2)
    print_slow(f'''
    {player.name}: Está bem condessa Cleo. O que seu coração sombrio deseja? 
    Condessa Cleo: Para minha missão, quero que roube o último lote de um 
    caviar Beluga. Será servido numa festa de caridade em Mônaco. 

    Player: Localizado na Riviera Francesa, Mônaco é o segundo 
    menor país do mundo. A festa será num luxuoso hotel em Monte Carlo.
    
    {player.name} viaja para o local, visando realizar a tarefa proposta.
    ''')

    sleep(2)
    return party(player)


def party(player):
    clear_screen()
    # Storytelling
    print(f'''
    {player.name} chega à festa. 
    O anfitrião a vê e se dirige a seu encontro.''')

    sleep(2)
    print_slow(f'''
    Anfitrião da Festa: Me daria a honra dessa dança, Srta...?

    {player.name}: Santa Rosa! Srta. Santa Rosa.

    Anfitrião da Festa: Me daria a honra dessa dança, Srta. Santa Rosa?

    {player.name}: ~ Estou em missão, então deveria me concentrar e recusar. 
    Mas aceitar a dança pode ser o melhor jeito de me misturar e 
    chegar à cozinha. ~
    ''')
    sleep(3)

    clear_screen()
    text = f'''
    Devo dançar ou prosseguir com o plano?

    [1] Dançar
    [2] Recusar a dança

    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return dance(player)
    else:
        sleep(1)
        return refuse_dance(player)


def dance(player):
    clear_screen()
    player.persuasion_op(+1)
    player.energy_op(-1)

    print_slow(f'''
    ------------
    Participar de uma bela dança com o Anfitrião da Festa foi uma ótima decisão.
    Entretanto, fazer isso lhe custou algumas coisinhas.

    Persuação: +{player.persuasion} [+1]
    Energia: +{player.energy} [-1]
    ------------
    .....
    ''')
    sleep(3)

    return talking_with_julia(player)


def refuse_dance(player):
    player.persuasion_op(-1)

    print_slow(f'''
    {player.name} : Obrigado, mas valsa não é minha praia. Se quiser dançar
    tango...

    O Anfitrião se despede cordialmente e vai embora. 

    ------------
    Opa! As vezes é bom realizar alguns sacrifícios 
    para se misturar no local...

    Persuação: +{player.persuasion} [-1]
    ------------
    ....
    ''')
    sleep(3)

    return talking_with_julia(player)


def talking_with_julia(player):
    print(f'{player.name} é abordada por outra agente da ACME.')
    print_slow(f'''
    Julia: {player.name}?

    {player.name}: Não quer dizer Scarlet Santa Rosa? 

    Julia: Sim. É claro. É bom te ver novamente senhorita Sta Rosa. 
    Posso presumir porque está aqui. Soubemos que um agente da V.I.L.E 
    está atrás do caviar Beluga. Aposto que está aqui para pegá-los 
    antes que o roubem. 

    {player.name}: É… Algo assim.

    Julia: Com certeza já soube do recente roubo do guerreiro chinês de 
    terracota. Eu ficaria aliviada se um tesouro roubado aparecesse na 
    minha porta e me permitisse devolvê-lo às autoridades. 

    Player: Só que dessa vez a entrega será feita à V.I.L.E e não à ACME.

    {player.name}: Talvez eu possa explicar isso à ela. 

    Player: Podemos confiar na Julia?
    ''')

    text = f'''
    {player.name}: Já me aliei a ela antes. 
    Confiar nela pode funcionar de novo. 
    Mas, se a V.I.L.E souber que estou de conluio com a ACME, 
    quem sabe o que farão? 

    [1] Confiar na Júlia
    [2] Enrolar a Júlia

    '''
    if check_input(text, [1, 2]) == 1:
        sleep(1)
        return trust_julia(player)
    else:
        sleep(1)
        return not_trust_julia(player)


def trust_julia(player):
    print_slow(f'''
    {player.name}: Julia, escuta. 
    Sou a agente enviada para roubar o caviar Beluga. 

    Julia: Não entendo. Por que roubaria para V.I.L.E?

    {player.name}: É só o que posso falar agora. 
    Peço que confie nos meus motivos. 


    Julia: Que sejam bons motivos, Srta Santa Rosa. 
    ''')
    print('Júlia vai se lembrar que você confiou nela.')
    player.trust_julia = 1
    sleep(2)
    return steel_caviare(player)


def not_trust_julia(player):
    print_slow(f'''
    {player.name}: Júlia, escuta. Você tem razão em estar desconfiada. 
    Preciso te mostrar uma coisa.
    ''')
    print(f'{player.name} segue para as escadas com Júlia.')
    sleep(1)
    print_slow(f'''
    {player.name}: A V.I.L.E. está de prontidão no telhado agora. 
    Temos que agir rápido! Anda! Não temos muito tempo!
    ''')
    print(f'''
    Júlia tenta chamar reforços usando sua caneta espiã mas {player.name} 
    toma de sua mão rapidamente quando ela passa pela porta que dá no telhado.
    ''')

    sleep(1)
    print(f'{player.name} tranca Júlia no telhado.')
    print_slow(f'{player.name}: Foi mal, Júlia. Sério mesmo.')
    print('Júlia vai se lembrar que você não confiou nela.')
    player.trust_julia = 0
    sleep(2)
    return steel_caviare(player)


def steel_caviare(player):
    clear_screen()
    print(f'''
    {player.name} observa dois garçons indo para a cozinha.
    ''')
    sleep(2)

    print_slow(f'''
    {player.name}: Avistei as ovas. 
    
    Player: Como você vai pegar?

    {player.name}: Posso esconder e sair furtivamente, 
    ou pegar e sair correndo.
    ''')
    sleep(3)

    clear_screen()
    text = f'''
    Disfarço e escondo o caviar ou roubo e saio correndo?
    
    [1] Disfarçar e Capturar
    [2] Roubar e Correr
    
    Sua escolha: '''

    if check_input(text, [1, 2]) == 1:
        clear_screen()

        print_slow(f'''
    ------------
    Ótima escolha! Entretanto, você precisará de sorte para o disfarce ser de
    acordo com o planejado.

    Sorte: +{player.lucky}
    ------------
    ....
        ''')
        sleep(2)

        if check_sucess(player.lucky) == True:
            sleep(1)
            return hide(player)
        else:
            clear_screen()
            print(f'''
    Infelizmente o disfarce não deu muito certo... Um garçom reconheceu você!
            ''')
            sleep(3)
            return run(player)
    else:
        sleep(1)
        return run(player)


def hide(player):
    clear_screen()

    print(f'''
    {player.name} se disfarça como garçonete para capturar os caviares. 
    Entretanto um imprevisto acontece! Como houve um tempo decorrido 
    para o disfarce, os caviares já foram removidos de suas latas e empratados!
    ''')

    sleep(2)
    print(f'''
    {player.name} captura os caviares dos pratos e os põe em uma vasilha e 
    foge furtivamente. Após sair da festa, entra em contato com a 
    Condessa Cleo.
    ''')
    
    sleep(2)
    clear_screen()
    print_slow(f'''
    {player.name}: O caviar está servido.

    Condessa Cleo: Que grosseria! Fora das latas, deixou a iguaria exposta!

    {player.name}: Você queria ovas de peixe, eu entreguei.
    
    Condessa Cleo: Foi o que fez. Mas agora só vão durar um dia! 
    E não posso consumir cem latas de caviar em um dia. 
    Dra Bellum, ative o... seja lá qual for o nome disso hoje!

    {player.name}: Não!
    ''')

    sleep(2)
    print(f'''
    Guardas surgem na prisão onde os amigos de {player.name} estão. 
    Eles tentam lutar mas é em vão. Suas mentes serão apagadas.''')
    sleep(3)

    clear_screen()
    print_slow(f'''
    ------------
    OH NÃO! Parece que estamos em um grande impasse. 
    Hora de testar seus limites!
    Você tentará convencer a Condessa Cleo a salvar seus amigos.
    
    Persuasão: +{player.persuasion}
    ------------
    .....
    ''')
    sleep(2)

    if check_sucess(player.persuasion) == True:
        clear_screen()
        print_slow(f'''
    {player.name} implora por uma nova oportunidade.

    {player.name}: Por favor, me dê uma nova oportunidade! Prometo que darei
    meu máximo em ser discreta. Afinal, sou a melhor opção que vocês possuem.
    
    Condessa Cleo afirma, relutante.

    Condessa Cleo: Está bem! Mas essa será sua última tentativa! Aguarde novas
    instruções.
        ''')
        sleep(2)
        return steel_again(player)

    else:
        clear_screen()
        print(f'''
    {player.name} implora por uma nova oportunidade.

    {player.name}: Por favor, me dê uma nova oportunidade! Prometo que darei
    meu máximo em ser discreta. Afinal, sou a melhor opção que vocês possuem.

    Condessa Cleo: Não mesmo! Apenas uma tola confiaria em uma ladra. 
    Continuem o procedimento!
        ''')
        sleep(2)
        endings.bad_ending_5()


def run(player):
    clear_screen()

    print(f'''
    {player.name} sai da cozinha com um carrinho com o caviar
    ''')

    print_slow(f'''
    Garçonete grita da cozinha: Mademoiselle, pare! 
    O caviar precisa ser empratado!

    Anfitrião: Peguem-na! 

    {player.name}: Prefiro a saída dramática.
    ''')
    print(f'''
    {player.name} pega o caviar, chuta o carrinho e salta voo com o planador. 
    ''')
    sleep(3)

    clear_screen()
    print(f'{player.name} liga para Condessa Cleo.')
    sleep(2)

    print_slow(f'''
    {player.name}: Peguei os bebês Beluga. 

    Condessa Cleo: Por favor, aguarde novas instruções. 
    ''')
    sleep(2)

    return steel_again(player)


def steel_again(player):
    print(f'''
    {player.name} conversa com Player sem que Condessa Cleo consiga ouvir.
    ''')
    sleep(2)

    print_slow(f'''
    {player.name}: Player, alguma pista de Zac e Ivy? 

    Player: Ainda não. Estou procurando, mas nada ainda.
    Fique na chamada com a Condessa Cleo por mais alguns segundos,
    estou tentando rastrear.
    ''')
    sleep(1)

    print('''
    Condessa Cleo parece estressada na chamada.
    ''')
    sleep(2)

    print_slow(f'''
    Condessa Cleo: Conversando com mais alguém, {player.name}?
    Pelo visto estou atrapalhando alguma coisa. 
    Você deve ter assuntos mais importantes que a vida da sua equipe.

    {player.name}: Nada disso, Condessa! 
    Estou apenas admirada pela sofisticação de seu look hoje.

    Player: {player.name}, achei um sinal!
    Buscando esconderijos da V.I.L.E no Círculo Ártico. 
    Encontrei um. O que quer fazer?

    {player.name}: ~ Posso tentar resgatar minha equipe agora ou posso roubar
    para a V.I.L.E. uma última vez. Uma nova missão pode ser arriscada,
    mas também pode ser uma chance de manter as aparências até conseguir
    recuperar a equipe. ~
    ''')
    sleep(3)

    clear_screen()
    text = f'''
    Começo uma arriscada missão de resgate, ou roubo pela última vez?

    [1] Resgatar Equipe
    [2] Roubar uma última vez
    
    Sua Escolha: '''

    if check_input(text, [1, 2]) == 1:
        sleep(1)
        player.missions_count
        from modules.acts_pt import act_3a
        return act_3a.start_3a(player) #Used to be a Good Ending
    else:
        sleep(1)
        player.missions_count
        from modules.acts_pt import act_2_m2
        return act_2_m2.start_m2(player)  # Used to be Bad Ending 4