# Netmiko_Aruba
Download and Save Running Configuration of HP Aruba Switch

This file will prompt a user for a device ip address, device username, device password, and . The input will be taken and stored into variables for use in the following lines. 

Lines 18-23 create a dictionary populated with the necessary variables for Netmiko to SSH into the device, run the commands, and send the output. 

Lines 25 and 26 will use ConnectHandler within Netmiko to SSH into the device and run the command "show run" against the device. 

Lines 28 and 29 will create a file using the file name specified on line 14 and will output the file to the current working directory. 

