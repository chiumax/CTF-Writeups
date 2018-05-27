# Blown Apart
**Category:** Cryptography **Points:** 350 **Solves:** 25

**Description:**
>Keith has discovered that Cueball is, yet again, sending everyone (except for Keith) some message, again encrypted using RSA. However, this time the number of people who received Cueball's message is more than 6!. Help Keith decrypt Cueball's message! Keith has been eavesdropping on Cueball's conversations, and has a complete log saved at file.txt.
Note: The flag to this problem is of the form flag{a_string_of_some_sort}. 

## Solve
This is an RSA problem. If you're not sure what RSA is, check [here](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

I remember reading about a [problem](https://www.youtube.com/watch?v=sYCzu04ftaY "Live Overflow") like this a while ago.

Anyways, the challenge gives us a huge list of `n` (modulus), `e` (pubkey), and `c` (ciphertext). Around 720 triplets. Take notice that the only thing in common is `m` (plaintext)

The `n`s they gave me are pretty large, so it'd take a pretty long time to find the prime factors `p` and `q`, even if the factors are less than or equal to n/2. If you want to read about how long it would take, check [here](https://crypto.stackexchange.com/questions/3043/how-much-computing-resource-is-required-to-brute-force-rsa?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

What we want is the plain text, and the only way to get that is by finding `d` (private key), but the only way we can find `d` is by finding `p` or `q`. 

They gave me 720 `n`s which could mean that a pair of them could have a common `p` factor. Let's try it out!

Doing some research, we find out that [Euclid's Algorithm]() is very efficient. Better than brute forcing at least. 

I wrote a program utilizing `gcd()` from the `fractions` module

```
'''
Given multiple modulus(n), we find p and q by finding the common divisor since
brute forcing to find p and q of n is inefficient and is not discovered. But, Euclid's gcd algorithms are super efficient
NOTE: Does not always work, but there was a good chance for finding a common divisor since there were so many
'''
# Python 3.6.0
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
```
This is our output:
```
Between person # :
68 
and the person #:
26 
the  gcd is: 
 22475281290880572740995360359318095277335621700349200715611491998104547011130635395372727125952267756271782502139857
n = 
 824472056452485900183440285141542770076945989369050255065689352740844666657459864516117424285631612949580396382766604617808407463222180655027644756839831149408035511904499638285468602977321104882998008453112733076256548968993554101
```
We can then find the second factor of `n` by dividing `n` by the `gcd`.

Now that we have `p`, `q`, `n`, `e`, `c`, we can find `d` using [this](http://www.mickybullock.com/blog/wp-content/RSA_Cryptography/dcalc.php) and decrypt using an online [RSA calculator](https://www.cs.drexel.edu/~introcs/Fa11/notes/10.1_Cryptography/RSAWorksheetv4d.html).
Or, you can just write a [script](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa) to do it for you.

The calculator gives me this:
```
102108097103123048049050054054098098055049050055048102052057057048048100057099052099101099102049055099057102053125057050053055056057049056054057057055052049
```
Since we know its in a `flag{}` format, let's try to convert to [ASCII](https://www.branah.com/ascii-converter)
**Flag:** `flag{01266bb71270f49900d9c4cecf17c9f5}`


## **References**

* http://www.mickybullock.com/blog/wp-content/RSA_Cryptography/dcalc.php
* https://www.cs.drexel.edu/~introcs/Fa11/notes/10.1_Cryptography/RSAWorksheetv4d.html
* https://www.youtube.com/watch?v=sYCzu04ftaY
* https://crypto.stackexchange.com/questions/3043/how-much-computing-resource-is-required-to-brute-force-rsa?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
* https://en.wikipedia.org/wiki/RSA_(cryptosystem)
* https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
* https://www.branah.com/ascii-converter


