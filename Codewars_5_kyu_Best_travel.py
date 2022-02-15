from itertools import combinations
def choose_best_sum(t, k, ls):
    # your code t - sum miles,  k - number towns, ls - string
    
    d = tuple(combinations(ls, k))
    c = [sum(tup) for tup in d]
    if c and t in c:
        return t
    elif c and min(c) < t:
        c = [i for i in c if i < t]
        a = sorted(c, key=lambda x: (abs(x - t), x))
        return a[0]
    return None
