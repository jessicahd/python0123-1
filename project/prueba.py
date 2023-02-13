import pandas as pd
import openpyxl as op
import os

def main():
    archivoExcel=leer_archivos()
    archivoExcel=agregarFiltros(archivoExcel)
    vista_data(archivoExcel)
    exportar_data(archivoExcel)

def leer_archivos():
    print("Leyendo archivos")
    input_cols=[0,5,7,8,12]
    path='project'
    filename=input("Ingrese el nombre del archivo a leer: ") + ".csv" #dataTienda
    fullpath=os.path.join(path,filename)
    print("Se está leyendo el archivo "+ fullpath)
    archivoExcel=pd.read_csv(fullpath,header=0,delimiter=';',usecols=input_cols)
    return archivoExcel
    #print(archivoExcel)

def agregarFiltros(archivoExcel):
    print("Agregando filtros... Mostrar información del usuario USER2")
    archivoExcel=archivoExcel[archivoExcel["USER_CLIENT"]=="USER2"]
    return archivoExcel

def vista_data(archivoExcel):
    print(" Vista data ")
    df_cols = archivoExcel.columns
    for col in df_cols:
        print(archivoExcel[col])

def exportar_data(archivoExcel):    
    print("...Exportando data a excel...")
    archivoExcel.to_excel('project/reporte.xlsx',header=True,index=False)

if __name__=="__main__":
    main()
    input("\rData exportada exitosamente")
