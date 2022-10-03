n = '21/23'
import math
def decompose(n):
    x=2
    denom= []
    nums=n.split('/')
    ratio =float(int(nums[0]) / int(nums[1]))
    # ratio = 0.66
    while ratio > 0 and x <100000000:
        if (1/x) > ratio:
            x += 1
            # print (ratio)
        else:
            denom.append(x)
            ratio = ratio - (1/math.ceil(1/ratio))
            x +=1
    print(ratio)
    print(denom)
decompose(n)  
# end