#!/usr/bin/python3

def magic_calculation(a, b):
    
    from magic_calculation_102 import add, sub
    
    if a < b:
        somme = add(a, b)
        for i in range(4, 6):
            somme = add(somme, i)
            return (somme)
        else:
            return(sub(a, b))
