# JoomScan
JoomScan can detect known vulnerabilities, such as file inclusion, command execution, and 
injection flaws, in Joomla CMS. It probes the application and extracts the exact version the
target is running.

# WPScan
WPScan is a very fast WordPress vulnerability scanner written in the Ruby programming
language and preinstalled in Kali Linux.
The following information can be extracted using WPScan:
  
   The name of the theme
   Weak passwords and usernames using the brute forcing technique
   Details of the version
   Possible vulnerabilities

# CMSmap
CMSmap is not included in Kali Linux, but is easily installable from GitHub. This is a
vulnerability scanner for the most commonly used CMSes: WordPress, Joomla, and Drupal.
It uses Exploit Database to look for vulnerabilities in the enabled plugins of CMS. To
download it, issue the following command in Kali Linux Terminal:
git clone https://github.com/Dionach/CMSmap.git

# ProxyStrike
Also included in Kali Linux is an active proxy known as ProxyStrike. This proxy not only
intercepts the request and response, but it also actively finds vulnerabilities. It has modules
to find SQL injection and XSS flaws. Similar to other proxies that have been discussed
previously, you need to configure the browser to use ProxyStrike as the proxy. It performs
automatic crawling of the application in the background, and the results can be exported to
both HTML and XML formats.

# Web Crawlers and Directory Bruteforce
Some applications have hidden web directories that an ordinary user interacting with the
web application will not see. Web crawlers try to explore all links and references within a
web page and find hidden directories. Apart from the spidering and crawling features of
some proxies, Kali Linux includes some really useful tools for this purpose.

# DIRB
DIRB is a command-line tool that can help you discover hidden files and directories in web
servers using dictionary files (such as, lists of possible filenames). It can perform basic
authentication and use session cookies and custom user agent names for emulating web
browsers.

# DirBuster
DirBuster is a Java application that performs a brute force attack on directories and
filenames on the web application. It can use a file containing the possible file and directory
names or generate all possible combinations. DirBuster uses a list produced by surfing the
internet and collecting the directory and files that developers use in real-world web
applications. DirBuster, which was developed by OWASP, is currently an inactive project
and is provided now as a ZAP attack tool rather than a standalone tool.

# Uniscan
Uniscan-gui is a comprehensive tool that can check for existing directories and files as well
as perform basic port scans, traceroutes, server fingerprinting, static tests, dynamic tests,
and stress tests against a target.

# Web Vulnerability Scanners
# Nikto
Nikto is long-time favorite of web penetration testers. Few features have been added to it
recently, but its development continues. It is a feature-rich vulnerability scanner that you
can use to test vulnerabilities on different web servers. It claims to check outdated versions
of software and configuration issues on several of the popular web servers.
Some of the well-known features of Nikto are as follows:
It generates output reports in several forms such as HTML, CSV, XML, and text
It includes false positive reduction using multiple techniques to test for
vulnerabilities
It can directly login to Metasploit
It does Apache username enumeration
It finds subdomains via brute force attacks
It can customize maximum execution time per target before moving on to the
next target

# w3af
The Web Application Attack and Audit Framework (w3af) is a web application
vulnerability scanner. It is probably the most complete vulnerability scanner included in
Kali Linux.

# Skipfish
Skipfish is a vulnerability scanner that begins by creating an interactive site map for the
target website, using a recursive crawl and prebuilt dictionary. Each node in the resulting
map is then tested for vulnerabilities. Speed of scanning is one of its major features that
distinguishes it from other web vulnerability scanners. It is well-known for its adaptive
scanning features, for more intelligent decision making from the response received in the
previous step. It provides a comprehensive coverage of the web application in a relatively
short time. The output of Skipfish is in the HTML format.


# OpenVAS
The Open Vulnerability Assessment Scanner (OpenVAS) is a network vulnerability
scanner in Kali Linux. A penetration test should always include a vulnerability assessment
of the target system, and OpenVAS does a good job of identifying vulnerabilities on the
network side. OpenVAS is a fork of Nessus, one of the leading vulnerability scanners in the
market, but its feeds are completely free and licensed under GPL. The latest version of Kali
Linux doesn't include OpenVAS, but it can be easily downloaded and installed using APT
as follows:
$ apt-get install openvas
Once installed in Kali Linux, OpenVAS requires an initial configuration before you start
using it. Go to Applications | Vulnerability Analysis, and select OpenVAS initial setup.
Kali Linux needs to be connected to the internet to complete this step as the tool downloads
all of the latest feeds and other files. At the end of the setup, a password is generated, which
is to be used during the login of the GUI interface:
You can now open the graphical interface by pointing your browser to
https://127.0.0.1:9392. Accept the self-signed certificate error, and then log in with
the admin username and the password generated during the initial configuration.
OpenVAS is now ready to run a vulnerability scan against any target. You can change the
password after you log in, by navigating to Administrations | Users and selecting the edit
user option (marked with a spanner) against the username.
The GUI interface is divided into multiple menus, as described here:
Dashboard: A customizable dashboard that presents information related to
vulnerability management, scanned hosts, recently published vulnerability
disclosures and other useful information.
Scans: From here you can start a new network VA scan. You will also find all of
the reports and findings under this menu.
Assets: Here you will find all of the accumulated hosts from the scans.
SecInfo: The detailed information of all the vulnerabilities and their CVE IDs are
stored here.
Configuration: Here you can configure various options, such as alerts,
scheduling, and reporting formats. Scanning options for host and open port
discovery can also be customized using this menu.
Extras: Settings related to the OpenVAS GUI, such as time and language, can be
done from this menu.
Administration: Adding and deleting users and feed synchronization can be
done through the Administration menu.

# Web application fuzzers
A fuzzer is a tool designed to inject random data into a web application. A web application
fuzzer can be used to test for buffer overflow conditions, error handling issues, boundary
checks, and parameter format checks. The result of a fuzzing test is to reveal vulnerabilities
that cannot be identified by web application vulnerability scanners. Fuzzers follow a trial
and error method and require patience while identifying flaws.
Burp Suite and WebScarab have a built-in fuzzer. Wfuzz is a one-click fuzzer available in
Kali Linux.

# Hackazon
Hackazon is a project from Rapid7, the company that makes Metasploit. It was first
intended to demonstrate the effectiveness of their web vulnerability scanner and then
released as open source. This is a modern web application (that is, it uses AJAX, web
services, and other features that you'll find in today's websites and applications). Hackazon
simulates an online store, but it has several security problems built in. You can practice
online at: http://hackazon.webscantest.com/. Alternatively, if you feel like setting up a
virtual server and installing and configuring it there, go to:
https://github.com/rapid7/hackazon.

# Web Security Dojo
The Web Security Dojo project from Maven Security is a self-contained virtual machine
that has vulnerable applications, training material, and testing tools included. This project is
very actively developed and updated. The latest version at the time of this writing is 3.0,
which was released in May 2017. It can be obtained from:
https://www.mavensecurity.com/resources/web-security-dojo

ZeroBank: This is a vulnerable banking application: http://zero.webappsecurity.com/login.html.

Acunetix's SecurityTweets: This is a Twitter-like application focused on HTML5 security: http://testhtml5.vulnweb.com/#/popular.

OWASP's vulnerable web applications directory: This is a curated list of publicly available vulnerable web applications for security testing:
https://github.com/OWASP/OWASP-VWAD.

VulnHub: A repository for vulnerable virtual machines and Capture The Flag (CTF) challenges. It contains some virtual machines with web applications:
https://www.vulnhub.com.
