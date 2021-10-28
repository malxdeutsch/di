my_list = [" "," "," "," "," "," "," "," "," "]
def display_board():
    tb_line = "*" * 13
    line1 = f"* {my_list[0]}| {my_list[1]}| {my_list[2]}| *"
    line_mid = "*" + ("-"*2) + "|"+ ("-"*2) + "|"+ ("-"*2) + "|" +" "+"*"
    line2 = f"* {my_list[3]}| {my_list[4]}| {my_list[5]}| *"
    line3 = f"* {my_list[6]}| {my_list[7]}| {my_list[8]}| *"
    print(tb_line)
    print(line1)
    print(line_mid)
    print(line2)
    print(line_mid)
    print(line3)
    print(tb_line)
display_board()

def take_a_turn(player):
    location= int(input("Type the number of the place where you wanna go? Each place has a value of 0-8 with the top row from L-R is 0,1,2 and the bottom row L-R is 6,7,8"))
    while location > 9 or my_list[location] in ["X","O"]:
        location= int(input("Type the number of the place where you wanna go? Each place has a value of 0-8 with the top row from L-R is 0,1,2 and the bottom row L-R is 6,7,8"))
    my_list[location] = player
   
def check(winning_list):
    for winners in winning_list:
        print(winners)
        while winners[0]== winners[1]==winners[2] != " ":
            if winners[0]== winners[1]==winners[2]:
                print(f"The winner is {winners[0]}")
                return True
    return False

def tic_tac_toe():
    player = "X" 
    for turn in range(9):
        take_a_turn(player)
        display_board()
        winning_list = [[my_list[0],my_list[1],my_list[2]] , [my_list[3],my_list[4],my_list[5]], [my_list[6],my_list[7],my_list[8]], [my_list[0],my_list[3],my_list[6]], [my_list[1],my_list[4],my_list[7]], [my_list[2],my_list[5],my_list[8]], [my_list[0],my_list[4],my_list[8]], [my_list[2],my_list[4],my_list[6]]]
        if check(winning_list):
            break
        if player == 'X':
            player = 'O'
            continue
        else:
            player = "X"
            continue
    
tic_tac_toe()
    
