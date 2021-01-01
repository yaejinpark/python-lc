#Library fine calculation

#Actual return date
ad, am, ay = [int(x) for x in input().split(' ')]
#Expected return date
ed, em, ey = [int(x) for x in input().split(' ')]

if(ad,am,ay) == (ed,em,ey):
    print(0)
elif (am,ay) == (em,ey):
    print(15*(ad - ed))
elif ay == ey:
    if am <= em and ad <= ed:
        print(0)
    else:
        print(500*(am-em))
elif ay > ey:
    print(10000)
else:
    print(0)