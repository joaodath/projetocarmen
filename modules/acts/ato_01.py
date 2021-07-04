def act_one():
    return invadir_predio()


def invadir_predio():
    choice = input('''Invadir pelo último andar ou térreo?
    [1] Último Andar
    [2] Térreo''')
    if choice == 'Último Andar':
        return pelo_ultimo_andar()
    else:
        return pelo_terreo()


def pelo_ultimo_andar():
    return cofre_da_vile()


def pelo_terreo():
    return cofre_da_vile()


def cofre_da_vile():
    choice = input('''Resgatar equipe ou roubar um guerreiro?
    [1] Regatar equipe
    [2] Roubar um Guerreiro''')
    if choice == 'Resgatar equipe':
        return resgatar_equipe()
    else:
        return roubar_um_guerreiro()


def resgatar_equipe():
    print('É uma emboscada.')
    return 1


def roubar_um_guerreiro():
    return fugir_seguranca()


def fugir_seguranca():
    choice = input('''Pular com estátua ou se camuflar? 
    [1] Pular com estátua
    [2] Se Camuflar''')
    if choice == 'Pular junto com a estátua':
        return pular_com_estatua()
    else:
        return se_camuflar()


def pular_com_estatua():
    print('Você caiu.')
    return 2


def se_camuflar():
    return 'Iniciar ato 2.'
