# OK
**Category:** Algorithm **Points:** 250 **Solves:**

**Description:**
>After ranting at length to a friend, Keith receives a message consisting of a single letter: "K". Incensed at this low-effort response, he responds with "OK", to which his friend replies "KOOK." An astute individual, Keith identifies the pattern instigated by his friend: subsequent messages consist of Keith and his friend replacing each "K" with "OK" and "O" with "KO". Help Keith find how many sets of consecutive Os of length two or greater are in the message on the 1000 reply. The first message, "K", does not count as a reply. Give your answer mod 10^9 + 7.
To clarify what constitutes "sets of consecutive Os of length two or greater": 
KOKOOKOOOKOOOO - there are three sets of consecutive Ks of length two or greater in this string ("OO", "OOO", "OOOO"). 

## Solve
The script I wrote for this problem was written in Python 3.6.0. It utilized the sys module to increase the recursion limit.

Reading the description over tells us that the first text "K" does not count as a reply. It also tells us that every "K" is replaced with "OK" and every "O" is replaced with "KO".

The script I wrote is poorly optimized in my opinion but at least it worked!

I decided to write a procedure that would help me visualize the first couple iterations / replies by following the rules above, here is the procedure that I wrote:

```
def ok(top):
    '''
Initial procedure. I used this to visualize the first couple replies / iterations of the messages.
'''
    iteration = 0 # counts how many replies have been made
    count = 0 # counts how many sets of consecutive O's whose length is at least 2
    temp_count = 0 # counts how many O's there are before reaching a K while iterating through a string
    string = 'K' # Since the first iteration doesn't count, I'm setting the string at K. And also because I need something in the string for it to work.
    string_temp = '' # Temporarily stores the edited string after one iteration / reply.
    #I did this because it is very complicated to loop through a list or string and edit it at the same time during the loop

    while iteration != top:
        for letter in string: # one iteration / reply
            if letter =='K':
                string_temp+= 'OK'
            else:
                string_temp +='KO'
                
        iteration +=1
        string = string_temp
        string_temp = ''

    for x in string: #counts how many sets of consecutive O's whose length is at least 2
        if x == 'O':
            temp_count +=1
        else:
            if temp_count >= 2:
                count +=1
            temp_count = 0
    return(string,count)
```

I did the first seven replies by hand and by using this function and got the same result:
```
(reply, # of consecutive O's length >= 2)
('OK', 0)
('KOOK', 1)
('OKKOKOOK', 1)
('KOOKOKKOOKKOKOOK', 3)
('OKKOKOOKKOOKOKKOKOOKOKKOOKKOKOOK', 5)
('KOOKOKKOOKKOKOOKOKKOKOOKKOOKOKKOOKKOKOOKKOOKOKKOKOOKOKKOOKKOKOOK', 11)
('OKKOKOOKKOOKOKKOKOOKOKKOOKKOKOOKKOOKOKKOOKKOKOOKOKKOKOOKKOOKOKKOKOOKOKKOOKKOKOOKOKKOKOOKKOOKOKKOOKKOKOOKKOOKOKKOKOOKOKKOOKKOKOOK', 21)
```

I tried to run the procedure I wrote with the 1000th iteration. Unfortunately, after around 3 minutes of hearing my pc fans spin, I stopped the program.

With any pattern, there is always another mathematical pattern that follows it.
The pattern I have so far:
```
{0, 1, 1, 3, 5, 11, 21}
```
I tried using online pattern finders but to no avail. I decided to find the difference between each of the terms of the list (excluding the first two terms):
```
{0, 2, 2, 6, 10}
```
It tooke me a while, but I found that the difference between each of the terms was: `(n-2)*2 + (n-1) = n`

I wrote a recursive function that followed that rule:
```
def ok_recursive(before,num,itera):
    itera -= 1
    if itera > 0:
        return ok_recursive(num,(before*2)+num,itera)
    return num
print(ok_recursive(0,1,999))
#This is because the ok() procedure starts iteration from 1 and the ok_recursive() starts from 0 (it counts the first message as a reply / iteration)
```

Running the function gave us the answer within a second.
```
1785847678643778868247375081766669684269008019509222679072917313950585085208226870821997298026159763545991121529255244708645242142820523405997429595783095800655761295804038497570179100843728523646325697025507745830596990211233127926527590657679510485761866079614423694610071638608770731139534278011563
```
The challenge wants us to mod the answer by 10^9+7
**Flag: ** `114737202`

## **References**
* http://www.calcul.com/show/calculator/recursive