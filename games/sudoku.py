import random

# for coloring Q1, Q2 ... etc.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_color(pre, post, word):
    if pre == 'H':
        pre = bcolors.OKCYAN

    if post == 'E':
        post = bcolors.ENDC

    print(pre + str(word) + post,end=' ')


def init_board():
    board = []
    for i in range(0,9):
        row_num = [1,2,3,4,5,6,7,8,9]
        for j in range(0,9):
            # random number size row_num
            ban_list = []
            for k in range(0,j):
                ban_list.append(board[i*9+k])
            for k in range(0,i):
                ban_list.append(board[k*9+j])
            if i % 3 == 0:
                # append random number to board
                possible_list = list(set(row_num)-set(ban_list))
                if len(possible_list) == 0:
                    return []
                pos = random.randint(0,len(possible_list)-1)
                num = possible_list.pop(pos)
                row_num.remove(num)
            elif i % 3 == 1:
                # check whether same number from upper 1 line
                if j < 3:
                    ban_list.append(board[(i-1)*9+0])
                    ban_list.append(board[(i-1)*9+1])
                    ban_list.append(board[(i-1)*9+2])
                elif j >= 3 and j < 6:
                    ban_list.append(board[(i-1)*9+3])
                    ban_list.append(board[(i-1)*9+4])
                    ban_list.append(board[(i-1)*9+5])
                elif j >= 6:
                    ban_list.append(board[(i-1)*9+6])
                    ban_list.append(board[(i-1)*9+7])
                    ban_list.append(board[(i-1)*9+8])
                possible_list = list(set(row_num)-set(ban_list))
                if len(possible_list) == 0:
                    return []
                pos = random.randint(0,len(possible_list)-1)
                num = possible_list.pop(pos)
                row_num.remove(num)
            elif i % 3 == 2:
                # check whether same number from upper 2 lines
                if j < 3:
                    ban_list.append(board[(i-2)*9+0])
                    ban_list.append(board[(i-2)*9+1])
                    ban_list.append(board[(i-2)*9+2])
                    ban_list.append(board[(i-1)*9+0])
                    ban_list.append(board[(i-1)*9+1])
                    ban_list.append(board[(i-1)*9+2])
                elif j >= 3 and j < 6:
                    ban_list.append(board[(i-2)*9+3])
                    ban_list.append(board[(i-2)*9+4])
                    ban_list.append(board[(i-2)*9+5])
                    ban_list.append(board[(i-1)*9+3])
                    ban_list.append(board[(i-1)*9+4])
                    ban_list.append(board[(i-1)*9+5])
                elif j >= 6:
                    ban_list.append(board[(i-2)*9+6])
                    ban_list.append(board[(i-2)*9+7])
                    ban_list.append(board[(i-2)*9+8])
                    ban_list.append(board[(i-1)*9+6])
                    ban_list.append(board[(i-1)*9+7])
                    ban_list.append(board[(i-1)*9+8])
                possible_list = list(set(row_num)-set(ban_list))
                if len(possible_list) == 0:
                    return []
                pos = random.randint(0,len(possible_list)-1)
                num = possible_list.pop(pos)
                row_num.remove(num)
            board.append(num)
            if i == 2 and j == 8:
                for n in range(0,3):
                    check = set([])
                    check.add(board[0+(n-1)*3])
                    check.add(board[1+(n-1)*3])
                    check.add(board[2+(n-1)*3])
                    check.add(board[9+(n-1)*3])
                    check.add(board[10+(n-1)*3])
                    check.add(board[11+(n-1)*3])
                    check.add(board[18+(n-1)*3])
                    check.add(board[19+(n-1)*3])
                    check.add(board[20+(n-1)*3])
                    if len(check) != 9:
                        return []
            if i == 5 and j == 8:
                for n in range(0,3):
                    check = set([])
                    check.add(board[27+(n-1)*3])
                    check.add(board[28+(n-1)*3])
                    check.add(board[29+(n-1)*3])
                    check.add(board[36+(n-1)*3])
                    check.add(board[37+(n-1)*3])
                    check.add(board[38+(n-1)*3])
                    check.add(board[45+(n-1)*3])
                    check.add(board[46+(n-1)*3])
                    check.add(board[47+(n-1)*3])
                    if len(check) != 9:
                        return []
            if i == 8 and j == 8:
                for n in range(0,3):
                    check = set([])
                    check.add(board[54+(n-1)*3])
                    check.add(board[55+(n-1)*3])
                    check.add(board[56+(n-1)*3])
                    check.add(board[63+(n-1)*3])
                    check.add(board[64+(n-1)*3])
                    check.add(board[65+(n-1)*3])
                    check.add(board[72+(n-1)*3])
                    check.add(board[73+(n-1)*3])
                    check.add(board[74+(n-1)*3])
                    if len(check) != 9:
                        return []
    return board


def print_board(board,colors):
    for i in range(0,9):
        if i % 3 == 0:
            print('---------------------')
       # print(
       #         board[i*9+0],board[i*9+1],board[i*9+2],'|',
       #         board[i*9+3],board[i*9+4],board[i*9+5],'|',
       #         board[i*9+6],board[i*9+7],board[i*9+8]
       #         )
        for j in range(0,9):
            if i*9+j in colors:
                print_color('H','E',board[i*9+j])
            else:
                print(board[i*9+j],end=' ')
            if j == 2 or j == 5:
                print('|', end = ' ')
        print()
    print('---------------------')



def check_same_lists(l1,l2,n):
    for i in range(0,n):
        if l1[i] != l2[i]:
            return False
    return True


solution = []
while(len(solution) == 0):
    solution = init_board()

board = []
for i in range(0,81):
    board.append('_')

show = int(input("choose how many numbers you want to know?\n"))
poses = []
for i in range(0,81):
    poses.append(i)

for i in range(0,show):
    pos = random.randint(0,len(poses)-1)
    num = poses.pop(pos)
    board[num] = solution[num]

is_game_over = False
while(not is_game_over):
    command = input("What do you want to do? E=End the game, S=Set the value, C=Check the answer, B=Show the board, G=Get value\n")
    if command == 'E':
        is_game_over = True
    elif command == 'B':
        # print_board(solution)
        print_board(board,poses)
    elif command == 'S' or command == 'G':
        row = int(input("input row's number\n"))
        col = int(input("input column's number\n"))
        if command == 'S':
            if row*9+col not in poses:
                print("You cannot change fixed number!")
                continue
            board[row*9+col] = int(input("input the value\n"))
        elif command == 'G':
            print(board[row*9+col])
    elif command == 'C':
        is_game_over = check_same_lists(board,solution,81)
        if is_game_over:
            print('Yes, it is correct! You are successful!')
        else:
            print("Haha, the answer is incorrect, please contniue~ :D")
