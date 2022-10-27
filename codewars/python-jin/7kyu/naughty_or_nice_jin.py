# https://www.codewars.com/kata/5662b14e0a1fb8320a00005c/train/python
def naughty_or_nice(data):
    nn_count = 0
    months = []
    
    for month in data:
        months.append(month)
    
    for i in range(len(months)):
        current_month = data[months[i]]
        for k,v in current_month.items():
            if current_month[k] == 'Naughty':
                nn_count -= 1
            else:
                nn_count += 1
    
    return 'Nice!' if nn_count >= 0 else 'Naughty!'