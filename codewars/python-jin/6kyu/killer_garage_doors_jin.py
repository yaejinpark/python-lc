# https://www.codewars.com/kata/58b1ae711fcffa34090000ea/solutions/python
def controller(events):
    time = 0
    res = ""
    moving = False
    direction = 1
        
    for event in events:
        if event == 'P':
            moving = not moving
        elif event == 'O':
            direction *= -1
        if moving:
            time += direction
        if time in (0,5):
            if time == 0:
                moving = False
                direction = 1
            else:
                moving = False
                direction = -1
        res += str(time)
    return res