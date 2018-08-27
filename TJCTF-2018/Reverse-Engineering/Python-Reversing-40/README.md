# Python Reversing

**Category: Reverse Engineering** **Points: 40** **Solves: 221**

**Description:**

> Found this flag checking file and it is quite vulnerable

[Source](https://static.tjctf.org/3e4bb82e4f30d27f9ba62d1c7885e448b5442448c5e00c58fd28de9cf17cd364_source.py)

## Solve

Files are in the repo if you want to take a closer look.

- `original.py` is the file provided

- `edited.py` is the file I tinkered with. Upon running will return the flag.

The first thing I notice is that there is a seed provided. This makes sure that all runs of the file will always have the same output.

I tried working this out with my head but it was hard to keep track.

Knowing that the flag always starts with `tjctf{`, we can get the same binary output as the `original_output` variable.

Here is the original file with comments I wrote:

```python
import numpy as np

flag = 'redacted'

np.random.seed(12345) # All methods dealing with numpy's random will always have the same outcome
arr = np.array([ord(c) for c in flag]) # Makes a list with the Unicode byte value for each character in flag
other = np.random.randint(1,5,(len(flag))) # This variable is always the same on every run, only difference is the length of the list
arr = np.multiply(arr,other) # Consistent with other and arr. ex. [1 2 3]

b = [x for x in arr] # This is arr but in the correct format of a list. ex. [1, 2, 3]
lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])] # This list is always the same
c = [b[i]^lmao[i] for i,j in enumerate(b)] # Basically xoring j with the item of lmao at the index of i
print(''.join(bin(x)[2:].zfill(8) for x in c))
# What this does is get the binary value of x and and join it with every other character in the list. It removes the first two characters because they are irrelevant '0b'.

# original_output was 1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101
```

The solution wasn't so much as reversing the binary output to the plain text. More like brute-forcing to the binary output.

This is because while testing, I found out that the output of `j` wasn't necessarily the same output as the `j` component of the ouput of `tjctf{` Also because the output lengths wern't always a factor of 8.

This shows that you can't really calculate the plain text. So, I wrote this to solve this problem:

```python
import numpy as np

flag = 'tjctf{'
charSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=_+[]{};\':",./<>?`~!@#$%^&*()'
testResult=''
result='1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101'

#original function
def flag_check(flag):
    # ...original file code
    return(''.join(bin(x)[2:].zfill(8) for x in c))


while testResult != result:
    for char in charSet:
        testResult = flag_check(flag + char)
        if testResult == result[:len(testResult)]:
            flag = flag+char
            break

print(flag)
```

I made a guess that the organizers wouldn't use Acrylic characters or Japanese, but instead guessed that the character set would be just the alphabet and all punctuation and all the numbers.

What my code essentially does is:

```
Check if the flag equals result
If not, brute force the flag_check() with charSet
If the flag + output from flag_check() is the same as result with the length modified to match flag_check()
Add the brute forced character to the current flag variable
Repeat this whole process until flag equals result and then print the flag
```

**Flag: tjctf{pYth0n_1s_tr1v14l}**
