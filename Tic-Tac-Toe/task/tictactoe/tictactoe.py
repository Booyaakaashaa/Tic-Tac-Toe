# write your code here
def printTTT(tic, countO = 0, countX = 0):
    is_emp = False
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for t in range(3):
            print(tic[t + 3 * i], end=" ")
            if tic[t + 3 * i] == " ":
                is_emp = True
            if tic[t + 3 * i] == "O":
                countO += 1
            if tic[t + 3 * i] == "X":
                countX += 1
        print("|")
    print("---------")
    return countO, countX, is_emp


def game(tic, is_empty, inp):

    if is_empty:
        while 1:
            x = input("Enter the coordinates: ").split()
            if len(x) == 1:
                print("You should enter numbers!")
                continue
            else:
                x, y = x[0], x[1]
            if not x.isnumeric() or not y.isnumeric():
                print("You should enter numbers!")
                continue
            x, y = int(x) - 1, int(y) - 1
            loc = 3 * x + y
            if loc < 0 or loc > 8 or y > 2:
                print("Coordinates should be from 1 to 3!")
                continue
            if tic[loc] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            tic[loc] = inp
            if 0 <= loc <= 8:
                break


def winner(tic):
    out = " "
    if tic[0] == tic[1] == tic[2]:
        out = tic[0]
    elif tic[0] == tic[3] == tic[6]:
        out = tic[0]
    elif tic[0] == tic[4] == tic[8]:
        out = tic[0]
    if tic[3] == tic[4] == tic[5]:
        if out != " " and out != tic[3]:
            return "Impossible"
        out = tic[3]
    elif tic[1] == tic[4] == tic[7]:
        if out != " " and out != tic[1]:
            return "Impossible"
        out = tic[1]
    elif tic[2] == tic[4] == tic[6]:
        if out != " " and out != tic[2]:
            return "Impossible"
        out = tic[2]
    if tic[6] == tic[7] == tic[8]:
        if out != " " and out != tic[8]:
            return "Impossible"
        out = tic[8]
    elif tic[2] == tic[5] == tic[8]:
        if out != " " and out != tic[8]:
            return "Impossible"
        out = tic[8]
    if out == " ":
        out = False
    return out


# Main Code
tic = [" "]*9
countO = 0
countX = 0
dat = 'X'
move = 0
countO, countX, is_empty = printTTT(tic, countO, countX)

while 1:
    game(tic, is_empty, dat)
    countO, countX, is_empty = printTTT(tic, countO, countX)
    result = winner(tic)
    if not result and not is_empty:
        print("Draw")
        break
    if result:
        print(result + " wins")
        break
    move += 1
    if move & 1:
        dat = 'O'
    else:
        dat = 'X'
