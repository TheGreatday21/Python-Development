#2

import char

def count_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


str = input("Enter string:")
count_character(str)
'''
char_count = count_character(string)


char_count()
'''