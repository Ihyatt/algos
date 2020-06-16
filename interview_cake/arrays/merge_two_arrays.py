def merge_lists(my_list, alices_list):

    my_pointer = alice_pointer = 0 
    merged = list()
    while my_pointer < len(my_list) and alice_pointer < len(alices_list):
        if my_list[my_pointer] < alices_list[alice_pointer]:
            merged.append(my_list[my_pointer])
            my_pointer += 1
        else:
            merged.append(alices_list[alice_pointer])
            alice_pointer += 1
        
    for i in range(my_pointer, len(my_list)):
        merged.append(my_list[i])
        
    for i in range(alice_pointer, len(alices_list)):
        merged.append(alices_list[i])


    return merged