#! /usr/bin/python3

from random import randint

# This program contains only one method, wich takes as argument a single string. This string must contain firstly 
# the program which primal or not-primal nature we won't to figure out and, secondly, the certainty we expect from
# the algorithm (which will keep working until this certainty is obtained).

# Fermat's little theorem states that for a given p and a numbers we can know p is primal when a**p-a is equal to some number 
# multiple of p. We can simplfy this into the following principle: if a**p%p=a, then p is primal. This program's algorithm is
# based on this translation of Fermat's theorem.
    
def fermats_little_theorem(input_values):

    n, c = input_values.split(" ")
    given_number, required_certainty = int(n), float (c)

    tested_ints = []
    
    count = 0
    while 1 - pow(2, -count) < required_certainty:
        a = randint(1, given_number - 1)
        print("certainty is " + str((1 - pow(2, -count))) + "\n")
        if pow(int(a), int(n),int(n)) != a:
            print(False)
            break
        elif a in tested_ints: 
            continue

        count += 1
        tested_ints.append(a)
    
    print(True)
    print("We can be " + str(1 - pow(2, -count)) + "% " + "certain that we are dealing with a prime number")
    
fermats_little_theorem(some_number, wanted_certainty)
    
#Example:
    
fermats_little_theorem("2367495770217142995264827948666809233066409497699870112003149352380375124855230064891220101264893169 0.999")
   
