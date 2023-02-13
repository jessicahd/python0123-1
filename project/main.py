import controller as ctr

message="""
    1)Insertar un usuario
    2)ver lista de usuarios
    3)Ingresar producto
    4)ver lista de productos
"""
global option
option=input('ingrese una opcion: ')

def registerUser():
    usuario=input('ingrese el siguiente data usuario: ')
    password=input('ingrese el siguiente data password: ')
    email=input('ingrese el siguiente data email: ')
    fullname=input('ingrese el siguiente data fullname: ')
    score=input('ingrese el siguiente data score: ')
    tipousuario=input('ingrese el siguiente data tipousuario: ')
    data=(usuario,password,email,fullname,score,tipousuario)
    try:
        ctr.insertUser(data)
    except Exception as e:
         print("error al ingresar data")
         print(e)

def listUser():
    print("Lista")
    data=ctr.controllerUser()
    for row in data:
        print(row)

def registerProduct():
    productid=input('ingrese el siguiente data PRODUCT_ID: ')
    name=input('ingrese el siguiente data NAMEPRODUCT: ')
    nroserie=input('ingrese el siguiente data NROSERIE: ')
    product=input('ingrese el siguiente data PRODUCT : ')
    price_unit=input('ingrese el siguiente data PRICE_UNIT: ')
    categoria=input('ingrese el siguiente data CATEGORIA: ')
    stockActual=input('ingrese el siguiente data STOCK_ACUTAL: ')    
    data=(productid,name,nroserie,product,price_unit,categoria,stockActual)
    try:
        ctr.insertProduct(data)
    except Exception as e:
         print("error al ingresar data")
         print(e)

def listProduct():
    print("Lista")
    data=ctr.controllerProduct()
    for row in data:
        print(row)

if __name__=='__main__':
    if option=='1':
        registerUser()
    elif option=='2':
        listUser()
    elif option=='3':
        registerProduct()
    elif option=='4':
        listProduct()
    else:
        print("error")


