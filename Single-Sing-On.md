Single sign-on (SSO) is a feature that allows 
users to access multiple services belonging 
to the same organization without logging 
in multiple times.

Cookie sharing, SAML, and OAuth are the three most common ways of 
implementing SSO.

# Cooking Sharing
The implementation of SSO is quite easy if the services that need to share 
authentication are located under the same parent domain, as is the case with 
the web and mobile versions.

Modern browsers allow sites to share their cookies across subdomains if the 
cookie’s Domain flag is set to a common parent domain. For example, if the 
server sets a cookie like the following, the cookie will be sent to all subdomains of facebook.com:
Set-Cookie: cookie=abc123; Domain=facebook.com; Secure; HttpOnly

However, not all applications can use this approach, because cookies 
can’t be shared this way across different domains. For instance, facebook.com
and messenger.com can’t share cookies, because they don’t share a common 
parent domain.
Moreover, this simple SSO setup comes with unique vulnerabilities. First, 
because the session cookie is shared across all subdomains, attackers can take 
over the accounts of all websites under the same parent domain by stealing a 
single cookie from the user. Usually, attackers can steal the session cookies by 
finding a vulnerability like cross-site scripting.

# Subdomain Takeovers
Put simply, subdomain takeovers occur when an attacker takes control over a 
company’s unused subdomain.
Let’s say a company hosts its subdomain on a third-party service, such 
as AWS or GitHub Pages. The company can use a DNS CNAME record 
to point the subdomain to another URL on the third-party site. This way, 
whenever users request the official subdomain, they’ll be redirected to the 
third-party web page.
