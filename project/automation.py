import pandas as pd
import os
import db
import controller as ctr
import datetime
import requests as rq
import openpyxl
import prueba as p
"""
message=
    1)Insertar data:
    2)Actualizar data del dolar

print(message)
a=int(input('ingrese la tarea a realizar: '))


def insertData():
    #obtiene la ruta absoluta
    path_=os.getcwd()+'\dataTienda.csv'
    #conection a bd
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    print(path_)
    df = pd. read_csv (path_, sep = ";") 
    ### logica para insertar 
    for i,fila in df.iterrows():
        print(fila['ORDER_ID'])

def updateDolar():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    pass"""
#3. En el archivo automation.py deberá implementar el menú iterativo en el cual podrá insertar data y actualizar 

def insertarData():
    compra=input('ingrese el siguiente data compra: ')
    venta=input('ingrese el siguiente data venta: ')
    moneda=input('ingrese el siguiente data moneda: ')
    fecha=datetime.datetime.now()
    data=(compra,venta,moneda,fecha)
    try:
        ctr.insertTipo(data)
    except Exception as e:
         print("error al ingresar data")
         print(e)

def listTipo():
    print("Lista")
    data=ctr.controllerTipo()
    for row in data:
        print(row)

def actualizarTipo():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    data = rq.get(url)
    if data.status_code==200:
        print(data.json())
        data=data.json()
        dolar_compra = data['compra']
        dolar_venta = data['venta']
        dolar_moneda=data['moneda']
        fecha_actualizacion=datetime.datetime.now()
        data=(dolar_compra,dolar_venta,dolar_moneda,fecha_actualizacion)
        try:
            ctr.insertTipo(data)
        except Exception as e:
            print("error al ingresar data")
            print(e)
    else:
        print("error de api")

message="""
    1)Insertar data 
    2)Actualizar data
    3)Generar Reporte en excel
    4)Salir
    """
while True:
    print(message)
    op=input("Elija una de las siguientes opciones: ")
    if op =='1':
        insertarData()
        listTipo()
    elif op =='2':
        actualizarTipo()
        listTipo()
    elif op =='3':
        p.main()
        print("\rData exportada exitosamente")
    elif op=='4':
        print("¡Hasta luego! Ha sido un placer asistirte")
        break
    else:
        print("Ingrese una opción válida")

