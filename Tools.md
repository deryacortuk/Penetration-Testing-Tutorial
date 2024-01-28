# Burp Suite

https://portswigger.net/burp
Burp Suite is an integrated platform for security testing and pretty much a must when
you are starting out. It has a variety of tools which are helpful, including:
• An intercepting proxy which lets you inspect and modify traffic to a site
• An application aware Spider for crawling content and functionality (either passively
or actively)
• A web scanner for automating the detection of vulnerabilities
• A repeater for manipulating and resending individual requests
• A sequencer tool for testing the randomness of tokens
• A comparer tool to compare requests and responses
Bucky Roberts, from the New Boston, has a tutorial series on Burp Suite available at
https://vimeo.com/album/3510171 which provides an introduction to Burp Suite.


# ZAP Proxy

https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project
The OWASP Zed Attack Proxy (ZAP) is a free, community based, open source platform
similar to Burp for security testing. It also has a variety of tools, including a Proxy,
Repeater, Scanner, Directory/File Bruteforcer, etc. It also supports add-ons so if you’re
a developer, you can create additional functionality. Their website has a lot of useful
information to help you get started.

# Knockpy

https://github.com/guelfoweb/knock
Knockpy is a python tool designed to iterate over a huge word list to identify sub
domains of a company. Identifying sub domains helps to increase the testable surface
of a company and increase the chances of finding a successful vulnerability.
This is a GitHub repository which means you’ll need to download the repo (the GitHub
page has instructions as to how) and need Python installed (they have tested with version
2.7.6 and recommend you use Google DNS (8.8.8.8 | 8.8.4.4).

# HostileSubBruteforcer

https://github.com/nahamsec/HostileSubBruteforcer
This app, written by @nahamsec (Ben Sadeghipour - great guy!), will bruteforce for
existing sub domains and provide the IP address, Host and whether it has been properly
setup, checking AWS, Github, Heroku, Shopify, Tumblr and Squarespace. This is great for
finding sub domain takeovers.

# Sublist3r

https://github.com/aboul3la/Sublist3r
According to it’s README.md, Sublist3r is python tool that is designed to enumerate sub
domains of websites using search engines. It helps penetration testers and bug hunters
collect and gather sub domains for the domain they are targeting. Sublist3r currently
supports the following search engines: Google, Yahoo, Bing, Baidu, and Ask. More search
engines may be added in the future. Sublist3r also gathers sub domains using Netcraft,
Virustotal, ThreatCrowd, DNSdumpster and PassiveDNS.
The tool, subbrute, was integrated with Sublist3r to increase the possibility of finding
more sub domains using bruteforce with an improved wordlist. The credit goes to
TheRook who is the author of subbrute.

# crt.sh

https://crt.sh
A search site for browsing Certificate Transaction logs, revealing sub domains associated
with certificates.

# IPV4info.com

http://ipv4info.com
This is a great site that I just learned about thanks to Philippe Harewood (again!). Using
this site, you can find domains hosted on a given server. So, for example, entering
yahoo.com will give you Yahoo’s IPs range and all the domains served from the same
servers.

# SecLists

https://github.com/danielmiessler/SecLists
While technically not a tool in and of itself, SecLists is a collection of multiple types of
lists used during hacking. This includes usernames, passwords, URLs, fuzzing strings,
common directories/files/sub domains, etc. The project is maintained by Daniel Miessler
and Jason Haddix (Hacking ProTips #5 guest)

# XSSHunter

https://xsshunter.com
XSSHunter is a tool developed by Matt Bryant1 (formerly of the Uber security team)
which helps you find blind XSS vulnerabilities, or XSS that you don’t see fire for whatever
reason. After signing up for XSSHunter, you get a special xss.ht short domain which
identifies your XSS and hosts your payload. When the XSS fires, it will automatically
collects information about where it occurred and will send you an email notification.

# sqlmap

http://sqlmap.org
sqlmap is an open source penetration tool that automates the process of detecting and
exploiting SQL injection vulnerabilities. The website has a huge list of features, including
support for:
• A wide range of database types (e.g., MySQL, Oracle, PostgreSQL, MS SQL Server, etc.)
• Six SQL injection techniques (e.g., boolean-based blind, time-based blind, errorbased, UNION query-based, etc)
• Enumerating users, password hashes, privileges, roles, databases, tables and columns
• And much more 

According to Michiel Prins, sqlmap is helpful for automating the exploitation of SQL
injection vulnerabilities to prove something is vulnerable, saving a lot of manual work.
Similar to Knockpy, sqlmap relies on Python and can be run on Windows or Unix based
systems.

# Nmap

https://nmap.org
Nmap is a free and open source utility for network discover and security auditing.
According to their site, Nmap uses raw IP packets in novel ways to determine: - Which
hosts are available on a network - What services (application name and version) those
hosts are offering - What operating systems (and versions) they are running - What type
of packet filters/firewalls are in use - And much more 
The Nmap site has a robust list of installation instructions supporting Windows, Mac and
Linux.

# Eyewitness

https://github.com/ChrisTruncer/EyeWitness
EyeWitness is designed to take screenshots of websites, provide some server header info
and identify default credentials if possible. It’s a great tool for detecting what services
are running on common HTTP and HTTPS ports and can be used with other tools like
Nmap to quickly enumerate hacking targets.

# Gowitness

https://github.com/sensepost/gowitness
gowitness is a website screenshot utility written in Golang, that uses Chrome Headless to
generate screenshots of web interfaces using the command line. Both Linux and macOS
is supported, with Windows support ‘partially working’.

# Gobuster

https://github.com/oj/gobuster
Gobuster is a tool used to brute-force URIs (directories and files) in web sites and DNS
subdomains (with wildcard support).

# Meg

https://github.com/tomnomnom/meg
meg is a tool for fetching lots of URLs but still being ‘nice’ to servers. It can be used to
fetch many paths for many hosts; fetching one path for all hosts before moving on to the
next path and repeating. You get lots of results quickly, but non of the individual hosts
get flooded with traffic.

# Shodan

https://www.shodan.io
Shodan is the internet search engine of “Things”. According to the site, you can, “Use
Shodan to discover which of your devices are connected to the internet, where they are
located and who is using them”. This is particularly helpful when you are exploring a
potential target and trying to learn as much about the targets infrastructure as possible.
Combined with this is a handy Firefox plugin for Shodan which allows you to quickly
access information for a particular domain. Sometimes this reveals available ports which
you can pass to Nmap.

# Censys

https://censys.io
Censys is a search engine that enables researchers to ask questions about the hosts and
networks that compose the Internet. Censys collects data on hosts and websites through
daily ZMap and ZGrab scans of the IPV4 address space, in turn maintaining a database
of how hosts and websites are configured.

# What CMS

http://www.whatcms.org
What CMS is a simple application which allows you to enter a site url and it’ll return the
likely Content Management System the site is using. This is helpful for a couple reason:
• Knowing what CMS a site is using gives you insight into how the site code is
structured
• If the CMS is open source, you can browse the code for vulnerabilities and test them
on the site
• If you can determine the version code of the CMS, it’s possible the site may be
outdated and vulnerable to disclosed security vulnerabilities

# BuiltWith

http://builtwith.com
BuiltWith is an interesting tool that will help you fingerprint different technologies used
on a particular target. According to its site, it covers over 18,000 types of internet
technologies, including analytics, hosting, which CMS, etc.

# Nikto

https://cirt.net/nikto2
Nikto is an Open Source web server scanner which tests against servers for multiple
items, including:
Potentially dangerous files/programs
• Outdated versions of servers
• Version specific problems
• Checking for server configuration items
According to Michiel, Nikto is helpful for finding files or directories that should not be
available (e.g., an old SQL backup file, or the inside of a git repo)

# Recon-ng

https://bitbucket.org/LaNMaSteR53/recon-ng
According to its page, Recon-ng is a full featured Web Reconnaissance framework
written in Python. It provides a powerful environment in which open source web-based
reconnaissance can be conducted quickly and thoroughly.
Unfortunately, or fortunately depending on how you want to look at it, Recon-ng provides
so much functionality that I can’t adequately describe it here. It can be used for sub
domain discovery, sensitive file discovery, username enumeration, scraping social media
sites, etc.

# GitRob

https://github.com/michenriksen/gitrob
Gitrob is a command line tool which can help organizations and security professionals
find sensitive information lingering in publicly available files on GitHub. The tool will iterate over all public organization and member repositories and match filenames against
a range of patterns for files that typically contain sensitive or dangerous information.

# CyberChef

https://gchq.github.io/CyberChef/
CyberChef is a swiss army knife providing all kinds of encoding/decoding tools. It also
provides functionality to save a list of favorites, download results, among many other
things.

# OnlineHashCrack.com

www.onlinehashcrack.com
Online Hash Crack is an online service that attempts to recover your passwords (hashes
like MD5, NTLM, Wordpress, etc), your WPA dumps (handshakes) and your MS Office
encrypted files (obtained legally). It is useful to help identify what type of hash is used if
you don’t know, supporting the identification of over 250 hash types.

# idb

http://www.idbtool.com
idb is a tool to help simplify some common tasks for iOS app security assessments and
research. It’s hosted on GitHub.

# Wireshark

https://www.wireshark.org
Wireshark is a network protocol analyzer which lets you see what is happening on your
network in fine detail. This is more useful when a site isn’t just communicating over
HTTP/HTTPS. If you are starting out, it may be more beneficial to stick with Burp Suite if
the site is just communicating over HTTP/HTTPS.

# Bucket Finder

https://digi.ninja/files/bucket_finder_1.1.tar.bz2
A cool tool that will search for readable buckets and list all the files in them. It can
also be used to quickly find buckets that exist but deny access to listing files - on these
buckets, you can test out writing using the AWS CLI and described in Example 6 of the
Authentication Chapter - How I hacked HackerOne S3 Buckets.

# Race the Web

https://github.com/insp3ctre/race-the-web
A newer tool which tests for race conditions in web applications by sending out a userspecified number of requests to a target URL (or URLs) simultaneously, and then compares the responses from the server for uniqueness. Includes a number of configuration
options.

# Google Dorks

https://www.exploit-db.com/google-hacking-database
Google Dorking refers to using advance syntaxes provided by Google to find information
not readily available. This can include finding vulnerable files, opportunities for external
resource loading, etc.

# JD GUI

https://github.com/java-decompiler/jd-gui
JD-GUI is a tool which can help when exploring Android apps. It’s a standalone graphical
utility that displays Java sources from CLASS files. While I don’t have much experience
with this tool (yet), it seems promising and useful.

# Mobile Security Framework

https://github.com/ajinabraham/Mobile-Security-Framework-MobSF
This is another tool useful for mobile hacking. It’s an intelligent, all-in-one open source
mobile application (Android/iOS) automated pen-testing framework capable of performing static, dynamic analysis and web API testing.

# Ysoserial

https://github.com/frohoff/ysoserial
A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization 

# Firefox Plugins

This list is largely thanks to the post from the Infosecinstitute available here: InfosecInstitute2

# FoxyProxy

FoxyProxy is an advanced proxy management add-on for Firefox browser. It improves
the built-in proxy capabilities of Firefox.

# User Agent Switcher

Adds a menu and tool bar button in the browser. Whenever you want to switch the user
agent, use the browser button. User Agent add on helps in spoofing the browser while
performing some attacks.

# Firebug

Firebug is a nice add-on that integrates a web development tool inside the browser. With
this tool, you can edit and debug HTML, CSS and JavaScript live in any webpage to see
the effect of changes. It helps in analyzing JS files to find XSS vulnerabilities.

# Hackbar

Hackbar is a simple penetration tool for Firefox. It helps in testing simple SQL injection
and XSS holes. You cannot execute standard exploits but you can easily use it to test
whether vulnerability exists or not. You can also manually submit form data with GET or
POST requests.

# Websecurify

WebSecurify can detect most common vulnerabilities in web applications. This tool can
easily detect XSS, SQL injection and other web application vulnerability.

# Cookie Manager+

Allows you to view, edit and create new cookies. It also shows extra information about
cookies, edit multiple cookies at once, backup and restore cookies, etc.

# XSS Me

XSS-Me is used to find reflected XSS vulnerabilities from a browser. It scans all forms
of the page, and then performs an attack on the selected pages with pre-defined XSS
payloads. After the scan is complete, it lists all the pages that renders a payload on the
page, and may be vulnerable to XSS. With those results, you should manually confirm
the vulnerabilities found.

# Offsec Exploit-db Search

This lets you search for vulnerabilities and exploits listed in exploit-db.com. This website
is always up-to-date with latest exploits and vulnerability details.

# Wappalyzer

https://addons.mozilla.org/en-us/firefox/addon/wappalyzer/
This tool will help you identify the technologies used on a site, including things like
CloudFlare, Frameworks, Javascript Libraries, etc
