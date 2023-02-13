import db

class ModelTipo():
    def __init__(self):
        self.db=db.Conection('project/tienda.db')
    def getTipo(self):
        cursor=self.db.getCursor()
        data=cursor.execute('select * from TASA_CAMBIOS').fetchall()
        return data
    def insertTipo(self,data):
        inserSentence="INSERT INTO TASA_CAMBIOS (COMPRA,VENTA,MONEDA,FECHA_CAMBIO) VALUES(?,?,?,?)"
        cursor=self.db.getCursor()
        cursor.execute(inserSentence,data)
        self.db.con.commit()
        print('data insertada')
