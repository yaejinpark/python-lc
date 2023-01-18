# A runner, who runs with base speed s with duration t will cover a distances d: d = s * t
# However, this runner can sprint for one unit of time with double speed s * 2
# After sprinting, base speed s will permanently reduced by 1, and for next one unit of time runner will enter recovery phase and can't sprint again.

# Your task, given base speed s and time t, is to find the maximum possible distance d.

# Input:
# 1 <= s < 1000
# 1 <= t < 1000

# Example:
# Given s = 2 and t = 4.
# We could schedule when runner should sprint so we could get these possible sequences:

# Seq.: RRRR
# => s + s + s + s
# => 2 + 2 + 2 + 2 = 8
# Seq.: RRRS
# => s + s + s + s*2
# => 2 + 2 + 2 + 2*2 = 10
# Seq.: RRSR
# => s + s + s*2 + (s-1)
# => 2 + 2 + 2*2 + (2-1) = 9
# Seq.: RSRR
# => s + s*2 + (s-1) + (s-1)
# => 2 + 2*2 + (2-1) + (2-1) = 8
# Seq.: RSRS
# => s + s*2 + (s-1) + (s-1)*2
# => 2 + 2*2 + (2-1) + (2-1)*2 = 9
# Seq.: SRRR
# => s*2 + (s-1) + (s-1) + (s-1)
# => 2*2 + (2-1) + (2-1) + (2-1) = 7
# Seq.: SRRS
# => s*2 + (s-1) + (s-1) + (s-1)*2
# => 2*2 + (2-1) + (2-1) + (2-1)*2 = 8
# Seq.: SRSR
# => s*2 + (s-1) + (s-1)*2 + (s-1-1)
# => 2*2 + (2-1) + (2-1)*2 + (2-1-1) = 7

# Where:
# - R: Normal Run / Recovery
# - S: Sprint
# Based on above sequences, the maximum possible distance d is 10.

def solution(s, t):
    
    # Sprints are optimally placed at the end of the race
    '''
    It is always beneficial to sprint at the end of the race
    Sprints are optimally placed at the end of the race
    e.g. RRRR...(SR)[n]S
    We take a run without sprints are keep adding sprints at
    the latest possible point until adding a sprint stops
    increasing the total distance travelled
    
    We can treat the final sprint as an add-on and count the number of
    (SR) units we introduce into the race. Looking at this, each add 
    on unit changes the distance from 2*s to (3*s-3*n), so altering
    the distance by (s-3*n). We find the largest n<s for which (s-3*n)>0
    to find the trade-off point. If this is longer than the race in general
    we do as many (SR) as possible.
    
    
    '''
    trade_off = s//3
    best_n_rs = min((t-1)//2, trade_off) # trade off must be less than max available slots
    d = lambda n: s*t+s*(n+1)-3/2*n*(n+1)
    return d(best_n_rs)



import codewars_test as test
# from solution import solution


@test.describe("Chaser\'s schedule")
def test_group():
    @test.it("Example test case")
    def test_case():
        test.assert_equals(solution(2,4), 10)
