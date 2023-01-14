total = 150
max_take = 28
game = False

def get_total():
    global total
    return total

def get_max_take():
    global max_take
    return max_take

def take_candy(take: int):
    global total
    total -= take

def check_game():
    global game
    return game

def new_game():
    global game, total
    if game:
        game = False
    else:
        total = 150
        game = True

