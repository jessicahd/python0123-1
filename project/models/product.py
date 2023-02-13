import db
import pandas as pd

class ModelProducto():
    def __init__(self):
        self.db=db.Conection('project/tienda.db')
    def getTipo(self):
        cursor=self.db.getCursor()
        data=cursor.execute('select * from TABLE_PRODUCTOS').fetchall()
        return data
    def insertProducto(self,data):
        inserSentence="INSERT INTO TABLE_PRODUCTOS (PRODUCT_ID,NAMEPRODUCT,NROSERIE,PRODUCT,PRICE_UNIT,CATEGORIA,STOCK_ACUTAL) VALUES(?,?,?,?,?,?,?)"
        cursor=self.db.getCursor()
        cursor.execute(inserSentence,data)
        self.db.con.commit()
        print('data insertada')
