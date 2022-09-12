def nb_year(p0, percent, aug, p):
    # your code
    current_pop = p0
    years = 0
    
    while p > current_pop:
        increase = int(current_pop*percent/100 + aug)
        # The 'int' is there to round down from any decimals. We don't want to count partial humans.
        current_pop += increase
        years += 1
    return years

# Using Recursion:
def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years