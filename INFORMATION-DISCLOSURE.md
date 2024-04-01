https://example.com/image?url=/images/../../../../../../../etc/shadow

if the application implements some sort of input validation and doesn’t allow ../ in the filepath, 
you can use encoded variations of ../, such as %2e%2e%2f (URL encoding), 
%252e%252e%255f (double URL encoding), and ..%2f (partial URL encoding).



On the Wayback Machine’s site, simply search for a domain to see its 
past versions. To search for a domain’s files, visit https://web.archive.org/web/*/
DOMAIN.

Add a /* to this URL to get the archived URLs related to the domain as 
a list. For example, https://web.archive.org/web/*/example.com/* will return a list 
of URLs related to example.com.


You can also search for backup files and configuration files by using 
common file extensions like .conf  and .env, or look for source 
code, like JavaScript or PHP files, by using the file extensions .js and .php.


 # truffleHog (https://github.com/dxa4481/truffleHog/) or Gitleaks (https://github.com/zricethezav/gitleaks/).
  # JavaScript files on a site by using tools like LinkFinder (https://github.com/GerbenJavado/LinkFinder/).


If directory listing is enabled, you can browse through the files and retrieve 
the leaked information. The wget command retrieves content from web 
servers. You can use wget in recursive mode (-r) to mass-download all files 
stored within the specified directory and its subdirectories: $ wget -r example.com/.git



