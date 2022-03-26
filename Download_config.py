from netmiko import ConnectHandler
import getpass

#get/store device IP from user
address=input("Enter the IP address of the device: ")
straddress = str(address)
#get/store username from user
username=input("Enter your username: ")
stusername= str(username)
#get/store password from user
password=getpass.getpass("Enter your password: ")
stpassword= str(password)
#create file name
filename=input("What would you like to name the output file? ")
stfilename = str(filename)

#create dictionary
arubav_1 = {
    'device_type': 'aruba_os',
    'ip': straddress,
    'username': stusername , 
    'password': stpassword ,
}
#Connect to device and send command
net_connect = ConnectHandler(**arubav_1)
output = net_connect.send_command('show run')

#Copy output into a file
with open(filename, 'w') as f:
    print (output, file=f)
