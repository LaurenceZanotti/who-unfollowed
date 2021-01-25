import json, sys


def main(argv):
    followers = None
    following = None
    
    if len(argv) != 3:
        print("Missing arguments. Usage: main.py followers.txt following.txt -u")
        sys.exit(1)

    try:
        with open(argv[1]) as file:
            followers = json.loads(file.read())
    except FileNotFoundError:
        print(f'File {argv[1]} doesn\'t exist. Was it typed correctly or is it in the same directory?')
        sys.exit(1)

    try:
        with open(argv[2]) as file:
            following = json.loads(file.read())
    except FileNotFoundError:
        print(f'File {argv[2]} doesn\'t exist. Was it typed correctly or is it in the same directory?')
        sys.exit(1)

    # Retrieve list of accounts that are not following back
    if "-u" in argv:
        unfollowed = unfollowedList(followers, following)
        print("People who doesn't follow you back:\n")
        for i in unfollowed:
            print(i)
    else:
            print("Missing argument. Usage: main.py [-u] for accounts that unfollowed you.")

    if "-b" in argv:
        unfollowed = unfollowedList(following, followers)
        print("People who you don't follow back:\n")
        for i in unfollowed:
            print(i)
        

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


