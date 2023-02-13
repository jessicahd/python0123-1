import tkinter as tk              
from tkinter import font as tkfont 
import controller as ctr
from tkinter import *
import prueba as p
import prueba2 as p2

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        container = tk.Frame(self)
        self.geometry("400x500")
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (InitPage, Productos,Reporte):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("InitPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class InitPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title = tk.Label(self, text="Ingreso de productos", font=controller.title_font,bg="white")
        title.pack(fill=tk.BOTH,expand=True)
        productIDLabel = tk.Label(self, text="Id del producto")
        self.productID = tk.StringVar()
        productIDEntry = tk.Entry(self, textvariable=self.productID)
        productIDLabel.pack(side="top",padx=4,pady=4)
        productIDEntry.pack(side="top",padx=4,pady=4)

        self.nameProduct=tk.StringVar()
        nameProductLabel=tk.Label(self, text="Nombre del producto")
        nameProductEntry = tk.Entry(self, textvariable=self.nameProduct)
        nameProductLabel.pack(side="top",padx=4,pady=4)
        nameProductEntry.pack(side="top",padx=4,pady=4)

        self.numSerie=tk.StringVar()
        numSerieLabel=tk.Label(self, text="Número de serie")
        numSerieEntry = tk.Entry(self, textvariable=self.numSerie)
        numSerieLabel.pack(side="top",padx=4,pady=4)
        numSerieEntry.pack(side="top",padx=4,pady=4)

        self.Producto=tk.StringVar()
        ProductoLabel=tk.Label(self, text="Producto")
        ProductoEntry = tk.Entry(self, textvariable=self.Producto)
        ProductoLabel.pack(side="top",padx=4,pady=4)
        ProductoEntry.pack(side="top",padx=4,pady=4)

        self.precioUnitario=tk.StringVar()
        precioUnitarioLabel=tk.Label(self, text="Precio Unitario")
        precioUnitarioEntry = tk.Entry(self, textvariable=self.precioUnitario)
        precioUnitarioLabel.pack(side="top",padx=4,pady=4)
        precioUnitarioEntry.pack(side="top",padx=4,pady=4)

        self.categoria=tk.StringVar()
        categoriaLabel=tk.Label(self, text="Categoria")
        categoriaEntry = tk.Entry(self, textvariable=self.categoria)
        categoriaLabel.pack(side="top",padx=4,pady=4)
        categoriaEntry.pack(side="top",padx=4,pady=4)

        self.stockActual=tk.StringVar()
        stockActualLabel=tk.Label(self, text="Stock Actual")
        stockActualEntry = tk.Entry(self, textvariable=self.stockActual)
        stockActualLabel.pack(side="top",padx=4,pady=4)
        stockActualEntry.pack(side="top",padx=4,pady=4)

        ButtonSubmit=tk.Button(self, text="Guardar data",
                            command=self.mostrarDataProductos,bg = "green",
                                 fg = "white")
        ButtonSubmit.pack(side="top",padx=4,pady=4)

        buttonDashboard = tk.Button(self, text="Generar Reporte Productos",
                           command=lambda: controller.show_frame("Productos"),bg = "pink",
                                 fg = "black")
         
        buttonReport = tk.Button(self, text="  Generar Reporte Usuario2  ",
                           command=lambda: controller.show_frame("Reporte"),bg = "pink",
                                 fg = "black")
        buttonDashboard.pack(side=tk.LEFT)
        buttonReport.pack(side=tk.RIGHT)

        
    def mostrardata(self):
            data=(str(self.username),str(self.password),str(self.email),str(self.fullname),str(self.tipousuario))
            print(type(str(self.username)))
            try:
                ctr.insertUser(data)
            except Exception as e:
                print("error al ingresar data")
                print(e)
    def mostrarDataProductos(self):
            data=(str(self.productID),str(self.nameProduct),str(self.numSerie),str(self.Producto),str(self.precioUnitario),str(self.categoria),str(self.stockActual))
            print(type(str(self.productID)))
            try:
                ctr.insertProduct(data)
            except Exception as e:
                print("error al ingresar data")
                print(e)        

class Productos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Productos", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Volver",
                           command=lambda: controller.show_frame("InitPage"))
        button2 = tk.Button(self,text="Generar Reporte de Productos", command=self.generateReport)
        button.pack()
        button2.pack()
    def generateReport(self):
        print("...Generando...")
        p2.main()
        print("\rData exportada exitosamente")
        pass


class Reporte(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Reporte", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Volver",
                           command=lambda: controller.show_frame("InitPage"))
        button2 = tk.Button(self,text="Generar Reporte de Usuario2", command=self.generateReport)
        button.pack()
        button2.pack()
    def generateReport(self):
        print("...Generando...")
        p.main()
        print("\rData exportada exitosamente")

        pass

