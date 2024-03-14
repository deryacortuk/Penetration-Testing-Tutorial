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
Example:

Standard payload: <script>alert(1)</script>
Obfuscated payload: <!-- <script> --> alert(1) <!-- </script> -->

# Payload fragmentation and concatenation:
Splitting payloads into
fragments or concatenating them in unexpected ways can bypass certain
WAF filters.
Example:

Standard payload: <script>alert(1)</script>

Fragmented payload: <<script>>a<</script>>lert(1)<</script>>
