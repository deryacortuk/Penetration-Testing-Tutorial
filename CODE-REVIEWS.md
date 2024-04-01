# The use of the eval() function in PHP can indicate a possible code injection vulnerability.
# PHP object injection guide at https://owasp.org/www-community/vulnerabilities/PHP_Object_Injection.


<img width="777" alt="Screenshot 2024-04-01 205127" src="https://github.com/deryacortuk/Penetration-Testing-Tutorial/assets/53267226/b2eb1f2f-32a3-4f12-9d7b-1e4011d42193">

You can look for these issues by grepping for keywords such as key, 
secret, password, encrypt, API, login, or token. You can also regex search for 
hex or base64 strings, depending on the key format of the credentials 
you’re looking for. For instance, GitHub access tokens are lowercase, 
40-character hex strings. A search pattern like [a-f0-9]{40} would find them 
in the source code. This search pattern matches strings that are 40 characters 
long and contains only digits and the hex letters a to f.

Entropy scanning can help you find secrets that don’t adhere to a specific format. In computing, entropy is a measurement of how random and 
unpredictable something is. For instance, a string composed of only one 
repeated character, like aaaaa, has very low entropy. A longer string with a 
larger set of characters, like wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY, has 
higher entropy. Entropy is therefore a good tool to find highly randomized 
and complex strings, which often indicate a secret. TruffleHog by Dylan
Ayrey (https://github.com/trufflesecurity/truffleHog/) is a tool that searches 
for secrets by using both regex and entropy scanning.


Look for issues such as weak encryption keys, breakable encryption algorithms, and weak hashing algorithms. Grep the names 
of weak algorithms like ECB, MD4, and MD5. The application might have 
functions named after these algorithms, such as ecb(), create_md4(), or md5_hash(). It might also have variables with the name of the algorithm, like 
ecb_key, and so on. The impact of weak hashing algorithms depends on 
where they are used.

Grep for specific code import functions in the language 
you are using with keywords like import, require, and dependencies. Then 
research the versions they’re using to see if any vulnerabilities are associated with them in the CVE database (https://cve.mitre.org/). The process 
of scanning an application for vulnerable dependencies is called software 
composition analysis (SCA). The OWASP Dependency-Check tool (https://
owasp.org/www-project-dependency-check/) can help you automate this process. 

http://dev.example.com/admin?debug=1&password=password


Configuration files allow you to gain more information about the target 
application and might contain credentials. You can look for filepaths to 
configuration files in source code as well. Configuration files often have the 
file extensions .conf, .env, .cnf, .cfg, .cf, .ini, .sys, or .plist.



