import pandas as pd
import datetime
import sqlite3
import controller as ctr

df=pd.read_excel("project\Productos.xlsx",sheet_name="Sheet1",header=0)
#print(type(df))

lista_valores=df.values.tolist()
#print(type(lista_valores))
#print(lista_valores['*'][7])
#k=datetime.strptime(lista_valores['CREACTION_PRODUCT'],'YYYY-MM-DD hh:mm:ss')
#print(type(k))

conn=sqlite3.connect('project/tienda.db')
cursor_obj = conn.cursor()
#cursor_obj.execute("DROP TABLE TABLE_PRODUCTOS")
#print("tabla borrada")
cursor_obj.executemany("INSERT INTO TABLE_PRODUCTOS (PRODUCT_ID,NAMEPRODUCT,NROSERIE,PRODUCT,PRICE_UNIT,CATEGORIA,STOCK_ACUTAL) VALUES(?,?,?,?,?,?,?)",lista_valores)
print("datos ingresados")
conn.commit()
conn.close()