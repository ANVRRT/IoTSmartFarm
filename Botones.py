#!/usr/bin/env python3.7
import time
import paho.mqtt.client as paho
import sys

class ClienteController:
    def procesarTransaccion(self):
        if(B == "boton1"):
            client= paho.Client("Boton1") 
            client.connect(broker)#connect
            client.publish(Node1_VE,"0")#publish
            client.publish(Node1_VE,"VE11")
            time.sleep(1)
            client.publish(Node1_VE,"1")
            client.publish(Node1_VE,"VE10")
            client.disconnect() #disconnect
            #AQUI MANDA MOSQUITO
        elif (B == "boton2"):
            client= paho.Client("Boton2") 
            client.connect(broker)#connect
            client.publish(Node2_VE,"0")#publish
            client.publish(Node2_VE,"VE21")
            time.sleep(1)
            client.publish(Node2_VE,"1")
            client.publish(Node2_VE,"VE20")
            client.disconnect() #disconnect
            #AQUI MANDA MOSQUITO
        elif (B == "boton3"):
            client= paho.Client("Boton3") 
            client.connect(broker)#connect
            client.publish(Node3_VE,"0")#publish
            client.publish(Node3_VE,"VE31")
            time.sleep(1)
            client.publish(Node3_VE,"1")
            time.sleep(0.3)
            client.publish(Node3_VE,"VE30")
            client.disconnect() #disconnect
            #AQUI MANDA MOSQUITO
        elif (B == "boton4"):
            client= paho.Client("Boton4") 
            client.connect(broker)#connect
            client.publish(Node4_VE,"0")#publish
            client.publish(Node4_VE,"VE41")
            time.sleep(1)
            client.publish(Node4_VE,"1")
            client.publish(Node4_VE,"VE40")
            client.disconnect() #disconnect
            #AQUI MANDA MOSQUITO
            

# Crear el objeto de la clase Primero
broker="rubenruiz.hopto.org"
Node1_VS = "N1Val_S"
Node2_VS = "N2Val_S"
Node3_VS = "N3Val_S"
Node4_VS = "N4Val_S"


Node1_VE = "N1Val_E"
Node2_VE = "N2Val_E"
Node3_VE = "N3Val_E"
Node4_VE = "N4Val_E"


V = sys.argv[1]
B = sys.argv[2]


cliente = ClienteController()
#cliente.respuestaServer2()
cliente.procesarTransaccion()

