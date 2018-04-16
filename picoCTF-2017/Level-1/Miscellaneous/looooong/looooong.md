# looooong
**Points:** 20

**Description:**
>I heard you have some "delusions of grandeur" about your typing speed. How fast can you go at shell2017.picoctf.com:1603?

**Hint:**
>Use the nc command to connect!

>I hear python is a good means (among many) to generate the needed input.

>It might help to have multiple windows open

## Solve
I might not have solved this the best way possible, but I still did it! :grin:

Connecting using nc multiple times, we can see a pattern (using x,y,z as placeholders):

```
To prove your skills, you must pass this test.                 
Please give me the 'x' character 'y' times, followed by a single 'z'.
```

I had the Python Shell open with the following code

```python
print('x'*y+'z')
```

Copied and pasted it to the terminal

```
You got it! You're super quick!                                
Flag: with_some_recognition_and_training_delusions_become_glimpses_c368f9f8d5b229152a2db1fbc95e5d09 
```

**Flag: with_some_recognition_and_training_delusions_become_glimpses_c368f9f8d5b229152a2db1fbc95e5d09**
