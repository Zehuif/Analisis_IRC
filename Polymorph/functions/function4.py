def f4(packet):
    try:
        if (packet['TCP']['dstport'] == 6667):
            data = packet['IRC']['request'].split(" ")
            if data[0] == 'PRIVMSG':
                print(packet['IRC']['request'])
                packet['IRC']['request'] = packet['IRC']['request'].replace('#channel1','#channel2')
                print(packet['IRC']['request'])
                return packet
    except:
        print("except")
        return None