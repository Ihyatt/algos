def reverse_words(message):
    message.reverse() #reverse in place
    def rev_word(start, end):
        while start < end:
            message[start], message[end] = message[end], message[start]
            start += 1
            end -= 1

    start = 0
    for i in range(len(message) + 1): # +1 can be used to avoid extra conditionals
        if (i == len(message)) or (message[i] ==" "):
            rev_word(start, i - 1)
            start = i + 1
            

    return message