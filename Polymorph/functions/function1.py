def f1(packet):
    try:
        if (packet['TCP']['dstport'] == 6667):
            data = packet['IRC']['request'].split(" ")
            if data[0] == 'PRIVMSG':
                print(packet['IRC']['request'])
                packet['IRC']['request'] = packet['IRC']['request'].replace('hola','chao')
                print(packet['IRC']['request'])
                return packet
    except:
        print("except")
        return None