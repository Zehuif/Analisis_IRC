def f2(packet):
     try:
        if (packet['TCP']['dstport'] == 6667):
            data = packet['IRC']['request'].split(" ")
            if (data[0] == "PART"):
                packet["IRC"]["request"] = packet["IRC"]["request"].replace("PART","JOIN")
                print('No PART')
                return packet
     except:
        print ("except")
        return None