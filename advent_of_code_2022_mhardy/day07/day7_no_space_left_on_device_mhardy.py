

file = open('input.txt','r')

total = 0
dir_dict = {'/': 0}
current_key = "/"
previous_keys = []
counter = 1
for i in file.readlines():
    line_list = i.rstrip().split(" ")
    print(counter, previous_keys, current_key, dir_dict[current_key])
    if line_list[1] == 'cd':
        if line_list[2] not in previous_keys and line_list[2] != '..' and line_list[2] != '/':
            previous_keys.append(current_key)
            current_key = line_list[2]
            if current_key not in dir_dict.keys():
                dir_dict[current_key] = 0
        elif line_list[2] == '..':
            if len(previous_keys) >= 1:
                current_key = previous_keys[-1]
                del previous_keys[-1]
            else:
                current_key = '/'
        # elif line_list[2] == '/':
        #     current_key = '/'
        #     del previous_keys[:]
    elif line_list[0].isnumeric():
        if current_key not in dir_dict.keys():
            dir_dict[current_key] = int(line_list[0])
            for i in previous_keys:
                dir_dict[i] += int(line_list[0])
        else:
            dir_dict[current_key] += int(line_list[0])
            for i in previous_keys:
                dir_dict[i] += int(line_list[0])

    
    counter += 1
    if counter % 150 == 0:
        print(dir_dict)

print(dir_dict)

for i in dir_dict.values():
    if i <= 100000:
        total += i

print(total)
    