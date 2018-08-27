# Programmable Hyperlinked Pasta

**Category: Web** **Points: 60** **Solves: 342**

**Description:**

> Check out my new site! PHP is so cool!

`programmable_hyperlinked_pasta.tjctf.org`

## Solve

This took me a while since it was my first time encountering such a problem.

Our first clue: **P**rogrammable **H**yperlinked **P**asta - **PHP** (Although that's not what php stands for...)

Spending some time looking through google about PHP, I found out something called a 'File Inclusion Vulnerability'.

According to [wikipedia](https://en.wikipedia.org/wiki/File_inclusion_vulnerability), PHP is susceptible to this type of vulerability.

We can put this into the url tab:
`https://programmable_hyperlinked_pasta.tjctf.org/?lang=../flag.txt`

This is essentially going back up a directory in the server (is it server?) and opening the file `flag.txt`

**Flag: tjctf{l0c4l_f1l3_wh4t?}**
