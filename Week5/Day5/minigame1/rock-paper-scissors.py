from game import Game

def get_user_menu_choice():
    want_play = input("A.Play a new game\n B. Show scores \n C.Quit \n")
    if want_play in "cC":
        break
    elif want_play.upper()== "A" or want_play.upper()=="B":
        return want_play


def print_results(results):
    #print(result)
    pass

def main():
    while get_user_menu_choice() == True:
        if True:
            play()
        else:
            print_results()

