# Penetration-Testing-Tutorial

*## Cybersecurity Software*

Network Forensic Tools
- Nmap
- Wireshark
- Xplico
- Snort
- TCPDump
- The Slueth Kit

Mobile Forensics Tools
- Elcomspoft iOS Forensic Toolkit
- Mobile Verification Toolkit
- Oxygen Forensic
- MOBILedit
- Cellebrite UFED
- MSAB XRY

Malware Analysis Tools
- Wireshark
- YARA
- Malwarebytes
- VirusTotal
- Cuckoo Sandbox
- IDA Pro

Data Recovery Tools
- Recuva
- EaseUS Data Recovery
- TestDisk
- Stellar Data Recovery
- PhotoRec
- Disk Drill

Email Forensic Tools
- MailXaminer
- MailPro+
- Xtraxtor
- Aid4Mail
- eMailTrackerPro
- Autopsy

OSINT Tools
- Maltego
- Nmap
- OSINT Framework
- Shodan
- Recon-ng
- TheHavester

Live Forensics Tools
- OS Forensics
- Encase Live
- CAINE
- F-Response
- Kali Linux Forensic Mode

Memory Forensics Tools
- Volatility
- DumpIt
- memDump
- Access data FTK Imager
- Hibernation Recon
- WindowSCOPE

Cloud Forensic Tools
- Magnet AXIOM
- MSAB XRY Cloud
- Azure CLI

Cybersecurity Tools By Category 

Information Gathering:
>Nmap

>Shodan

>Maltego

>TheHavester

>Recon-NG

>Amass

>Censys

>OSINT Framework

>Gobuster 

Exploitation:
>Burp Suite

>Metasploit Framework

>SQL Map

>ZAP

>ExploitDB

>Core Impact

>Cobalt Strike

Password Cracking:
>John The Ripper

>Hydra

>Hashcat

>OPHCrack

>Medusa

>THC-Hydra

>Cain & Abel

Vulnerability Scanning:
>OpenVAS

>Nessus

>AppScan

>LYNIS

>Retina

>Nexpose 

Software Engineering:
>GoPhish

>HiddenEye

>SocialFish

>EvilURL

>Evilginx

Forensics:
>SluethKit

>Autopsy

>Volatility

>Guymager

>Foremost

>Binwalk

>Wireshark 

Wireless Hacking:
>Aircrack-NG

>Wifite

>Kismet

>TCPDump

>Airsnort

>Netstumbler

>Reaver

Web Application Assessment:
>OWASP ZAP

>Burp Suite

>Nikto

>ZAP

>WPScan

>Gobuster

>App Spider

Top 35 Cybersecurity Tools

1. Nmap
2. Metaspoilt
3. Cain and Abel
4. Wireshark
5. Kali Linux
6. John the Ripper
7. Nikto
8. Forcepoint
9. Burp Suite 
10. Tor

11. Tcpdump
12. Aircrack-ng
13. Splunk 
14. Netstumbler 
15. Acunetix 
16. OSSEC
17. VIPRE
18. Avira 
19. Naggios
20. Snort
21. Argus
22. Keypass 
23. KisMAC 
24. Truecrypt 
25. Nessus

26. Webroo 
27. Lifelock 
28. Mimecast 
29. Malwarebytes 
30. POf 
31. Paros Proxy
32. OpenVAS
33. BluVector
34. OSSIM
35. ClamAV

Top 10 Tools used to crack WI-FI Password 

1. Wifite 
2. Kismet 
3. Fluxion. 
4. Cain and Abel 
5. Airjack 
6. Aircrack-ng 
7. CoWPAtty
8. Wireshark 
9. Airgeddon 
10.  Wifiphiser

#Wordlist
● https://github.com/danielmiessler/SecLists
● https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/RobotsDisallowed-Top1000.txt
● https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/raft-large-directories.txt
● https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/raft-large-files.txt
● https://github.com/assetnote/commonspeak2
● https://github.com/assetnote/commonspeak2-wordlists
● https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056
● https://github.com/internetwache/CT_subdomains



# ICS
Industrial Control Systems or ICS have received a lot of attention lately. In the US the ICS-CERT was established and ENISA has a whole unit devoted to Industrial Control Systems/SCADA. But for most people working in IT it is still a relatively new playing field.

Because every area in technology has its own specific vocabulary I wrote a small intro to PLCs, ICS and SCADA of the different components that play in the ICS field.
What is PLC, ICS, SCADA?
What is an ICS?
What is an Industrial Control Systems or ICS? An ICS is divided into different parts.

Production network

Sensors, the input and output to the PLCs
RTU, the Remote Terminal Units (a PLC, to be used remotely)
Contains classical wireless networks
Supervision network
Sometimes called the SCADA network
Workstations with the supervision software installed
This is the place from where engineers manage the processes
Maintenance laptops
Servers specific to the process
Corporate network
Workstations
Connected with supervision network for gathering data for optimization
Import data to SAP (or any other ERP)
What we call ICS is basically production and supervision network. It is the network that has the connection with the physical world.

Vocabulary
A bit of vocabulary:

ICS : Industrial Control System

IACS : Industrial Automation and Control Systems

SCADA : Supervisory Control And Data Acquisition

DCS : Distributed Control System

Remember that SCADA is only one part of the ICS but sometimes people mix the terms. If someone refers to SCADA make sure that they don’t mean the entire ICS.

ICS Components
An ICS often consists of these components

Sensors and actuators : The connectors to the real physical world. Consider the sensor as some kind of switch and the actuator as the component that does the action.

Local HMI : Human Machine Interface, useful to interact with a subprocess

PLC : programmable logic control manages the sensors and actuators

Supervision screen : remote supervision of the industrial process

Data historian : records data and allows exporting to the corporate network

Stuxnet: game changer

The discovery of Stuxnet in 2010 / 2011 changed the view on ICS security. What is currently wrong with ICS security?

No awareness : they care about physical safety and not security, often remote access of the process is not always assessed properly;

Limited staff : only a few people involved with IT (and that most often does not mean ‘security’);

Lack of network segmentation : There are no real DMZ or firewalls. The access control is done via ACLs on routers. Sometimes it’s fairly easy to jump from the corporate network to the ICS network;

Vulnerability management : it is not easy to apply patches because you can not just shut down a plant. Often the Windows machines are not patched (sometimes because they are not connected to the Windows Update Systems). PLCs are sometimes updated with firmware updates but patching also requires a shutdown of the industrial process. Because of this, although the patches are published they are rarely applied;

Security protocols : there is no IT security included in the protocols (no authentication, clear text protocols, …);

Third party management : some environments need to allow remote support to their specific devices;

Security supervision : ICS is all about monitoring a process, not monitoring the security state of a process.

ICS is about monitoring an industrial system, not monitoring the security state of a system.


What is a PLC?

A PLC is a programmable logic control. It is some kind of real-time computer. It is designed to manage input and output of processes. It was invented to replace electric relays.

It consists of hardware, firmware/OS and applications. The last is one is the programmable logic that is run through the middleware. There are different ways to program a PLC. The “ladder logic” was the first programming language for PLC, as it mimics the real-life circuits. Afterwards there were 5 programming languages defined for PLCs.

Unity Pro is software that you have to use if you want to control most of the Schneider PLCs.

Where do you find systems on the Internet?

You can find a list of systems (not restricted to PLCs) connected to the Internet via Shodan. You can search for “interesting” strings. For example search for Schneider PLC: M340 or S7-1200.

# Modbus

Modbus Protocol

Modbus is a serial communication protocol. It is the most widespread used protocol within ICS.

I have a separate blog post with an introduction to Modbus TCP traffic.

Detecting PLCs

Next to using Shodan you can use a couple of scripts to detect PLCs on your network. A word of warning. The TCP/IP stack in some PLCs might not be fully mature. If you send uncommon traffic you might crash the PLC. Never do the scanning without permission.

You can use

nmap : network port scanner

PLCScan : PLC devices scanner (port 102 for Siemens, port 502 for Modbus)

Nmap has a script to query for example Modbus devices and Siemans S7 PLC devices.


sudo nmap -p 502 -sV --script modbus-discover 127.0.0.1

sudo nmap -p 102 -sV --script s7-info 127.0.0.1

Detect attacks on ICS devices

There are a number of techniques and tools that you can use to detect attacks on ICS devices. A large number of these attacks will contain a network component. This means that using basic network security monitoring and intrusion detection will already get you very far.

Honeypot

Conpot is a low interactive server side Industrial Control Systems honeypot designed to be easy to deploy, modify and extend.

Industrial Control Systems Library: Poster

The Fall 2015 poster from the SANS institute details the SANS ICS Curriculum and what categories of actions contribute to security.

https://www.vanimpe.eu/2015/12/06/intro-plcs-ics-scada/

https://www.vanimpe.eu/2015/12/07/introduction-to-modbus-tcp-traffic/

