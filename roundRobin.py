div1 = ['4','3','2','1']
games = []

def create_schedule(list):
    """ Create a schedule for the teams in the list and return it"""
    s = []


    for i in range(len(list)-1):

        mid = len(list) / 2
        l1 = list[:mid]
        l2 = list[mid:]
        l2.reverse()	

        # Switch sides after each round
        if(i % 2 == 1):
            s = s + [ zip(l1, l2) ]
        else:
            s = s + [ zip(l2, l1) ]

        list.insert(1, list.pop())
        
    return s


def main():
    """for round in create_schedule(div1):
        for match in round:
            print match[0] + " - " + match[1]
    print"""
    for round in create_schedule(div1): 
        for match in round:
            print match[0] + " - " + match[1]
            gameList = []
            gameList.append(match[0])
            gameList.append(match[1])
            games.append(gameList)
        print
    for round in create_schedule(div1): 
        for match in round:
            print match[1] + " - " + match[0]
        print

main()