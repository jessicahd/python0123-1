import models.product as mp


def controllerProduct():
    tipo=mp.ModelProducto()
    data=tipo.getTipo()
    return data


def insertProduct(data):
    tipo=mp.ModelProducto()
    tipo.insertProducto(data)