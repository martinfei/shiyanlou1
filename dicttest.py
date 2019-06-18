#!usr/bin/env python3
def handle_data(arg):
    (key,value) = arg.split(':')
    output_dict[key] = value
    

def print_data(key,value):
    print('ID:{} Name:{}'.format(key,value))

output_dict  = {}
import sys

if __name__  == '__main__':
   
    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key,output_dict[key])
