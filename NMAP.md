MAC address spoofing involves altering the original MAC address to conceal the true identity of the sender. This technique is employed to mask the source of network traffic. To execute this method, use the command nmap --spoof-mac <spoofed-MAC> targetIP.

Source port manipulation involves altering the original source port to a frequently used port, thereby increasing the difficulty for IDS or firewalls to identify and thwart the scanning activity. To execute this technique, use the command nmap -g <common-source-port> targetIP.

IP address spoofing enables the creation or manual selection of a decoy IP address, presenting a significant hurdle for IDS or firewalls in accurately identifying the true source. To employ this technique, utilize the command nmap -S <decoy-IP> targetIP or nmap -D RND:<random host number> targetIP


The technique of packet fragmentation entails dispatching fragmented probe packets to the target, which are then reassembled upon reception. This approach can effectively bypass specific Intrusion Detection Systems (IDS) and firewalls. To utilize this technique, execute the command nmap -f targetIP.


## Creating custom packets

1. The --data-length command facilitates the specification of the desired
length for the appended data. To utilize this functionality, execute the
command nmap --data-length <length> targetIP.


2.The --data-string command allows for the addition of a specific string to
the packets, allowing the inclusion of customized content. To utilize this
feature, execute the command nmap --data-string "<string>" targetIP.

3.The --data command, on the other hand, enables the inclusion of custom
data in various formats, including binary, by providing the data in
hexadecimal format. To utilize this functionality, execute the command
nmap --data <hex string> targetIP.

## Nmap Scripting Engine

Nmap Scripting Engine (NSE) scripts enable the utilization of specific scripts tailored to bypass firewall restrictions and uncover vulnerabilities. These scripts encompass techniques like packet fragmentation, source port manipulation, IP address spoofing, and other methods explicitly devised to bypass firewalls. To execute the script, use the command nmap --script=firewall-bypass targetIP

