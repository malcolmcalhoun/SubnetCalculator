import  random
import sys

def subnet_calculator():
    try:
        print("\n")
        while True:
            ip_address = input("Enter an IP Address: ")
            ip_octets = ip_address.split('.')
            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and \
            (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or \
            int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and \
            0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break
            else:
                print("The IP address is not Valid. Try again")
                continue
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        while True:
            subnet_mask = input("Enter a Subnet Mask: ")
            mask_octets = subnet_mask.split('.')
            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and \
            (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and \
            (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >=\
            int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break
            else:
                print("this subnet mask is not Valid. Try again")
                continue

        binary_octet_masks = []
        for octets in mask_octets:
            binary_octet = bin(int(octets)).lstrip('0b')
            binary_octet_masks.append(binary_octet.zfill(8))        #Zfill method to fill in octets w/ zero to meet desired length

        binary_mask = "".join(binary_octet_masks)

        number_of_zeros = binary_mask.count("0")
        number_of_ones = 32 - number_of_zeros
        number_of_hosts = abs(2 ** number_of_zeros - 2)

        wildcard_octets = []
        for octets in mask_octets:
            wild_octet = 255 - int(octets)
            wildcard_octets.append(str(wild_octet))

        wildcard_mask = ".".join(wildcard_octets)

        ip_octects_binary = []
        for octets in ip_octets:
            binary_octet = bin(int(octets)).lstrip('0b')
            ip_octects_binary.append(binary_octet.zfill(8))        #Zfill method to fill in octets w/ zero to meet desired length

        binary_ip = "".join(ip_octects_binary)

        network_address_binary = binary_ip[:(number_of_ones)] + "0" * number_of_zeros
        broadcast_address_binary = binary_ip[:(number_of_ones)] + "1" * number_of_zeros

        net_ip_octets = []
        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit +8]
            net_ip_octets.append(net_ip_octet)

        net_ip_address = []

        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        #print(net_ip_address)
        network_address = ".".join(net_ip_address)

        bst_ip_octets = []
        for bit in range(0, 32, 8):
            bst_ip_octet = broadcast_address_binary[bit: bit +8]
            bst_ip_octets.append(bst_ip_octet)

        bst_ip_address = []
        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))

        print(bst_ip_address)
        broadcast_address = ".".join(bst_ip_address)

        print("\n")
        print("Network address: %s" % network_address)
        print("Broadcast adress: %s" % broadcast_address)
        print("Number of valid hosts per subnet: %s" % number_of_hosts)
        print("wildcard mask: %s" % wildcard_mask)
        print( "Mask bits: %s" % number_of_ones)

        while True:
            generate = input("Generate random IP address from this subnet?(y/n)")
            if generate == "y" or generate == "Y":
                generated_ip = []

                for indexb, oct_bst in enumerate(bst_ip_address):
                    for indexn, oct_net in enumerate(net_ip_address):
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                generated_ip.append(oct_bst) #append common octets between network address and broadcast address
                            else:
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst)))) #if the octets aren't the same print a random number between the two of them
            y_ipaddress = ".".join(generated_ip)

            print("Random IP address is: %s" % y_ipaddress)
            print("\n")
            continue
        else:
            print("OK, bye!\n")
            brea
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Goodbye...")
        sys.exit()

subnet_calculator()
