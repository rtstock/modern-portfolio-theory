##def constrained_sum_sample_pos(n, total):
##    """Return a randomly chosen list of n positive integers summing to total.
##    Each such list is equally likely to occur."""
##    import random
##    dividers = sorted(random.sample(xrange(-1 * total, total), n - 1))
##    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
##
##print constrained_sum_sample_pos(10, 100)
##


def unconstrained_sample_posneg(l, h , total, divisor):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    #import random
    #dividers = sorted(random.sample(xrange(1, total), n - 1))
    #return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
    import random
    l1 = l * 100.0
    h1 = h * 100.0
    lst = []
    for i in range(1,total):
        lst.append(random.randrange(l1,h1,5)/100.0/divisor)
    return lst

import random
print random.randrange(-5,5,1)
x = unconstrained_sample_posneg(-5,5,1000,100.0)
i = 0
for a in x:
    i += 1
    print i,a

