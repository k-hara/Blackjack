# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
       return 0
    elif name == "Spock":
         return 1
    elif name == "paper":
         return 2
    elif name == "lizard":
         return 3
    elif name == "scissors":
         return 4
    else:
          return "invalid choice"


def number_to_name(number):
    if number == 0:
       return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "invalid choice" 

def rpsls(player_choice): 
    print ""
    player_number = name_to_number(player_choice)
    if player_number == "invalid choice":
        print player_number
    else:
        print "Player chooses", player_choice   
        import random 
        comp_number = random.randrange(0, 5)
        comp_name = number_to_name(comp_number)
        print "Computer chooses", comp_name
        result = (player_number - comp_number) % 5
        if result == 0:
            print "Player and computer tie!"
        elif (result == 1) or (result == 2):
            print "Player wins!"
        else:
            print "Computer wins!"
        
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
