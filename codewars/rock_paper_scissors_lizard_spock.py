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
    if (input1 == "scissors" and (input2 == "paper" or input2 == "lizard")) or \
    (input1 == "paper" and (input2 == "rock" or input2 =="spock")) or \
    (input1 == "rock" and (input2 == "lizard" or input2 =="scissors")) or \
    (input1 == "lizard" and (input2 == "spock" or input2 =="paper")) or \
    (input1 == "spock" and (input2 == "scissors" or input2 == "rock")):
        return "Player 1 Won!"
    elif input1 == input2:
        return "Draw!"
    else:
        return "Player 2 Won!"


print(rpsls('scissors', 'lizard'), "expected: Player 1 wins") 

print(rpsls('lizard', 'scissors'), "expected: Player 2 wins")

import codewars_test as test


@test.describe('rock paper scissors lizard spock')
def test():
    @test.it('Player 1 Won!')
    def _():
        test.assert_equals(rpsls('rock', 'lizard'), 'Player 1 Won!')
        test.assert_equals(rpsls('paper', 'rock'), 'Player 1 Won!')
        test.assert_equals(rpsls('scissors', 'lizard'), 'Player 1 Won!')
        test.assert_equals(rpsls('lizard', 'paper'), 'Player 1 Won!')
        test.assert_equals(rpsls('spock', 'rock'), 'Player 1 Won!')
    
    @test.it('Player 2 Won!')
    def _():
        test.assert_equals(rpsls('lizard','scissors'), 'Player 2 Won!')
        test.assert_equals(rpsls('spock','lizard'), 'Player 2 Won!')
        test.assert_equals(rpsls('paper','lizard'), 'Player 2 Won!')
        test.assert_equals(rpsls('scissors','spock'), 'Player 2 Won!')
        test.assert_equals(rpsls('rock','spock'), 'Player 2 Won!')

    @test.it("Draw!")
    def _():
        test.assert_equals(rpsls('rock', 'rock'), 'Draw!')
        test.assert_equals(rpsls('spock', 'spock'), 'Draw!')