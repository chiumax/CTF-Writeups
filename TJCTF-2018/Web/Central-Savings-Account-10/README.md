# Central Savings Account

**Category: Web** **Points: 10** **Solves: 612**

**Description:**

> I seem to have forgotten the password for my [savings account](https://central_savings_account.tjctf.org/). What am I gonna do?

> The flag is not in standard flag format.

## Solve

Check out the source using dev tools.

Under the 'Sources' tab, we can find a javascript file called `main.js`

```javascript
$(document).ready(function() {
  $("#login-form").submit(function() {
    if (
      md5($("#password").val()).toLowerCase() ===
      "698967f805dea9ea073d188d73ab7390"
    ) {
      $("html").html("<h1>Login Succeeded!</h1>");
    } else {
      $("html").html("<h1>Login Failed!</h1>");
    }
  });
});
```

Located at the bottom of the file, we find an md5 hash.

I used [this](https://crackstation.net/) to break the hash.

**Flag: avalon**
or
**Flag: tjctf{avalon}**

_I forget which one it is_
