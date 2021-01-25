import json


def main():
    followers = None
    following = None

    with open('followers.json') as file:
        followers = json.loads(file.read())

    with open('following.json') as file:
        following = json.loads(file.read())

    
    unfollowed = unfollowedList(followers, following)

    for i in unfollowed:
        print(i)
        

def unfollowedList(followers, following):
    """
    Return list of people who unfollowed you

    """
    unfollowed = []
    for x in followers:
        if x not in following:
            unfollowed.append(x)



    return unfollowed
                
main()


