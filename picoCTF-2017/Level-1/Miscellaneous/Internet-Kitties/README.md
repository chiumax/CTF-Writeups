# Internet Kitties
**Category:** Misc **Points:** 10

**Description:**
>I was told there was something at IP shell2017.picoctf.com with port 24369. How do I get there? Do I need a ship for the port?

**Hint:**
>Look at using the netcat (nc) command!
To figure out how to use it, you can run "man nc" or "nc -h" on the shell, or search for it on the interwebz

## Solve
Given the hostname and the port, we can connect using nc by pasting this into the webshell:

`nc shell2017.picoctf.com 24369`

This returns the flag!

```
Yay! You made it!                                            
Take a flag!                                                 
8eb2c54a37f4f6b7233b00c4800d0075   
```

**Flag: 8eb2c54a37f4f6b7233b00c4800d0075**
