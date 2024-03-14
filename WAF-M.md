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


<img width="900" alt="10" src="https://github.com/deryacortuk/Penetration-Testing-Tutorial/assets/53267226/6b6d16cf-28af-4ec7-a152-385ddaacd597">

# Mixed encodings:
By using a combination of different encodings, we can
bypass filters that target specific encoding types. Combining URL encoding
with HTML encoding can yield effective bypasses.

<img width="700" alt="11" src="https://github.com/deryacortuk/Penetration-Testing-Tutorial/assets/53267226/ee8814f8-663a-4b05-8b18-296887eb909a">

# Comments and whitespace Tricks
Including comments and whitespace in payloads can help obfuscate them
and bypass filters.


# Payload fragmentation and concatenation:
Splitting payloads into
fragments or concatenating them in unexpected ways can bypass certain
WAF filters.

<img width="570" alt="12" src="https://github.com/deryacortuk/Penetration-Testing-Tutorial/assets/53267226/33e4f2ee-e707-45a9-a81c-263dd5ac514b">

<img width="900" alt="13" src="https://github.com/deryacortuk/Penetration-Testing-Tutorial/assets/53267226/48b4d844-cf41-4b8e-92ac-f08f06ef49de">


<img width="800" alt="14" src="https://github.com/deryacortuk/Penetration-Testing-Tutorial/assets/53267226/b1ed4853-1802-4311-a5aa-bbfc8a877e79">


