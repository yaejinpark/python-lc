# THIS CODE IS DESIGNED TO PERFORM MARKOV CHAIN
# CALCULATIONS ON STOCHASTIC TRANSITIONAL MATRICES

# 'steps' refers to the number of recursive cyles you wish to perform
# 'trans_matrix' refers to a stochastic matrix, and each list contained within
#     should reflex a HORIZONTAL row of the matrix.
# 'initial state' should reflect the VERTICAL A/B values of the given initial state

trans_matrix = [[0.2,0.9],[0.8,0.1]]
initial_state = [.5,.5]
steps = 3

def markov_chain(matrix, state, steps, count=1):
    if count == 1:
        print(f'------------------\nInitial State: {state}\n------------------')
    new_state = []
    for i in matrix:
        res = 0
        display = ''
        for idx, val in enumerate(i):
            res += val * state[idx]
            display += f' ({val} * {state[idx]}) +'
        print(display.lstrip(' ').rstrip(' + '), f'= {round(res, 3)}')
        new_state.append(round(res, 3))
    steps -= 1
    if steps == 0:
        print(f'------------------\nFinal State (#{count}): {new_state}\n------------------')
    else:
        print(f'------------------\nTransitional State (#{count}): {new_state}\n------------------')
        return markov_chain(matrix, new_state, steps, count+1)

markov_chain(trans_matrix, initial_state, steps)

