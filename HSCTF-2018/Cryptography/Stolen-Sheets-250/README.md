# Title
**Category:** Cryptography **Points:** 250 **Solves:** 238

**Description:**
>Keith finds a sheet of paper with the following items:
The flag will be the message "mrkcdpmsuimzstqrlg" decoded. 


![SheetofPaper](https://github.com/dumblole/CTF-Writeups/blob/master/HSCTF-2018/images/solen-sheetsproblem.PNG)





## Solve
Judging from the list, we can see that the cipher text has the same length as the plain text and that the letters used matched up with other letters in other texts in the list.

Let's write down what we have so far:
```
plain text = cipher text
a = ?
b = ?
c = ?
d = ?
e = c
f = t
g = k
h = b
i = s
j = ?
k = ?
l = ?
m = ?
n = z
o = q
p = ?
q = ?
r = p
s = g
t = x
u = o
v = f
w = w
x = h
y = ?
z = ?
```

Let's input what we got into a [substitution cipher decoder](https://quipqiup.com/).

![quipqiup.com](https://github.com/dumblole/CTF-Writeups/blob/master/HSCTF-2018/images/Stolen-Sheets.PNG)
**Flag:** `algebraicmanifolds`

## **References**
* https://quipqiup.com/
