# Implement an extended version of the famous rock-paper-scissors game with the following rules:
# Scissors cuts paper
# Paper covers rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes scissors
# scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# Rock crushes scissors

def rpsls(input1, input2):
    if (input1 == "scissors" and input2 == ("paper" or "lizard")) or \
    (input1 == "paper" and input2 == ("rock" or "spock")) or \
    (input1 == "rock" and input2 == ("lizard" or "scissors")) or \
    (input1 == "lizard" and input2 == ("spock" or "paper")) or \
    (input1 == "spock" and input2 == ("scissors" or "rock")):
        return "Player 1 Won!"
    elif input1 == input2:
        return "Draw!"
    else:
        return "Player 2 Won!"


print(rpsls('scissors', 'lizard'), "expected: Player 1 wins") # for some reason this returns the correct answer here, but fails on codewars

print(rpsls('lizard', 'scissors'), "expected: Player 2 wins")

