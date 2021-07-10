import time
import paho.mqtt.client as paho
from datetime import datetime
import mysql.connector
import subprocess
import json

def mysqlfunc(ide,estado,formatofh,tabla):
    conexion = mysql.connector.connect(user="root", password="root", database="iot")
    query = f"INSERT INTO {tabla} Values('{ide}','{estado}','{formatofh}') ;"
    statement = conexion.cursor()
    statement.execute(query)
    conexion.commit()
    statement.close()
    conexion.close()

broker="rubenruiz.hopto.org"
#define callback
def on_message(client, userdata, message):
    #TIEMPO
    global time1,TL, TC, VS1,VS2, VS3, VS4, H1, H2, H3, H4, L1, L2, L3, L4, T1, T2, T3, T4, dicc
    time2= time.time()
    if ((time2-time1)>=TIEMPO): TL=1
    #print("TIEMPO : ",(time2-time1))

    #TERMINA TIEMPO

    #time.sleep(1)
    message = str(message.payload.decode("utf-8"))
    #print("EL MENSAJE ES: ",message)
    if ((message)=="1" or (message)=="0"):
        pass

    else:
        
        ide = int(message[2])
        estado = int(message[3:])
    
        now = datetime.now()
        formatofh = now.strftime("%Y-%m-%d %H:%M:%S")
        #client.publish("PRASP", "ENTRA message")
        #"V": {"VS1": "0","VS2": "0","VS3": "0","VS4": "0"}
        if (message[0:2]=="VE"):
            dicc[f'{message[0]}'][f'VS{message[2]}']=f'{message[3:]}'
        else:
            dicc[f'{message[0]}'][f'{message[0:3]}']=f'{message[3:]}'


        with open('/var/www/html/RTD.json', 'w') as outfile:
            
            json.dump(dicc, outfile)

    #print("received message = "+message)
    if (message[0:2]=="VS"):
        if (TL==1):
            if (VS1==0 and message[2]=="1"):
                
                mysqlfunc(ide,estado,formatofh,"Valvula")
                
                VS1 = 1
            if (VS2==0 and message[2]=="2"):
            
                mysqlfunc(ide,estado,formatofh,"Valvula")
                
                VS2 = 1
            if (VS3==0 and message[2]=="3"):
            
                mysqlfunc(ide,estado,formatofh,"Valvula")
                
                VS3 = 1
            if (VS4==0 and message[2]=="4"):
            
                mysqlfunc(ide,estado,formatofh,"Valvula")
                
                VS4 = 1
    
    elif(message[0:2]=="VE"):
        #mysqlfunc(ide,estado,formatofh,tabla)
        
        estado = 1
        mysqlfunc(ide,estado,formatofh,"Valvula")

        estado = 0
        mysqlfunc(ide,estado,formatofh,"Valvula")
    elif (message[0:2]=="HU"):
        
        if (TL==1):
            if (H1==0 and message[2]=="1"):
                
                mysqlfunc(ide,estado,formatofh,"Humedad")
                
                H1 = 1
            if (H2==0 and message[2]=="3"):
            
                mysqlfunc(ide,estado,formatofh,"Humedad")
                
                H2 = 1
            if (H3==0 and message[2]=="3"):
            
                mysqlfunc(ide,estado,formatofh,"Humedad")
                
                H3 = 1
            if (H4==0 and message[2]=="4"):
            
                mysqlfunc(ide,estado,formatofh,"Humedad")
                
                H4 = 1
    elif (message[0:2]=="TE"):
        
        if (TL==1):
            if (T1==0 and message[2]=="1"):
                
                mysqlfunc(ide,estado,formatofh,"S_temperatura")
                
                T1 = 1
            if (T2==0 and message[2]=="3"):
            
                mysqlfunc(ide,estado,formatofh,"S_temperatura")
                
                T2 = 1
            if (T3==0 and message[2]=="3"):
            
                mysqlfunc(ide,estado,formatofh,"S_temperatura")
                
                T3 = 1
            if (T4==0 and message[2]=="4"):
            
                mysqlfunc(ide,estado,formatofh,"S_temperatura")
                
                T4 = 1
    elif (message[0:2]=="LU"):
        
        if (TL==1):
            if (L1==0 and message[2]=="1"):
                
                mysqlfunc(ide,estado,formatofh,"S_iluminacion")
                
                L1 = 1
            if (L2==0 and message[2]=="3"):
            
                mysqlfunc(ide,estado,formatofh,"S_iluminacion")
                
                L2 = 1
            if (L3==0 and message[2]=="3"):
            
                mysqlfunc(ide,estado,formatofh,"S_iluminacion")
                
                L3 = 1
            if (L4==0 and message[2]=="4"):
            
                mysqlfunc(ide,estado,formatofh,"S_iluminacion")
                
                L4 = 1
    

    TC = VS1+VS2+VS3+VS4+H1+H2+H3+H4+T1+T2+T3+T4+L1+L2+L3+L4

    if (TC>=16 and TL==1):
        #print("ENTRA")
        VS1 = 0
        VS2 = 0
        VS3 = 0
        VS4 = 0
        H1 = 0
        H2 = 0
        H3 = 0
        H4 = 0
        T1 = 0
        T2 = 0
        T3 = 0
        T4 = 0
        L1 = 0
        L2 = 0
        L3 = 0
        L4 = 0

        TC = 0
        TL = 0
        time1 = time.time()



TIEMPO = 1

time1 = time.time()


Node1_VE = "N1Val_E"
Node1_VS = "N1Val_S"
Node1_H = "N1Hum"
Node1_I = "N1Ilum"
Node1_I = "N1Ilum"
Node1_T = "N1TE"
VS1 = 0
H1 = 0
L1 = 0
T1 = 0


Node2_VE = "N2Val_E"
Node2_VS = "N2Val_S"
Node2_H = "N2Hum"
Node2_I = "N2Ilum"
Node2_T = "N2TE"

VS2 = 0
H2 = 0
L2 = 0
T2 = 0

Node3_VE = "N3Val_E"
Node3_VS = "N3Val_S"
Node3_H = "N3Hum"
Node3_I = "N3Ilum"
Node3_T = "N3TE"

VS3 = 0
H3 = 0
L3 = 0
T3 = 0

Node4_VE = "N4Val_E"
Node4_VS = "N4Val_S"
Node4_H = "N4Hum"
Node4_I = "N4Ilum"
Node4_T = "N4TE"

VS4 = 0
H4 = 0
L4 = 0
T4 = 0

dicc = {"V": {"VS1": "0","VS2": "0","VS3": "0","VS4": "0"} ,"H": {"HU1": " ","HU2": " ","HU3": " ","HU4": " "},"T": {"TE1": " ","TE2": " ","TE3": " ","TE4": " "},"L": {"LU1": " ","LU2": " ","LU3": " ","LU4": " "}}

TL=0
TC= 0

client= paho.Client("RASPABABY") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
#client.loop_start() #start loop to process received messages

client.subscribe(Node1_VS)#subscribe
client.subscribe(Node1_VE)
client.subscribe(Node1_H)
client.subscribe(Node1_I)
client.subscribe(Node1_T)

client.subscribe(Node2_VS)
client.subscribe(Node2_VE)
client.subscribe(Node2_H)
client.subscribe(Node2_I)
client.subscribe(Node2_T)

client.subscribe(Node3_VS)
client.subscribe(Node3_VE)
client.subscribe(Node3_H)
client.subscribe(Node3_I)
client.subscribe(Node3_T)


client.subscribe(Node4_VS)
client.subscribe(Node4_VE)
client.subscribe(Node4_H)
client.subscribe(Node4_I)
client.subscribe(Node4_T)


time1= time.time()

#while True:
    
    #time.sleep(1)
    
    #client.publish("PRASP","on")#publish
    #client.disconnect() #disconnect
client.loop_forever() #stop loop