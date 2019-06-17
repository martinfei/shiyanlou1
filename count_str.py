#!usr/bin/env python3
def char_count(str_):
    countdict = {}
    for char in str_:
        countdict[char] = countdict.setdefault(char,0) + 1
    print(countdict)

if __name__ == '__main__':

    s = input('Enter a string:')

    char_count(s)
