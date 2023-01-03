# https://www.codewars.com/kata/59e270da7997cba3d3000041/train/python
def zero_plentiful(arr):
    zeros = [z for z in ''.join('0' if i == 0 else ' ' for i in arr).strip().split()]
    seq_counter = 0
    for i in zeros:
        if len(i) >= 4:
            seq_counter += 1
        if len(i) < 4:
            return 0
    return seq_counter 