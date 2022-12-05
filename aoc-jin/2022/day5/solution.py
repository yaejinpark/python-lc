def box_setup():
    f = open('input.txt','r')
    boxes = {k:[] for k in range(1,10)}

    box_counter = 0
    for line in f.readlines():
        current_stack = line.split('\n')
        current_stack = current_stack[0]
        slots = [current_stack[i*4:i*4+3] for i in range(9)]
        
        for i in range(len(slots)):
            if slots[i] != '   ':
                boxes[i+1].append(slots[i][1])
        box_counter += 1
        if box_counter == 8:
            break
    for k,v in boxes.items():
        v.reverse()
    return boxes

def part1():
    boxes = box_setup()
    # print(boxes)
    f = open('input.txt','r')
    line_counter = 1

    for line in f.readlines():
        print(boxes)
        line_counter += 1
        if line_counter >= 12:
            commands = line.rstrip().split(' ')
            num_to_move = int(commands[1])
            source_of_move = int(commands[3])
            target_move = int(commands[-1])
            for i in range(num_to_move):
                moving = boxes[source_of_move].pop()
                boxes[target_move].append(moving)
    res = ''
    for k,v in boxes.items():
        res += v[-1]
    print(res)
# part1()

def part2():
    boxes = box_setup()
    f = open('input.txt','r')
    line_counter = 1
    for line in f.readlines():
        line_counter += 1
        if line_counter >= 12:
            commands = line.rstrip().split(' ')
            num_to_move = int(commands[1])
            source_of_move = int(commands[3])
            target_move = int(commands[-1])
            moving = boxes[source_of_move][-1:-num_to_move-1:-1][::-1]
            boxes[target_move].extend(moving)
            for i in range(num_to_move):
                boxes[source_of_move].pop()

    res = ''
    for k,v in boxes.items():
        res += v[-1]
    print(res)

part1()
part2()