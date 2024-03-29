These often show up as URL parameters like the ones in bold here:

https://example.com/login?redirect=https://example.com/dashboard

https://example.com/login?redir=https://example.com/dashboard

https://example.com/login?next=https://example.com/dashboard

https://example.com/login?next=/dashboard



Google dork techniques are an efficient way to find redirect parameters. To 
look for redirect parameters on a target site by using Google dorks, start by 
setting the site search term to your target site:

site:example.com

Then look for pages that contain URLs in their URL parameters, making use of %3D, the URL-encoded version of the equal sign (=). By adding %3D
in your search term, you can search for terms like =http and =https, which 
are indicators of URLs in a parameter. The following searches for URL 
parameters that contain absolute URLs:

inurl:%3Dhttp site:example.com

This search term might find the following pages:

https://example.com/login?next=https://example.com/dashboard

https://example.com/login?u=http://example.com/settings

Also try using %2F, the URL-encoded version of the slash (/). The following search term searches URLs that contain =/, and therefore returns 
URL parameters that contain relative URLs:

inurl:%3D%2F site:example.com

This search term will find URLs such as this one:

https://example.com/login?n=/dashboard

Alternatively, you can search for the names of common URL redirect 
parameters. Here are a few search terms that will likely reveal parameters 
used for a redirect:

inurl:redir site:example.com

inurl:redirect site:example.com

inurl:redirecturi site:example.com

inurl:redirect_uri site:example.com

inurl:redirecturl site:example.com

inurl:redirect_uri site:example.com

inurl:return site:example.com

inurl:returnurl site:example.com

inurl:relaystate site:example.com

inurl:forward site:example.com

inurl:forwardurl site:example.com

inurl:forward_url site:example.com

inurl:url site:example.com

inurl:uri site:example.com

inurl:dest site:example.com

inurl:destination site:example.com

inurl:next site:example.com

These search terms will find URLs such as the following:

https://example.com/logout?dest=/

https://example.com/login?RelayState=https://example.com/home


https://example.com/logout?forward=home

https://example.com/login?return=home/settings


Using Browser Autocorrect
First, you can use browser autocorrect features to construct alternative 
URLs that redirect offsite. Modern browsers often autocorrect URLs that 
don’t have the correct components, in order to correct mangled URLs 
caused by user typos. For example, Chrome will interpret all of these URLs 
as pointing to https://attacker.com:

https:attacker.com

https;attacker.com

https:\/\/attacker.com

https:/\/\attacker.com

These quirks can help you bypass URL validation based on a blocklist. 
For example, if the validator rejects any redirect URL that contains the 
strings https:// or http://, you can use an alternative string, like https;, to 
achieve the same results.
Open Redirects   137
Most modern browsers also automatically correct backslashes (\) to forward slashes (/), meaning they’ll treat these URLs as the same:

https:\\example.com

https://example.com

If the validator doesn’t recognize this behavior, the inconsistency could 
lead to bugs. For example, the following URL is potentially problematic:

https://attacker.com\@example.com


