import json, sys


def main(argv):
    followers, following, excluded = None, None, []
    
    if len(argv) < 3:
        print("Missing arguments. Usage: main.py followers.txt following.txt [exclusion.txt] -u [-b]")
        sys.exit(1)

    # Load contents of the files
    followers = parseAccounts(argv, 1)
    following = parseAccounts(argv, 2)
    if len(argv) >= 3 and argv[3][0] != "-":
        excluded = parseAccounts(argv, 3)

    # Retrieve list of accounts that are not following back
    if "-u" in argv:
        unfollowed = unfollowedList(followers, following, argv[3], excluded)

        print("People who doesn't follow you back:\n")
        for account in unfollowed:
            print(account)
        
        print("")

    # Retrive list of accounts that you (user) don't follow back
    if "-b" in argv:
        unfollowed = unfollowedList(following, followers, argv[3], excluded)
        print("People who you don't follow back:\n")
        for account in unfollowed:
            print(account)

        print("")
        

def unfollowedList(followers, following, *args):
    """
    Return list of people who unfollowed you
    """
    unfollowed = []

    if args[0] != "-": # If there's an exclusion file
        for account in following:
            if account in args[1]:
                continue # Skip to next account
            if account not in followers:
                unfollowed.append(account)
    else:
        for account in following:
            if account not in followers:
                unfollowed.append(account)

    return unfollowed


def parseAccounts(argv, index):
    """
    Parse accounts in a list whether the data is json or txt
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
        print('File was not found. Did you type it correctly or is it in the same directory?')
        sys.exit(1)

main(sys.argv)
