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
    input_cols=[1,4,5,6]
    path='project'
    filename=input("Ingrese el nombre del archivo a leer (solo Productos)(.xlsx): ") + ".xlsx" ##se ingresa: Productos
    fullpath=os.path.join(path,filename)
    print("Se está leyendo el archivo "+ fullpath)
    archivoExcel=pd.read_excel(fullpath,sheet_name='Sheet1',usecols=input_cols)
    return archivoExcel
   

def agregarFiltros(archivoExcel):
    print("Agregando filtros... Mostrar información del stock que debe ser observado")
    archivoExcel=archivoExcel[archivoExcel["STOCK_ACUTAL"]<=50]
    return archivoExcel

def vista_data(archivoExcel):
    print(" Vista data ")
    df_cols = archivoExcel.columns
    for col in df_cols:
        print(archivoExcel[col])

def exportar_data(archivoExcel):    
    print("...Exportando data a excel...")
    archivoExcel.to_excel('project/reporteProductos.xlsx',header=True,index=False)

if __name__=="__main__":
    main()
    input("\rData exportada exitosamente")