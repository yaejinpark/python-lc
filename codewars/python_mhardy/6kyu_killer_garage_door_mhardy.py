# Situation
# You have been hired by a company making electric garage doors. 
# Accidents with the present product line have resulted in numerous damaged cars, 
# broken limbs and several killed pets. Your mission is to write a safer version of their controller software.

# Specification
# We always start with a closed door. The remote control has exactly one button, with the following behaviour.

# If the door is closed, a push starts opening the door, and vice-versa
# It takes 5 seconds for the door to open or close completely
# While the door is moving, one push pauses movement, another push resumes movement in the same direction
# In order to make the door safer, it has been equiped with resistance-based obstacle detection. 
# When the door detects an obstacle, it must immediately reverse the direction of movement.

# Input
# A string where each character represents one second, with the following possible values.

# '.' No event
# 'P' Button has been pressed
# 'O' Obstacle has been detected (supersedes P)
# As an example, '..P....' means that nothing happens for two seconds, then the button is pressed, then no further events.

# Output
# A string where each character represents one second and indicates the position of the door 
# (0 if fully closed and 5 fully open). The door starts moving immediately, 
# hence its position changes at the same second as the event.

# Example
# ..P...O..... as input should yield 001234321000 as output

def controller(events):

    current = 0
    output = ''
    mode = ''
    direction = 'up'
    for i in [*events]:
        if not mode:
            if i == '.':
                output += str(current)
            if i == 'P':
                mode = 'P'
                current += 1
                output += str(current)
        elif mode == 'P':
            if i == '.':
                if direction == 'up':
                    current += 1
                    if current <= 5:
                        output += str(current)
                    else:
                        current = 5
                        output += str(current)
                elif direction == 'down':
                    current -= 1
                    if current >= 0:
                        output += str(current)
                    else:
                        current = 0
                        output += str(current)
            elif i == 'P' and current != 5 and current != 0:
                output += str(current)
                mode = 'PAUSE'
            elif i == 'P' and current == 5:
                current -= 1
                output += str(current)
                direction = 'down'
            elif i == 'P' and current == 0:
                current += 1
                output += str(current)
                direction = 'up'
            elif i == 'O':
                if direction == 'up':
                    current -= 1
                    output += str(current)
                    direction = 'down'                   
                elif direction == 'down':
                    current += 1
                    output += str(current)
                    direction = 'up'
        elif mode == 'PAUSE':
            if i == '.':
                output += str(current)
            elif i == 'P':
                if direction == 'up':
                    current += 1
                    output += str(current)
                    mode = 'P'
                elif direction == 'down':
                    current -= 1
                    output += str(current)
                    mode = 'P'

    return output


# JIN'S MORE EFFICIENT SOLUTION:

# def controller(events):
#     time = 0
#     res = ""
#     moving = False
#     direction = 1
        
#     for event in events:
#         if event == 'P':
#             moving = not moving
#         elif event == 'O':
#             direction *= -1
#         if moving:
#             time += direction
#         if time in (0,5):
#             if time == 0:
#                 moving = False
#                 direction = 1
#             else:
#                 moving = False
#                 direction = -1
#         res += str(time)
#     return res




import codewars_test as test


test.describe('Uninterrupted operation')
test.assert_equals(controller('..........'), '0000000000')
test.assert_equals(controller('P....'), '12345')

test.describe('Operation paused')
test.assert_equals(controller('P.P..'), '12222')

test.describe('Obstacle detected')
test.assert_equals(controller('..P...O...'), '0012343210')
