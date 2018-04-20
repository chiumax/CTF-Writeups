# Hash101
**Category:** Cryptography **Points:** 50

**Description:**
>Prove your knowledge of hashes and claim a flag as your prize! Connect to the service at shell2017.picoctf.com:17428

**Hint:**
>	All concepts required to complete this challenge, including simple modular math, are quickly found by googling :)

## Solve
Connecting to the service greets us with this:
```
dumblole@shell-web:~$ nc shell2017.picoctf.com 17428           
                                                               
Welcome to Hashes 101!                                         
                                                               
There are 4 Levels. Complete all and receive a prize!          
                                                               
                                                               
-------- LEVEL 1: Text = just 1's and 0's --------             
All text can be represented by numbers. To see how different le
tters translate to numbers, go to http://www.asciitable.com/   
                                                               
TO UNLOCK NEXT LEVEL, give me the ASCII representation of 01101
1000110111101110110011001010110110001111001     
```
Let's translate it to ASCII using this [tool](https://gchq.github.io/CyberChef/)

The ASCII representation was `lovely`

Next level:
```
>lovely                                                        
Correct! Completed level 1                                     
                                                               
------ LEVEL 2: Numbers can be base ANYTHING -----             
Numbers can be represented many ways. A popular way to represen
t computer data is in base 16 or 'hex' since it lines up with b
ytes very well (2 hex characters = 8 binary bits). Other format
s include base64, binary, and just regular base10 (decimal)! In
 a way, that ascii chart represents a system where all text can
 be seen as "base128" (not including the Extended ASCII codes) 
                                                               
TO UNLOCK NEXT LEVEL, give me the text you just decoded, lovely
, as its hex equivalent, and then the decimal equivalent of tha
t hex number ("foo" -> 666f6f -> 6713199)                      
                                                               
hex>                                                           
```

**Flag:**

## **References**
