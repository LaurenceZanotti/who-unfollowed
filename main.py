import json, sys


def main(argv):
    followers, following, excluded = None, None, []
    
    if len(argv) < 3:
        print("Missing arguments. Usage: main.py followers.txt following.txt [exclusion.txt] -u [-b]")
        sys.exit(1)

    try:
        with open(argv[1]) as file:
            followers = json.loads(file.read())

        with open(argv[2]) as file:
            following = json.loads(file.read())

        if len(argv) >= 3 and argv[3][0] != "-":
            with open(argv[3]) as file:
                for acc in file:
                    excluded.append(acc.replace('\n','')) # Replace newline


    except FileNotFoundError:
        print(f'File was not found. Did you type it correctly or is it in the same directory?')
        sys.exit(1)

    print(type(excluded), excluded)

    # Retrieve list of accounts that are not following back
    if "-u" in argv:
        unfollowed = unfollowedList(followers, following)

        print("People who doesn't follow you back:\n")
        for i in unfollowed:
            print(i)
        
        print("")

    # Retrive list of accounts that you don't follow back
    if "-b" in argv:
        unfollowed = unfollowedList(following, followers)
        print("People who you don't follow back:\n")
        for i in unfollowed:
            print(i)

        print("")
        

def unfollowedList(followers, following):
    """
    Return list of people who unfollowed you

    """
    unfollowed = []
    for x in following:
        if x not in followers:
            unfollowed.append(x)


    return unfollowed


main(sys.argv)
