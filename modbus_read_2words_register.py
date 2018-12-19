#!/usr/bin/python
# coding: utf8
import sys
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

if len(sys.argv) != 4: #un seul argument ==> le nom de l'executable
        print("Pas assez d'arguments fournis\r\n")
        print("Usage : modbus.py host id_sur_le_bus numero_de_registre")
        print("./modbus.py 10.251.1.114 2 18458")
        exit()
else :
        host = sys.argv[1]
        slave_id = sys.argv[2]
        register_number = sys.argv[3]
        #print("Host ==> "+host)
        #print("ID du slave ==> "+slave_id)
        #print("Numéro du registre ==> "+register_number)

        client = ModbusClient(host, port=502)
        client.connect()

        response = client.read_holding_registers(int(register_number), 2, unit=int(slave_id)) #2 car on traite un mot de 2x16 bits


        word1 = response.registers[0]
        word2 = response.registers[1]
        courant = (word1 << 16) + word2
        courant = float(courant) / 1000

        print(str(courant)+" Amp | A="+str(courant))
