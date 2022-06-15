def f3(packet):
    try:
        if (packet['TCP']['dstport'] == 6667):
            data = packet['IRC']['request'].split(" ")
            if data[0] == 'TOPIC':
                print(packet['IRC']['request'])
                packet['IRC']['request'] = packet['IRC']['request'].replace('juegos','clases')
                print(packet['IRC']['request'])
                return packet
    except:
        print("except")
        return None