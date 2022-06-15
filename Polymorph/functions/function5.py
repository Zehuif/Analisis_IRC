def f5(packet):
    try:
        if (packet['TCP']['dstport'] == 6667):
            data = packet['IRC']['request'].split(" ")
            if data[0] == 'PING':
                packet['IRC']['request'] = ' '
                print("No PONG")
                return packet
    except:
        print("except")
        return None