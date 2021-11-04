import random


class Game:
    def __init__(self):
        self.game= ["rock", "paper", "scissors"]
    def get_user_item(self):
        user_item = input("select an item (rock/paper/scissors)") 
        while not user_item in self.game:
            user_item = input("select an item (rock/paper/scissors)") 
        return user_item

    def get_computer_item(self):
        comp_item = random.choice(self.game)
        return comp_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            end = "draw"
        elif user_item == "scissors" and computer_item =="paper":
            end = "win"
        elif user_item == "paper" and computer_item =="rock":
            end = "win"
        elif user_item == "rock" and computer_item =="scissors":
            end = "win"
        elif comp_item == "scissors" and user_item =="paper":
            end = "lose"  
        elif comp_item == "paper" and user_item =="rock":
            end = "lose" 
        elif comp_item == "rock" and user_item =="scissors":
            end = "lose" 
        return end


    def play(self):
        user_turn = self. get_user_item()
        comp_turn = self.get_computer_item()
        result = self.get_game_result(user_turn, comp_turn)
        print(f"You selected {user_turn}. The computer selected {comp_turn}. You {result}.")

new_game=Game()
print(new_game.play())
