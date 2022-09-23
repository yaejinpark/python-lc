# https://www.codewars.com/kata/5ae840b8783bb4ef79000094/train/python
def merge(*dicts):
    res = {}
    for i in range(len(dicts)):
        if dicts[i]:
            for k,v in dicts[i].items():
                if k not in res:
                    res[k] = [v]
                else:
                    res[k].append(v)
    return res