# WorldChat
**Points:** 30

**Description:**
>We think someone is trying to transmit a flag over WorldChat. 
Unfortunately, there are so many other people talking that we can't really keep track of what is going on! 
Go see if you can find the messenger at shell2017.picoctf.com:48145. 
Remember to use Ctrl-C to cut the connection if it overwhelms you!

**Hint:**
>There are cool command line tools that can filter out lines with specific keywords in them. 
Check out 'grep'! You can use the '|' character to put all the output into another process or command (like the grep process)

## Solve
Connecting using `nc` connects us to a 'WorldChat' which presents us an onslaught of text from various users, making it 
difficult to read anything.

Let's back off for now (`Ctrl-C`)

The hint shows us that there's a helpful command called `grep`.

`nc shell2017.picoctf.com 48145 | grep flag` should work, but they've tricked us!

```
dumblole@shell-web:/$ nc shell2017.picoctf.com 48145 | grep fla
g
18:25:16 noihazflag: A huge moose is our best chance to drink y
our milkshake                                                  
18:25:17 whatisflag: Scary pandas need to meet up for what, I d
o not know                                                     
18:25:17 personwithflag: A dog with a cape totally understands 
me and my pet sloth to generate fusion power                   
18:25:17 flagperson: this is part 1/8 of the flag - 748a
18:25:18 flagperson: this is part 2/8 of the flag - 3a37
18:25:19 personwithflag: We need to meet up for the future of h
umanity                                                        
18:25:19 noihazflag: that guy from that movie will never unders
tand me to understand me                                       
18:25:19 personwithflag: Only us , in my well-educated opinion,
 are our best chance for the future of humanity                
18:25:19 personwithflag: Hungry jackolanterns want to see me to
 drink your milkshake 
 ```
 Reading this snippet, we can see that people also have `flag` in their username.
 
 So, we need to find something more specific.
 
 There's someone by the name of `flagperson` that is distributing parts of the flag.
 
 `nc shell2017.picoctf.com 48145 | grep flagperson`
 
 All parts of the flag:
 
 ```
 dumblole@shell-web:~$ nc shell2017.picoctf.com 48145 | grep flagperson                             
03:11:13 flagperson: this is part 1/8 of the flag - 748a
03:11:16 flagperson: this is part 2/8 of the flag - 3a37
03:11:21 flagperson: this is part 3/8 of the flag - ce62
03:11:24 flagperson: this is part 4/8 of the flag - e537
03:11:27 flagperson: this is part 5/8 of the flag - 4552
03:11:32 flagperson: this is part 6/8 of the flag - c31f
03:11:35 flagperson: this is part 7/8 of the flag - 5319
03:11:36 flagperson: this is part 8/8 of the flag - 30dc
```

**Flag: 748a3a37ce62e5374552c31f531930dc**
