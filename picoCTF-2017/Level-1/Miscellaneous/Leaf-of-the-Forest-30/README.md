# Leaf of the Forest
**Category:** Misc **Points:** 30

**Description:**
>We found an even bigger directory tree hiding a flag starting at /problems/ba3662836dafb25fdcb412b505b7b677. 
It would be impossible to find the file named flag manually...

**Hint:**
>Is there a search function in Linux? Like if I wanted to 'find' something...

## Solve
The hint in this problem is very helpful.

After navigating to the problem directory, we can find another directory called `forest`.

Listing out the items in `forest` there are many `tree` directories followed by many `branch` directories
and so on.

Looking back at the hint, we can find that a `find` function does indeed exist!

So, inputting `find ./ -name flag` will return the current path of the flag file.

`./tree2763a4/trunk764d/trunke6d5/trunk7905/trunk0008/trunk95d7/trunkcbe5/trunk2319/branchc790/flag`

We can read the flag file with `cat`

**Flag: 395ba83a5a494eb04f43e15020577a75**

### Notes
Find more about the find function `man find`
