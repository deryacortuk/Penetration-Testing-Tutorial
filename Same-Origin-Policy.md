SAME - ORIGIN POLICY VULNERABILITIES private information leaks and often lead to more vulnerabilities, such as authentication bypass, account 
takeover, and large data breaches.

Two URLs are said to have the same origin if they share the same 
protocol, hostname, and port number. Modern web applications often base 
their authentication on HTTP cookies, and servers take action based on the 
cookies included automatically by the browser. When the SOP is implemented, malicious web pages won’t 
be able to take advantage of the cookies stored in your browser to access 
your private information.


CORS is a mechanism that protects 
the data of the server. It allows servers to explicitly specify a list of origins 
that are allowed to access its resources via the HTTP response header 
Access-Control-Allow-Origin. 

The application can also return the Access-Control-Allow-Origin header 
with a wildcard character (*) to indicate that the resource on that page can 
be accessed by any domain:  Access-Control-Allow-Origin: *

The most basic misconfiguration of CORS involves allowing the null
origin. If the server sets Access-Control-Allow-Origin to null, the browser will 
allow any site with a null origin header to access the resource. 

Access-Control-Allow-Origin: null

Access-Control-Allow-Origin: https://attacker.com

Access-Control-Allow-Origin: https://www.example.com.attacker.com

An interesting configuration that isn’t exploitable is setting the allowed 
origins to the wildcard (*). This isn’t exploitable because CORS doesn’t 
allow credentials, including cookies, authentication headers, or client-side 
certificates, to be sent with requests to these pages. Since credentials cannot 
be sent in requests to these pages, no private information can be accessed:
Access-Control-Allow-Origin: *

JSON with Padding (JSONP) is another technique that works around the SOP. 
It allows the sender to send JSON data as JavaScript code. A page of a different origin can read the JSON data by processing the JavaScript.
JSONP works around this issue by wrapping the data in a JavaScript 
function, and sending the data as JavaScript code instead of a JSON file.
The requesting page includes the resource as a script and specifies a 
callback function, typically in a URL parameter named callback or jsonp. 
This callback function is a predefined function on the receiving page ready 
to process the data:
<script src="https://a.example.com/user_info?callback=parseinfo"></script>

JSONP allows resources to be read across origins. 
Here’s a summary of what happens during a JSONP workflow:
1. The data requestor includes the data’s URL in a script tag, along with 
the name of a callback function.
2. The data provider returns the JSON data wrapped within the specified 
callback function.
3. The data requestor receives the function and processes the data by running the returned JavaScript code.

 JSONP is suitable for transmitting only public data. While 
JSONP can be hardened by using CSRF tokens or maintaining an allowlist of referer headers for JSONP requests, these protections can often be 
bypassed.  Now that CORS is a reliable option for cross-origin communication, 
sites no longer use JSONP as often.

CORS sites will often return HTTP 
responses that contain an Access-Control-Allow-Origin header. A site could be 
using postMessage() if you inspect a page (for example, by right-clicking it in 
Chrome and choosing Inspect, then navigating to Event Listeners) and find 
a message event listener.

And a site could be using JSONP if you see a URL being loaded in a 
<script> tag with a callback function:
<script src="https://a.example.com/user_info?callback=parseinfo"></script>
<script src="https://a.example.com/user_info?jsonp=parseinfo"></script>

<img width="750" alt="SOP" src="https://github.com/deryacortuk/Penetration-Testing-Tutorial/assets/53267226/d40609d2-15f9-44ae-8577-7449aa9abb0b">

When the target site does not rely on cookies for authentication, these SOP 
bypass misconfigurations might not be exploitable.

