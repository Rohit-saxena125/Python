user1 = input()
user2 = input()
user1_a= input()
user2_a= input()

def compare(u1, u2):
    if u1 == u2:
        return("tie")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return(user1_a,"win")
        else:
            return(user2_a,"win")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return(user1_a,"win")
        else:
            return(user2_a,"win")
    elif u1 == 'paper':
        if u2 == 'rock':
            return(user1_a,"win")
        else:
            return(user2_a,"win")
    else:
        return("Start new game.")
        sys.exit()

print(compare(user1_answer, user2_answer))