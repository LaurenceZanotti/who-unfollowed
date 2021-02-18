import json, sys


def main(argv):
    followers, following, excluded = None, None, []
    
    if len(argv) < 3:
        print("Argumentos faltando. Uso: main.py seguidores.txt seguindo.txt [excluidos.txt] -u [-b]")
        sys.exit(1)

    # Carregar conteúdos dos arquivos
    followers = parseAccounts(argv, 1)
    following = parseAccounts(argv, 2)
    if len(argv) >= 3 and argv[3][0] != "-":
        excluded = parseAccounts(argv, 3)

    # Obter lista de contas que não estão seguindo de volta
    if "-u" in argv:
        unfollowed = unfollowedList(followers, following, argv[3], excluded)

        print("Pessoas que não estão te seguindo de volta:\n")
        for account in unfollowed:
            print(account)
        
        print("")

    # Obter lista de contas que você (usuário) não segue de volta
    if "-b" in argv:
        unfollowed = unfollowedList(following, followers, argv[3], excluded)
        print("Pessoas que você não segue de volta:\n")
        for account in unfollowed:
            print(account)

        print("")
        

def unfollowedList(followers, following, *args):
    """
    Retorna uma lista de pessoas que deixaram de seguir você
    """
    unfollowed = []

    if args[0] != "-": # Se estiver lista de exclusão
        for account in following:
            if account in args[1]:
                continue # Pular para próxima conta
            if account not in followers:
                unfollowed.append(account)
    else:
        for account in following:
            if account not in followers:
                unfollowed.append(account)

    return unfollowed


def parseAccounts(argv, index):
    """
    Converte contas em uma lista independente de ser json ou txt
    """
    try:
        with open(argv[index]) as file:
            if argv[index].find('.json') != -1:
                return json.loads(file.read())
            elif argv[index].find('.txt') != -1:
                arr = []

                for acc in file:
                    arr.append(acc.replace('\n', ''))

                return arr

    except FileNotFoundError:
        print('O arquivo não foi encontrado. Você digitou corretamente ou ele está no mesmo diretório?')
        sys.exit(1)

main(sys.argv)
