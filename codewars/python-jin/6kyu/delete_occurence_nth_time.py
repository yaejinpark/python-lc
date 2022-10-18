# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
def delete_nth(order,max_e):
    freq = {k:0 for k in set(order)}
    res = []
    for i in order:
        if i in freq:
            if freq[i] < max_e:
                res.append(i)
        freq[i] += 1
    return res