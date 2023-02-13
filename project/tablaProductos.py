import pandas as pd
import datetime
import sqlite3
import controller as ctr
###Para ingresar los datos de los producto a la base de datos, se creo Productos.xlsx para extraer
###los datos correpondientes al del producto, se ejecuta el proceso en tablaProductos.py
###

df=pd.read_excel("project\Productos.xlsx",sheet_name="Sheet1",header=0)
#print(type(df))

lista_valores=df.values.tolist()

conn=sqlite3.connect('project/tienda.db')
cursor_obj = conn.cursor()

cursor_obj.executemany("INSERT INTO TABLE_PRODUCTOS (PRODUCT_ID,NAMEPRODUCT,NROSERIE,PRODUCT,PRICE_UNIT,CATEGORIA,STOCK_ACUTAL) VALUES(?,?,?,?,?,?,?)",lista_valores)
print("datos ingresados")
conn.commit()
conn.close()