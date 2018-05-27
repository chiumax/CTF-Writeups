# Very Small Primes
**Category:** Cryptography **Points:** 200 **Solves:** 62

**Description:**
>During their algebraic geometry class, Pawel and Keith had a conversation. A short transcript of the conversation is given below:

>Keith: "Pawel, I want to send you a message."

>Pawel: "Ok".

>To receive Keith's message, Pawel asks his cousins Simone and Simtwo to give him two primes p, q. Pawel then writes his public key (N, e) on the blackboard in the front of the class (where N = pq). Keith then promptly writes the number C on the blackboard. Pawel gives a thumbs up, signifying that he received the message. 

>Craig saw the first exchange between Keith and Pawel and he wants to know what Keith's message is. Luckily, Craig knows that Simone can only give numbers with at most 6 digits (when written in base 10) and he was able to find the message.

>N = 0x10722aa034ca559f3e30fdd3a5fbdbb6f2eede584f4aedc764f0bf8a72bc7853ccc874e975563fa80348cbd3355e36903e5cbbc4ce7ba91ca29989b8a09fe3212931e4421a3460501c91aa2b47729eb114c22f15d87d11deddd102f576704dd8ae8aca12afad9e0fbf909f7be534ff73fc17d2ef11ac76b2eaa9a62b7ffc0bd 

>e = 65537

>C = 0x502c9f367b231c49a36ed5353f9afdcc4ed7c262f593995085ab44e017c3ebb912fa94b7b06213bb9cb9ea052bdb70af922b54617a035c82be819e7f4209e5718901688be800669247a449ea8bd6f8328090396117ae6b3a292eb4f1de1806f81442d7641d35c68bd32d44f21fe36a1128bbc84258904619f749e2692b8bca

>Find the flag.

>Note: The flag is an ascii string. 


## Solve
I suggest reading up on [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) before reading this.

Let's take a look at what they give me:
* This is an RSA problem
* Flag is an ASCII string
* `e` (public key) is 65537
* `n` (modulus) is in base 16
* `c` (cipher-text) is also in base 16
* `p` (modulus component) can be at most 999,999 (Simone)

Now all we need now is  `q` (modulus component) so we can find `d` (private key) and finally decrypt `c` (cipher-text).

Since we know that one of the factors of `n` is less than 1,000,000 (one million) it would be very easy to brute-force.

I wrote a program in Python 3.6.0 to brute force every odd number (primes are odd numbers) between 0 and 1,000,000.
```
def factor(n):
    divisor = 3
    while True:
        if n%divisor == 0:
            print(divisor)
            print(n/divisor)
            break
        else:
            divisor+=2
```
Convert `n` to base 10, run `factor(n)` and we get:
```
999773
```
As `p`. Now we can get `q` by dividing `n` by `p`:
```
721960629061904110756973047896820529650646626913987914193058081946869300323505631503613785147235083747598529092067962512605338801581684234964490805070294572618497933653948906694134011361476095650659862416376029070102910970128990995504864728056436234936733309062195718092793663000312918831684212336353
```
With `p` and `q`, we can finally get `d` by using the modular multiplicative inverse of `e` and phi `n`. Look [here](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa) for a python script to do it for you.
```
417502229327473395118183058782860785031894183173528193352646066020816648283807501290900872443499537030097388296577580318266256237614908894887326208179024440867659615918784406775804521747584148242291821653009461433650968947520715054172886761267711972507875832818986088871590840703106680356234078804931373569
```
Now we can break c, which gives up
```
1021089710312367114971051034583109101108108115456697100125
```
Flag is in ASCII, so let's convert it from decimal to ASCII.

**Flag:** `flag{Craig-Smells-Bad}`

## **References**
* https://en.wikipedia.org/wiki/RSA_(cryptosystem)
* https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
