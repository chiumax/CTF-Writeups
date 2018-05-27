'''
Given multiple modulus(n), we find p and q by finding the common divisor since
brute forcing to find p and q of n is inefficient and is not discovered. But, Euclid's gcd algorithms are super efficient
NOTE: Does not always work, but there was a good chance for finding a common divisor since there were so many
'''
#Python 3.6.0

from fractions import gcd

rsa_modulus = {}
counter = 0

with open('Blown-Apart.txt','r') as file:
    for line in file:
        if line[0] == 'n':
            words = line.split()
            rsa_modulus.update({counter: int(words[-1])}) # Iterates through the list and compiles a dictionary of all the n (modulus)
            counter+=1

'''
It's a dictionary because we can differentiate between people
'''

for person_a in rsa_modulus: # Iterates and compares every person with every other person
    for person_b in rsa_modulus:
        if person_a != person_b: # Make sure that the gcd isn't compared with itself
            common = gcd(rsa_modulus[person_a], rsa_modulus[person_b])
            if common != 1: # Filter out cases that have gcd of 1
                print(f'Between person # :\n{person_a} \nand the person #:\n{person_b} \nthe  gcd is: \n {common}')
                print(f'n = \n', rsa_modulus[person_a])


                
