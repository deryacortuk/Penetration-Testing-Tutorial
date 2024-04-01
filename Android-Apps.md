# https://github.com/OWASP/owasp-mstg/)

APKs are like ZIP files that contain 
everything an Android application needs to operate: the application code, 
the application manifest file, and the application’s resources.

AndroidManifest.xml file contains the application’s package 
name, version, components, access rights, and referenced libraries, as well 
as other metadata. 

There are four types of app 
components: Activities (declared in <activity> tags), Services (declared 
in <service> tags), BroadcastReceivers (declared in <receiver> tags), and 
ContentProviders (declared in <provider> tags).


Activities are application components that interact with the user.  Services
are long-running operations that do not directly interact with the user, such 
as retrieving or sending data in the background. BroadcastReceivers allow an 
app to respond to broadcast messages from the Android system and other 
applications. ContentProviders provide a way to share 
data with other applications. 

The permissions that the application uses, such as the ability to send 
text messages and the permissions other apps need to interact with it, are 
also declared in this AndroidManifest.xml file.

# The classes.dex file contains the application source code compiled in the DEX file format.

The resources.arsc file contains the application’s precompiled resources, 
such as strings, colors, and styles. The res folder contains the application’s 
resources not compiled into resources.arsc. In the res folder, the res/values/
strings.xml file contains literal strings of the application.
The lib folder contains compiled code that is platform dependent. Each 
subdirectory in lib contains the specific source code used for a particular 
mobile architecture. Compiled kernel modules are located here and are 
often a source of vulnerabilities.
The assets folder contains the application’s assets, such as video, audio, and 
document templates. Finally, the META-INF folder contains the MANIFEST.MF
file, which stores metadata about the application. This folder also contains the 
certificate and signature of the APK.

# Android Debug Bridge
The Android Debug Bridge (ADB) is a command line tool that lets your computer communicate with a connected Android device. This means you won’t 
have to email application source code and resource files back and forth 
between your computer and your phone if you want to read or modify them 
on the computer. For example, you can use ADB to copy files to and from 
your device, or to quickly install modified versions of the application you’re 
researching. ADB’s documentation is at https://developer.android.com/studio/
command-line/adb/.

# Android Studio
Android Studio is software used for developing Android applications, and you 
can use it to modify an existing application’s source code. It also includes 
an emulator that lets you run applications in a virtual environment if you 
don’t have a physical Android device. You can download and read about 
Android Studio at https://developer.android.com/studio/.

# Apktool
Apktool, a tool for reverse engineering APK files, is essential for Android 
hacking and will probably be the tool you use most frequently during your 
analysis. It converts APKs into readable source code files and reconstructs 
an APK from these files. The Apktool’s documentation is at https://ibotpeaches
.github.io/Apktool/.

# Frida
Frida (https://frida.re/) is an amazing instrumentation toolkit that lets you 
inject your script into running processes of the application. You can use it 
to inspect functions that are called, analyze the app’s network connections, 
and bypass certificate pinning.
Frida uses JavaScript as its language, so you will need to know JavaScript 
to take full advantage of it. However, you can access plenty of premade 
scripts shared online.

# Mobile Security Framework
I also highly recommend the Mobile Security Framework (https://github.com/
MobSF/Mobile-Security-Framework-MobSF/), or the MobSF, for all things 
mobile app testing. This automated mobile application testing framework 
for Android, iOS, and Windows can do both static and dynamic testing. It 
automates many of the techniques that I talk about in this chapter and is a 
good tool to add to your toolkit once you understand the basics of Android 
hacking.

Mobile apps also tend 
to have issues with session management, such as reusing session tokens, 
using longer sessions, or using session cookies that don’t expire. These 
issues can be chained with XSS to acquire session cookies that allow attackers to take over accounts even after users log out or change their passwords. 
Some applications use custom implementations for encryption or hashing. 
Look for insecure algorithms, weak implementations of known algorithms, 
and hardcoded encryption keys. After reviewing the application’s source 
code for potential vulnerabilities, you can validate your findings by testing 
dynamically on an emulator or a real device.
