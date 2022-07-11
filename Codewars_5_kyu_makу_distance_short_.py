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


def variance(numbers): 
    # your code here
    sum, variance = 0, 0
    sum_list = 0
    for nu in numbers:
        sum_list += nu
    len_num = int(len(numbers))
    mean = sum_list/len_num
    
    for num in numbers:
        print(num)
        num = (num - mean)**2 / len(numbers)
        variance += num
    return variance
    pass
