import db

class ModelUser():
    def __init__(self):
        print('model user')
        self.db=db.Conection('project/tienda.db')
    def getUser(self):
        cursor=self.db.getCursor()
        data=cursor.execute('select * from USUARIOS').fetchall()
        return data
    def insertUser(self,data):
        inserSentence="INSERT INTO USUARIOS (USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES(?,?,?,?,?,?)"
        cursor=self.db.getCursor()
        cursor.execute(inserSentence,data)
        self.db.con.commit()
        print('data insertada')

