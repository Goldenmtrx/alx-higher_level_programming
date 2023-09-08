#!/usr/bin/python3

def magic_calculation(a, b):
    """match bytecode provided by H S"""
    from magic_calculation_102 import add, sub
    if a < b:
        s = add(a, b)
        for i in range(4, 6):
            s = add(s, i)
            return (s)
        
        else:
            return(sub(a, b))
