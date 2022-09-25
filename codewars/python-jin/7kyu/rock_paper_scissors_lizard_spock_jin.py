# https://www.codewars.com/kata/57d29ccda56edb4187000052
def rpsls(input1, input2):
    if input1 == "scissors" and (input2 == "paper" or input2 == "lizard") or \
    input1 == "paper" and (input2 =="rock" or input2=="spock") or \
    input1 == "rock" and (input2 == "lizard" or input2=="scissors") or \
    input1 == "lizard" and (input2 == "spock" or input2=="paper") or \
    input1 == "spock" and (input2 == "scissors" or input2=="rock"):
        return "Player 1 Won!"
    elif input1 == input2:
        return "Draw!"
    else:
        return "Player 2 Won!"