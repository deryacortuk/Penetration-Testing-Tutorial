<img width="950" alt="WAF-Byypasss" src="https://github.com/deryacortuk/Penetration-Testing-Tutorial/assets/53267226/4221b862-ce1c-4135-825c-0adde3f04ce1">

# Case manipulation:
Some poorly developed WAFs selectively filter
payloads based on case sensitivity. By combining upper and lower case
characters, we can bypass these filters.

Example:

Standard payload: <script>alert()</script>
Bypassed payload: <ScRiPt>alert()</ScRiPt>
Similarly, the SQL query SELECT * FROM users WHERE username =
‘ummed’ can be bypassed as SeLecT * FRoM users WhErE username =
‘ummed’.

# HTML encoding:
Web applications often encode special characters into
their HTML representations. By using HTML encoding, we can bypass
certain WAF filters.

Example:

Standard payload: <script>alert(1)</script>
Encoded payload: &lt;script&gt;alert(1)&lt;/script&gt
Similarly, the SQL query SELECT * FROM users WHERE username =
‘admin’ can be encoded as SELECT * FROM users WHERE username =
‘adm&#105;n’.
