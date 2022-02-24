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
