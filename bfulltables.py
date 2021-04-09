#!/usr/bin/env python3.7
import sys
import mysql.connector


class ClienteController:
    
    
    def __init__ (self):
        self.ide    = None
        self.estado=None
        self.fh=None
        global V,B,HR
        global libs
    
    def header(self):
        print("<h2>TABLA DE HUERTO: "+V+"</h2>")
        print("<tr> <td style='padding: 15px; color: white;'> ID </td> <td style='padding: 15px; color: white;'> ESTADO </td><td style='padding: 15px; color: white;'> FECHA </td> <td style='padding: 15px; color: white;'> HORA </td></tr>")
        
    def tablas(self,IDET,ESTADOT,FECHAT,HORAT):
        
        print("<tr> <td style='padding: 15px; color: black; '>"+IDET+"</td>"+"<td style='padding: 15px; color: black;'>"+ESTADOT+"</td>"+"<td style='padding: 15px; color: black;'>"+FECHAT+"</td>"+"<td style='padding: 15px; color: black;'>"+HORAT+"</td>")


    def respuestaServer1(self, datos):
        
        print(libs)
        print("<html>")
        print("<head><title>SQL</title></head>")
        print("<body>")
        
        print("<table class='styled-table' border=1; style='background-color: #009879;'>")
        stCliente = datos.split("\n")
        i = 0
        
        self.header()
        while(i<len(stCliente)):
            cliente=stCliente[i]
            cliente = cliente.split("_")
            try:
                if (cliente[1]=="1"):
                    estado="AB"
                else:
                    estado="CE"
            except:
                pass
            self.tablas(cliente[0],estado,(cliente[2])[0:10],(cliente[2])[10:])
            
            i=i+1
        print("</div>")
        print("</body>")
        print("</html>")
    
    def respuestaServer5(self, datos):
        print(libs)
        print("<html>")
        print("<head><title>SQL</title></head>")
        print("<body>")
        
        print("<table class='styled-table' border=1; style='background-color: #009879;'>")
        stCliente = datos.split("\n")
        i = 0
        
        self.header()
        while(i<len(stCliente)):
            cliente=stCliente[i]
            cliente = cliente.split("_")
            if (cliente[1]=="1"):
                estado="AB"
            else:
                estado="CE"
            VAL = ((cliente[2])[10:13])
            #print("FECHA: ",(cliente[2])[0:11])
            #print("RECIBIDO: ",F)
            if (HR!="" and F!=""):
                #print("HORA SQL: '"+str((cliente[2])[0:10])+"' <br>")
                #print("F: '"+str(F)+"' <br>")
                if((int(HR)==int(VAL)) and (str((cliente[2])[0:10]))==str(F) ):
                    print("ENTRA")
                    self.tablas(cliente[0],estado,(cliente[2])[0:11],(cliente[2])[10:])

            else:
                if (F!=""):
                    if (str((cliente[2])[0:10])==str(F)):
                        self.tablas(cliente[0],estado,(cliente[2])[0:11],(cliente[2])[10:])
                else:
                    if(int(HR)==int(VAL)):
                        self.tablas(cliente[0],estado,(cliente[2])[0:11],(cliente[2])[10:])
            i=i+1
        
        print("</body>")
        print("</html>")
    #

    def respuestaServer2(self, datos):
        print(libs)
        
        print("<html>")
        print("<head><title>SQL</title></head>")
        print("<body>")
       
        
        print("<table class='styled-table' border=1; style='background-color: #009879;'>")
        stCliente = datos.split("\n")
        i = 0
        self.header()
        while(i<len(stCliente)):
            cliente2=stCliente[i]
            cliente2 = cliente2.split(" ")
            
            self.tablas(cliente2[0],cliente2[1],(cliente2[2]),(cliente2[3]))
            i=i+1
        
        print("</body>")
        print("</html>")

    def respuestaServer3(self, datos):
        print(libs)
        print("Content-type: text/html\n\n")
        print("<html>")
        print("<head><title>SQL</title></head>")
        print("<body>")
        
        
        print("<table class='styled-table' border=1; style='background-color: #009879;'>")
        stCliente = datos.split("\n")
        i = 0
        self.header()
        while(i<len(stCliente)):
            cliente2=stCliente[i]
            cliente2 = cliente2.split(" ")
            try:
                if (HR!="" and F!=""):
                #print("HORA SQL: '"+str((cliente[2])[0:10])+"' <br>")
                #print("F: '"+str(F)+"' <br>")
                    if((int(HR)==int(VAL)) and str((cliente2[2]))==str(F) ):
                        self.tablas(cliente2[0],cliente2[1],(cliente2[2]),(cliente2[3]))
                else:
                    if (F!=""):
                        if (str((cliente2[2]))==str(F)==F):
                            self.tablas(cliente2[0],cliente2[1],(cliente2[2]),(cliente2[3]))
                    else:

                        if (((cliente2[3])[0:2])==HR):
                            self.tablas(cliente2[0],cliente2[1],(cliente2[2]),(cliente2[3]))
            except:
                pass
            i=i+1
        
        print("</body>")
        print("</html>")

        
    def procesarTransaccion(self):
        conexion = mysql.connector.connect(user="root", password="root", database="iot")
        
        if(B == "Consultar Valvula"):
            
            query = "SELECT * FROM Valvula WHERE id='"+V+"'"
            
            statement = conexion.cursor()
            statement.execute(query)
            
            
            datos=""
            st = datos.split("_")
            tupla = statement.fetchone()
            # while tupla is not None:
            while(tupla != None):
                ide=tupla[0]
                estado=tupla[1]
                fh=tupla[2]
                
                datos = datos + str(ide) +"_"+ str(estado) +"_"+ str(fh) + "\n"
                # print(tupla)
                tupla = statement.fetchone()
            
            
            statement.close()
            conexion.close
            
            if (HR!="" or F!=""):
                self.respuestaServer5(datos)
            else:
                self.respuestaServer1(datos)
   
            
        elif (B == "Consultar Temperatura"):
           
            query = "SELECT * FROM S_temperatura WHERE id='"+V+"'"
            
            statement = conexion.cursor()
            statement.execute(query)
            
            
            datos=""
            st = datos.split("_")
            tupla = statement.fetchone()
            # while tupla is not None:
            while(tupla != None):
                
                ide=tupla[0]
                estado=tupla[1]
                fh=tupla[2]
                
                datos = datos + str(ide) +" "+ str(estado) +" "+ str(fh) + "\n"
                # print(tupla)
                tupla = statement.fetchone()
            
            
            statement.close()
            conexion.close
            if (HR!="" or F!=""):
                self.respuestaServer3(datos)
            else:
                self.respuestaServer2(datos)

        elif (B == "Consultar Humedad"):
            
            query = "SELECT * FROM Humedad WHERE id='"+V+"'"
           
            statement = conexion.cursor()
            statement.execute(query)
            
            # Procesar los datos de la tabla resultante
            datos=""
            st = datos.split("_")
            tupla = statement.fetchone()
            # while tupla is not None:
            while(tupla != None):
                
                ide=tupla[0]
                estado=tupla[1]
                fh=tupla[2]
                
                datos = datos + str(ide) +" "+ str(estado) +" "+ str(fh) + "\n"
                # print(tupla)
                tupla = statement.fetchone()
            
           
            statement.close()
            conexion.close
            if (HR!="" or F!=""):
                self.respuestaServer3(datos)
            else:
                self.respuestaServer2(datos)

        elif (B == "Consultar Luminosidad"):
           
            query = "SELECT * FROM S_iluminacion WHERE id='"+V+"'"
            
            statement = conexion.cursor()
            statement.execute(query)
            
            # Procesar los datos de la tabla resultante
            datos=""
            st = datos.split("_")
            tupla = statement.fetchone()
            # while tupla is not None:
            while(tupla != None):
                
                ide=tupla[0]
                estado=tupla[1]
                fh=tupla[2]
                
                datos = datos + str(ide) +" "+ str(estado) +" "+ str(fh) + "\n"
                # print(tupla)
                tupla = statement.fetchone()
            
        
            statement.close()
            conexion.close
            if (HR!="" or F!=""):
                self.respuestaServer3(datos)
            else:
                self.respuestaServer2(datos)

        

# Crear el objeto de la clase Primero
HR= None
V = sys.argv[1]
HR = sys.argv[2]
F = sys.argv[3]
B = sys.argv[4]
libs= """
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
        <link rel="icon" href="images/favicon.ico">
        <link rel="shortcut icon" href="images/favicon.ico" />
        <link rel="stylesheet" href="css/owl.carousel.css">
        <link rel="stylesheet" href="css/style.css">
        <script src="js/jquery.js"></script>
        <script src="js/jquery-migrate-1.1.1.js"></script>
        <script src="js/script.js"></script>
        <script src="js/jquery.ui.totop.js"></script>
        <script src="js/superfish.js"></script>
        <script src="js/sForm.js"></script>
        <script src="js/jquery.equalheights.js"></script>

        <script src="js/jquery.easing.1.3.js"></script>
        <div class="content" >

        
        """

cliente = ClienteController()
cliente.procesarTransaccion()
