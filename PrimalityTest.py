#! /usr/bin/python3

from random import randint

# This program contains only one method, wich takes as argument a single string. This string must contain firstly 
# the number which primal or not-primal nature we want to figure out and, secondly, the certainty we expect from
# the algorithm (which will keep working until this certainty is obtained).

# Fermat's little theorem states that for a given p, if p is prime, then one minus a raised to the predecessor of p will be
# a multiple of p. This translates into: a**(p-1)-1 = x, where x is a multiple of p.
# An algorithm based on this formula states that, if a**p%p=a, then we can be confidently certain p is a primal number, except
# when dealing with the rare cae of a being a Charmicael number. This algorithm is used on the program.

def fermats_little_theorem(input_values):

    n, c = input_values.split(" ")
    given_number, required_certainty = int(n), float (c)

    tested_ints = []
    
    count = 0
    while 1 - pow(2, -count) < required_certainty:
        a = randint(2, given_number - 1)
        print("certainty is " + str((1 - pow(2, -count))) + "\n")
        if pow(int(a), given_number, given_number) != a:
            print(False)
            break
        elif a in tested_ints: 
            continue

        count += 1
        tested_ints.append(a)
    
    print(True)
    print("We can be " + str(1 - pow(2, -count)) + "% " + "certain that we are dealing with a prime number")
    
fermats_little_theorem("some_number required_certainty")
    
#Example:
    
fermats_little_theorem("2367495770217142995264827948666809233066409497699870112003149352380375124855230064891220101264893169 0.999")
   
