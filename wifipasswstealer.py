
# {{{***IMPORTANT USE PYTHON 3.8 TO  RUN ***}}}


import subprocess, re
color= subprocess.call("color 02", shell=True)
command = "netsh wlan show profile"
network= subprocess.check_output(command, shell=True)
network_name_list = re.findall("(?:Profile\s*:\s)(.*)",network)
# print(network_name_list)

for network_name in network_name_list:
    # print("PASSWORD FOR "+ network_name)
    command1 = "netsh wlan show profiles name=\""+network_name+"\" key=clear"
    network1= subprocess.check_output(command1, shell=True)
    result= re.search("(?:Content\s*:\s)(.*)",network1)
    # result1= str(result)ddddddddddddddddddddddddddddddddddddddddd
    # print("PASSWORD FOR "+network_name+" PAS")
    if result:
        # final_result = result.group(1)
        # print("Password for "+network_name+"is")
        # print("\n")
        with open("WIFI PASSWORDS.txt","a") as output:
            output.write("Password for "+network_name+"\tis\t" +result.group(1))
            # output.write("\n")
            # output.write(result.group(1))# color= subprocess.call("color 04", shell=True)
        # print(result.group(1))

        # print("\n")
    # if result.group(1) == None:
    #     Break
    # else:
    #     print result.group(1)
    # print(network)
# print final_result
# with open("WIFI PASSWORDS.txt","w") as output:
#     output.write(final_result)