# Master Keys
**Category:** Cryptography **Points:** 200 **Solves:** 43

**Description:**
>During their late-night discourse, Keith finds a number d1 that functions as a private key to Alice's public key (N,e). Surprisingly, Alice tells Keith a different number d2 that she used for the private key. Given the information below, the flag will be the sum (in decimal) of the primes that divide N, taken modulo 1000000007.
N is the product of two primes. 


## Solve
I suggest reading up on [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) before reading this.
And reading up on the properties of [Modular Arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic).

This problem was pretty difficult in my opinion.

Let's take a look at what they gave me:
* They give us 2 `d` (private keys)
* They also give us `n` (modulus)
* The private keys work with the same `n`, `e` (public key) pair.
* What they give us is in base 16


This is an RSA problem but we aren't trying to decrypt text, instead, we're trying to find the sum of `p` and `q`. When converted to base 10, `n` is over 600 digits long. It would literally take [forever to brute-force](https://crypto.stackexchange.com/questions/3043/how-much-computing-resource-is-required-to-brute-force-rsa?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa).

So, there must be another way other than factoring `n`.

I found this [paper](http://people.csail.mit.edu/rivest/Rsapaper.pdf) while researching about RSA.

Page 12 tells us (under the "Computing phi `n` without factoring `n`") that:
* phi `n` = `n`+1-(`p`+`q`)
* phi `n` = a multiple of (`p`-1)(`q`-1)

Looking back at the problem, we know that both `d` (private keys) work with the same `n` and `e`.

So we can write an equation that looks like this:
```
d1*e mod phi(n) = d2*e mod phi(n) 
```
We know that `x mod y` finds the remainder of `x/y`.
This is an example:
```
24 mod 12 = 0
48 mod 12 = 0
```
The difference between 24 and 36 is a factor of 12.
```
48 mod 12 = 24 mod 12 
```
Since the difference is by a factor of 12, we can:
```
48 = 24 + 12 * k (k is an integer)
```
This will always work because it is a property of mod.
```
(48 - 24)/12 = k
```

Let's look back on our equation:
```
d1*e = d2*e + phi(n) *k (k is an integer)
d1*e - d2*3 = phi(n) *k
d1 - d2 = phi(n)*k / e
```
Remember what I said about `n`? It's 600 digits long.

phi `n` = (`p`-1)(`q`-1)

`n` = `pq`

What difference is `-1` going to make when it's 600 digits long. Barely any difference. In relative terms.

Let's try substituting phi `n` with `n`:
```
(d1 - d2) / n = k / e
```
As I have already said, these numbers are pretty huge so I'm not pasting the [actual #s here](https://github.com/dumblole/CTF-Writeups/blob/master/HSCTF-2018/Cryptography/Master-Keys-200/master-keys-file.txt).
```
(abs(d1-d2))/n = 1.0000000000000...1
k / e = 1
d1-d2 = n
d1-d2 = n+1-(p+q)
d1-d2-n-1 = -(p+q)
```
After doing all the math, we get `p+q`, mod 1000000007.

This problem was kind of a stretch, but at least we got it.

**Flag:** `917560622`

## **References**
* http://people.csail.mit.edu/rivest/Rsapaper.pdf
* https://crypto.stackexchange.com/questions/3043/how-much-computing-resource-is-required-to-brute-force-rsa?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
* https://en.wikipedia.org/wiki/RSA_(cryptosystem)

