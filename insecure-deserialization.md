In a PHP application, look for 
unserialize(), and in a Java application, look for readObject(). In Python and 
Ruby applications, look for the functions pickle.loads() and Marshall.load(), 
respectively.


Automating the Exploitation by Using Ysoserial
Ysoserial (https://github.com/frohoff/ysoserial/) is a tool that you can use to 
generate payloads that exploit Java insecure deserialization bugs, saving you 
tons of time by keeping you from having to develop gadget chains yourself.
Ysoserial uses a collection of gadget chains discovered in common Java 
libraries to formulate exploit objects. With Ysoserial, you can create malicious Java serialized objects that use gadget chains from specified libraries 
with a single command:

$ java -jar ysoserial.jar gadget_chain command_to_execute

For example, to create a payload that uses a gadget chain in the 
Commons-Collections library to open a calculator on the target host, 
execute this command:

$ java -jar ysoserial.jar CommonsCollections1 calc.exe

The gadget chains generated by Ysoserial all grant you the power to 
execute commands on the system. The program takes the command you 
specified and generates a serialized object that executes that command.

GitHub at https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet/.

# Prevention
Defending against deserialization vulnerabilities is difficult. The best way to 
protect an application against these vulnerabilities varies greatly based on 
the programming language, libraries, and serialization format used. No 
one-size-fits-all solution exists.
You should make sure not to deserialize any data tainted by user input 
without proper checks. If deserialization is necessary, use an allowlist to 
restrict deserialization to a small number of allowed classes.
You can also use simple data types, like strings and arrays, instead of 
objects that need to be serialized when being transported. And, to prevent the tampering of serialized cookies, you can keep track of the session 
state on the server instead of relying on user input for session information. 
Finally, you should keep an eye out for patches and make sure your dependencies are up-to-date to avoid introducing deserialization vulnerabilities 
via third-party code.

The OWASP Deserialization Cheat Sheet is an excellent resource for 
learning how to prevent deserialization flaws for your specific technology: 
https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html.
