Fuzzing is the process of sending a wide range of invalid and unexpected data 
to an application and monitoring the application for exceptions. Fuzzing is particularly useful for exposing bugs like memory 
leaks, control flow issues, and race conditions.


SecLists by Daniel Miessler (https://github.com/
danielmiessler/SecLists/) and Big List of Naughty Strings by Max Woolf 
(https://github.com/minimaxir/big-list-of-naughty-strings/) for a pretty comprehensive payload list useful for fuzzing web applications. Among other features, 
these lists include payloads for the most common web vulnerabilities, such 
as XXS, SQL injection, and XXE. Another good wordlist database for 
both enumeration and vulnerability fuzzing is FuzzDB (https://github.com/
fuzzdb-project/fuzzdb/).

# Fuzzing with Wfuzz
Now that you understand the general approach to take, let’s walk through 
a hands-on example using Wfuzz, which you can install by using this 
command:

$ pip install wfuzz

 Fuzzing is useful in both the recon phase and the hunting phase: you 
can use fuzzing to enumerate filepaths, brute-force authentication, test for 
common web vulnerabilities, and more.
Path Enumeration
During the recon stage, try using Wfuzz to enumerate filepaths on a server. 
Here’s a command you can use to enumerate filepaths on example.com:

$ wfuzz -w wordlist.txt -f output.txt --hc 404 --follow http://example.com/FUZZ

Wfuzz to fuzz the authentication 
headers, using the -H flag to specify custom headers:

$ wfuzz -w wordlist.txt -H "Authorization: Basic FUZZ" http://example.com/admin

wfuzz -w usernames.txt -w passwords.txt --basic FUZZ:FUZ2Z http://example.com/admin

Other ways to bypass authentication by using brute-forcing include 
switching out the User-Agent header or forging custom headers used for 
authentication. You could accomplish all of these by using Wfuzz to bruteforce HTTP request headers

$ wfuzz -w wordlist.txt -v –-follow http://example.com?redirect=FUZZ

$ wfuzz -w xss.txt --filter "content~FUZZ" http://example.com/get_user?user_id=FUZZ





