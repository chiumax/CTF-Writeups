# Go Git It
**Points:** 25

**Description:**
>The code samurai (also known by his pseudonym Nicholas) was making some final optimizations on his program when… he accidentally decapitated it.

>Download the samurai’s repository: [go git it.tar.bz2](https://github.com/dumblole/CTF-Writeups/blob/master/PACTF-2018/Go-Git-It-25/go_git_it.tar.427f1b62f4aa.bz2)

**Hint:**
>Perhaps ‘chopping a branch off a tree’ would be the more precise analogy.


## Solve
Git challenge. Assuming we have to recover a branch.

Extract the folder. It gives us a file that ends with `.tar.123456`

Delete it to get a `tar` file. Extract the `tar` file.

Using `git reflog`, we can recover the flag in `README.md`

![Go-Git-It](https://github.com/dumblole/CTF-Writeups/blob/master/PACTF-2018/images/gogitit.PNG)

`The flag is `3x3rc1z3_caut10n_wh3n_d3tach1ng_ur_h3ad`!`

**Flag:** `3x3rc1z3_caut10n_wh3n_d3tach1ng_ur_h3ad`

