def jump_to(x, y):
    
    count = 0
    remain = y - (x-1)
    while y > x:
        div = y/2
        dif = y - div 
        if y%2 == 0 and dif >= x:
            y = y/2
            remain -= y
        else:
            y = y - 1
            remain = remain - 1 
        count += 1
    return count
