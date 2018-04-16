# Leaf of the Tree
**Points:** 20

**Description:**
>We found this annoyingly named directory tree starting at /problems/a45d1519bd193bc3a273744c83fad1e2. 
It would be pretty lame to type out all of those directory names but maybe there is something in there worth finding? 
And maybe we dont need to type out all those names...? Follow the trunk, using cat and ls!

**Hint:**
>Tab completion is a wonderful, wonderful thing

## Solve
Using the webshell, navigate to `/problems/a45d1519bd193bc3a273744c83fad1e2` using cd.

Using the command `ls -la` shows us a directory called `trunk`.

After entering the directory, we can see that there is also another variation of `trunk` directory but with a couple numbers trailing it. 
The hint tells us that tab completion is important here.

Tab completion is essentially pressing the tab key and terminal finishes your statement.

Without having to type out the whole trunk name, we can instead type the first character of the directory
and use tab completion. 

After reaching the last `trunk`, there is a flag file that can be opened using `cat`.

This gives us the flag~


**Flag: 1510e551a2821bd027da10a7653814c8**
