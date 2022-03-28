from netmiko import ConnectHandler
import getpass

#get username from user
username=input("Enter SSH username: ")
#get password from user
password=getpass.getpass("Enter SSH password: ")

#open file to populate IP
with open('myswitches.txt') as switches:
    for IP in switches:
        arubav_1 = {
            'device_type': 'aruba_os',
            'ip': IP,
            'username': username , 
            'password': password ,
        }
        print('Connecting to ' + IP)
        print('-'*65)

        for devices in arubav_1:
            net_connect = ConnectHandler(**arubav_1)
            output = net_connect.send_command('show run')
            with open('backup_' + IP, 'w') as f:
                print (output, file=f)
        
