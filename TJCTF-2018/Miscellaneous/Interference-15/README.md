# Interference

**Category: Miscellaneous** **Points: 15** **Solves: 270**

**Description:**

> I was looking at some images but I couldn't see them clearly. I think there's some [interference](https://static.tjctf.org/01a68dd1c1db3bb4eb69853b32cb4dbbc22c6c05abf994733e99b928c20c5295_interference.zip).

## Solve

I don't think I was supposed to do this problem the way I did...

note: files are located in the repo

They provide 2 images of what looks like static for us. They both look similar.

I decided to play around with the bits of each image [here](https://incoherency.co.uk/image-steganography/).

The second image showed something promising:

I could barely make out the QR code that is embedded in it; let alone scan it.

![fuzzy qr code img](https://github.com/dumblole/CTF-Writeups/blob/master/TJCTF-2018/images/download.png)

Since the background is only consisted of two colors, I thought it wouldn't be too difficult to just write a python script that sharpened the image for us (script located in repo):

![clear qr code img](https://github.com/dumblole/CTF-Writeups/blob/master/TJCTF-2018/images/edit.png)

Scan the QR code.

**Flag: tjctf{m1x1ing_and_m4tchIng_1m4g3s_15_fun}**

_I think I was supposed to do something with the images TOGETHER_
