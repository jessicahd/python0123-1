import models.tipoCambio as mt


def controllerTipo():
    tipo=mt.ModelTipo()
    data=tipo.getTipo()
    return data


def insertTipo(data):
    tipo=mt.ModelTipo()
    tipo.insertTipo(data)
    
