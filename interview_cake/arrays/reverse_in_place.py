def reverse(list_of_chars):
    opp_index = len(list_of_chars) - 1
    for i in range(len(list_of_chars) // 2): # // will return an int for python 3
        list_of_chars[i], list_of_chars[opp_index] = list_of_chars[opp_index], list_of_chars[i]
        opp_index -= 1
        
    return list_of_chars