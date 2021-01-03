import  random
import sys
from validity_checker_test import ip_validity_checker

def subnet_calculator():        #define a function to calculate network parameters from IP address and subnet masks
    try:                #try clause to print a new line
        print("\n")     #print newline
        ip_address = (input("Enter an IP Address: ")) #prompt the user for an IP address
        ip_octets = ip_address.split('.')       #split the ip address by '.' and assign them to a ip octet list
        ip_validity_checker(ip_octets)  #check the validity of the ip octets using the ip validity checker object function
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0] #create a list of subnet masks

        while True:         #while true
            subnet_mask = input("Enter a Subnet Mask: ") #prompt the user from subnet mask input and assign it to a variable
            mask_octets = subnet_mask.split('.')        #split input by "." and assign them to a new variable

            #if the length of the mask_octets list is 4 and the first octet is between 0 and 255
            #and if the 2nd, 3rd, and 4th octets are in the masks list
            #and the 2nd octet is greater than the 3rd and the 3rd octet is greater than the 4th
            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and \
            (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and \
            (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >=\
            int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                print("Subnet mask is Valid.")   #then print subnet mask is valid
                break
            else:       #or else
                print("this subnet mask is not Valid. Try again") #print the subnet mask is not valid
                continue    #continue

        binary_octet_masks = []         #create an empty list for binary_octet_masks
        for octets in mask_octets:      #for every octet in the mask_octets
            binary_octet = bin(int(octets)).lstrip('0b')    #print the binary conversion of each octet and strip "0b" from the output
            #add the binary conversion of each octet to the binary_octet_masks list Zfill method to fill in octets w/ zero to meet desired length
            binary_octet_masks.append(binary_octet.zfill(8))

        binary_mask = "".join(binary_octet_masks)   #join the binary_octet_masks list into one string and assign it to a variable

        number_of_zeros = binary_mask.count("0")     #count the number of zeros in the binary_mask
        number_of_ones = 32 - number_of_zeros       #the number of ones is equal to 32 - the number of zeros
        number_of_hosts = abs(2 ** number_of_zeros - 2) #the number of hosts is the absolute value of (2 times the number of zeros minus 2)

        wildcard_octets = []                    #create a wildcard octet list
        for octets in mask_octets:              #for the octets in the mask_octets
            wild_octet = 255 - int(octets)      #wildcard octet is 244 minus the number of each octet
            wildcard_octets.append(str(wild_octet)) #add the wildcard octets to the wildcard_octets list

        wildcard_mask = ".".join(wildcard_octets)   #join the wildcard_octets list together into one string

        ip_octects_binary = []          #create an empty ip_octets_binary list
        for octets in ip_octets:        #for the octets in the ip_pctets list
            binary_octet = bin(int(octets)).lstrip('0b')    #convert each octet to binary and remove and "0b" characters
            #add the binary conversion of each octet to the ip_octets_binary list Zfill method to fill in octets w/ zero to meet desired length
            ip_octects_binary.append(binary_octet.zfill(8))

        binary_ip = "".join(ip_octects_binary)  #join the ip_octets_binary list together into one string

        network_address_binary = binary_ip[:(number_of_ones)] + "0" * number_of_zeros     #the network address binary is the number of ones plus the number of zeros
        broadcast_address_binary = binary_ip[:(number_of_ones)] + "1" * number_of_zeros    #the broadcast address is all 1's

        net_ip_octets = []                  #create an empty net_ip_octets list
        for bit in range(0, 32, 8):         #for every bit in the range 0-32 by steps of 8
            net_ip_octet = network_address_binary[bit: bit +8] #split up the network_address_binary into slices of 8(bits) and add them to the net_ip_octet list
            net_ip_octets.append(net_ip_octet)      #add each net_ip_octet to the net_ip_octets list

        net_ip_address = []                 #create an empty net_ip_address list

        for each_octet in net_ip_octets:        #for each octet in the net_ip_octets list
            net_ip_address.append(str(int(each_octet, 2)))  #append the string version of the integer conversion of each octet(convert from binary to base 10)


        network_address = ".".join(net_ip_address) #join the net_ip_address list together into a string assigned to a variable

        bst_ip_octets = []                  #create an empty broadcast ip octets list
        for bit in range(0, 32, 8):          #for every bit in the range 0-32 by steps of 8
            bst_ip_octet = broadcast_address_binary[bit: bit +8]    #split up the bst_address_binary into slices of 8(bits) and add them to the net_ip_octet list
            bst_ip_octets.append(bst_ip_octet)   #add each net_ip_octet to the net_ip_octets list

        bst_ip_address = []              #create an empty bst_ip_address list
        for each_octet in bst_ip_octets:    #for each octet in the bst_ip_octets list
            bst_ip_address.append(str(int(each_octet, 2)))     #append the string version of the integer conversion of each octet(convert from binary to base 10)


        broadcast_address = ".".join(bst_ip_address)    #join the bst_ip_address list together into a string assigned to a variable

        print("\n")
        print("Network address: %s" % network_address)      #print the network address
        print("Broadcast adress: %s" % broadcast_address)   #print the broadcast address
        print("Number of valid hosts per subnet: %s" % number_of_hosts) #print the nuber of valid hosts per subnet
        print("wildcard mask: %s" % wildcard_mask)  #print the wildcard mask
        print( "Mask bits: %s" % number_of_ones)    #print the mask bits

        while True:     #while true
            generate = input("Generate random IP address from this subnet?(y/n)")   #y or n to generate random ip address with network paarameters
            if generate == "y" or generate == "Y":      #if yes
                generated_ip = []                       #create an empty generated_ip list

                for indexb, oct_bst in enumerate(bst_ip_address):   #for loop to map the broadcast address to an index
                    for indexn, oct_net in enumerate(net_ip_address):   # for loop map the network address to an index
                        if indexb == indexn:        #if indexb matches indexn then
                            if oct_bst == oct_net:  #if the broadcast octet and the netowrk octet print then
                                generated_ip.append(oct_bst) #append common octets between network address and broadcast address
                            else: #or else
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst)))) #if the octets aren't the same print a random number between the two of them and add the octets to the generate_ip list
            y_ipaddress = ".".join(generated_ip) #join the generated_ip list together into one string and assign it to a variable

            print("Random IP address is: %s" % y_ipaddress)     #print the random ip address
            print("\n")         #print a newline
            if generate == "n" or generate == "N":      #if the input is no
                print("OK, bye!\n")         #print ok bye
                break           #then exit loop
    except KeyboardInterrupt:   #except clause to interrupt the program using CTRL-C
        print("\n\nProgram aborted by user. Goodbye...")#print abort message
        sys.exit()  #exit

subnet_calculator()     #call the main function
