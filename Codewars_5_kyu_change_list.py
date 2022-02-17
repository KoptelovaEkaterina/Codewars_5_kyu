def move_zeros(array):
    count = 0
    new_list = []
    zero_list = []
    for i in range(len(array)):
        if array[i] == 0:
            zero_list.append(array[i])
        else:
            new_list.append(array[i])
    for i in range(len(zero_list)):
        new_list.append(zero_list[i])
    return new_list
