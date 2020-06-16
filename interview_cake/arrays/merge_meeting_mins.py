def merge_ranges(meetings):
    meetings.sort() #sort in place for merging algos
    condensed_meetings = list() #create a new list
    curr = [meetings[0][0], meetings[0][1]] #initial list for comparison
    for i in range(1, len(meetings)): #ignore 0th element
        if curr[1] >= meetings[i][0]: #compare if less or equal to
            curr[1] = max(meetings[i][1], curr[1]) #use max for edge cases
        else:
            condensed_meetings.append(tuple(curr)) #wrap list in tuple
            curr = [meetings[i][0], meetings[i][1]] #resetting variable
        if i == (len(meetings) - 1): #check if at end of list
            condensed_meetings.append(tuple(curr))

    return condensed_meetings