# Blank

**Category: Web** **Points: 5** **Solves: 979**

**Description:**

> Someone told me there was a flag on this [site](https://blank.tjctf.org/), so why is it that I can only see blank?

## Solve

Crack open dev tools. (f12 in chrome).

```
<body data-gr-c-s-loaded="true">
    <p>『　　』</p>
    <!-- flag: tjctf{50urc3_c0d3_n3v3r_l0535} -->

</body>
```

The flag is located in a html comment.

**Flag: tjctf{50urc3_c0d3_n3v3r_l0535}**
