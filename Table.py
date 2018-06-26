from tkinter import *
from tkinter import messagebox
import os

ROWS = 1
COLUMNS = 10
# Tabla donde se guardan los datos
TablaApps = []
# Lista de usuarios registrados
apps = []

def mostrarApps():
    # Constante para el nombre del archivo
    FILENAME = os.path.join("Apps.txt")
    # Constantes para las posiciones en la tabla
    POS_IDVENDEDOR = 0
    POS_IDPRODUCTO = 1
    POS_CATEGORIA = 2
    POS_DESCRIPCION = 3
    POS_PRECIO = 4
    POS_ESTADO = 5
    POS_SS1 = 6
    POS_SS2 = 7
    POS_DL = 8
    POS_DLCR = 9
    # Valores para la cantidad de filas y columnas de la tabla

    # Crear la ventana
    mainwindow = Tk()
    mainwindow.title("Aplicaciones")
    mainwindow.minsize(1350, 800)
    canvasApps1 = Canvas(mainwindow, width= 1350, height = 300)#canvas para la tabla
    canvasApps1.place(x=-1, y=600)


    # Etiqueta titulo
    lbTitle = Label(mainwindow, text="Tabla de aplicaciones", bg="midnight blue", fg="#EFEFFB",
                       font=("Helvetica", 23), justify=CENTER, width=76)
    lbTitle.place(x=0, y=360)

    # Canvas para la tabla
    canvasTabla = Canvas(mainwindow)
    canvasTabla.place(x=0, y=400)
    def volver( ):
        mainwindow.destroy ( )
    boton = Button (mainwindow, text = "volver", font = ("Helvetica", 12), width = 6, command = volver)
    boton.place (x = 1200, y = 10)

    def limpiarTabla(): #elimina todos los entries creados para hacer nuevos
        global TablaApps
        if TablaApps == []: #ya se borro todo lo que habia en la tabla
            print('Tabla:', TablaApps)
            return None
        elif TablaApps[-1] == []:#-1 va de atras para adelante #el ultimo elemento de la tabla esta vacio
            TablaApps.pop() #.pop elimina el ultimo elemento de la lista y lo retorna #como una palomita
            return limpiarTabla()
        item = TablaApps[-1].pop() #pop es el ultimo elemento y Tabla[-1] es la ultima lista
        del item #destruye de la memoria el entry
        return limpiarTabla()

    def createTabla(i, j, rows):
        global TablaApps
        if i == ROWS:
            print("Tabla:",TablaApps)
            return None
        elif j == COLUMNS:
            TablaApps += [rows] #se agrega la fila * a la tabla
            return createTabla(i + 1, 0, []) #[] porque se va a volver a llenar
        item = Entry(canvasTabla, text="", justify=CENTER, width = 22)
        item.grid(row=i, column=j)
        return createTabla(i,  j + 1, rows + [item]) #se van llenando las columnas de la fila = *

    def createHeader():
        global TablaApps
        TablaApps[0][POS_IDVENDEDOR].insert(0, "IDVENDEDOR")
        TablaApps[0][POS_IDPRODUCTO].insert(0, "IDPRODUCTO")
        TablaApps[0][POS_CATEGORIA].insert(0, "CATEGORIA")
        TablaApps[0][POS_DESCRIPCION].insert(0, "DESCRIPCION")
        TablaApps[0][POS_PRECIO].insert(0, "PRECIO")
        TablaApps[0][POS_ESTADO].insert(0, "ESTADO")
        TablaApps[0][POS_SS1].insert(0, "SS1")        
        TablaApps[0][POS_SS2].insert(0, "SS2")
        TablaApps[0][POS_DL].insert(0, "DL")
        TablaApps[0][POS_DLCR].insert(0, "DLCR")
        
    def disableEdition(i, j):
        global TablaApps
        if i == ROWS:
            return None
        elif j == COLUMNS:
            return disableEdition(i + 1, 0)
        TablaApps[i][j].config(state=DISABLED)
        return disableEdition(i,  j + 1)

    def fillTabla(i, j):
        global TablaApps, apps
        if i == ROWS - 1 or apps == []:
            return None
        elif j == COLUMNS:
            return fillTabla(i + 1, 0)
        TablaApps[i+1][j].insert(0, apps[i][j])
        TablaApps[i+1][j].config(state=DISABLED)
        return fillTabla(i, j + 1)

    def splitapps(i):
        global apps
        if i == len(apps):
            return
        apps[i] = apps[i].replace("\n", "").split(";")
        splitapps(i + 1)

    def update(event):
        global apps, ROWS
        limpiarTabla()
        if os.path.isfile(FILENAME):
            file = open(FILENAME, 'r')
            apps = file.readlines()
            splitapps(0)
            ROWS = len(apps) + 1
            file.close()
        createTabla(0, 0, [])
        createHeader()
        fillTabla(0, 0)
        disableEdition(0, 0)

    update(None)
    
    def agregarAplicacion(): #permite "editar", o más bien escribir algo y añadirlo en el archivo de texto. Esto sucede al ejecutar el .bind
        ID_Producto = entradaID_Producto.get() #obtiene el texto escrito en la entrada
        Categoria = entradaCategoria.get()
        Descripcion = entradaDescripcion.get()
        Precio = entradaPrecio.get()
        SS1 = entradaSS1.get()
        SS2 = entradaSS2.get()
        if ID_Producto != "" and Categoria != "" and Descripcion != "" and Precio != "" and SS1 != "" and SS2 != "" : #si las entradas no estan vacias
            if Categoria == "0" or "1" or "2" or "3" or "4":
                with open("Apps.txt", "r") as file: #abre el archivo "Apps.txt", en modo leer, como "file"
                    largo = len(file.readlines()) #"largo" es la longitud de la lista
                agregar = open("Apps.txt", "a")
                agregar.write(str(largo + 1) + ";" + ID_Producto + ";" + Categoria + ";" + Descripcion + ";" + Precio + "$" + ";"  +  SS1 + ";" + SS2 + "0" + "0" + "\n") #el largo de la lista mas uno (esto es para autoasignarle un ID a el nuevo vendedor) y mas los datos
                agregar.close()
                messagebox.showinfo("Listo", "Aplicacion Añadida. Presione F5 para actualizar la tabla.")

            else:
                messagebox.showerror("Error en los datos", "Tome en cuenta la lista de categorias.")
        else:
            messagebox.showerror("Error en los datos", "Debe llenar todos los campos solicitados.")  
    
    labelAgregarApp = Label(mainwindow, text = "Agregar Aplicacion", bg = "midnight blue", fg = "white", font=("Helvetica", 20))
    labelAgregarApp.place(x = 30, y = 10)
    labelID_Producto = Label(mainwindow, text = "ID Producto", font = ("arial", 12), bg = "midnight blue", fg = "white")
    labelID_Producto.place (x = 105, y = 50)
    entradaID_Producto = Entry (mainwindow, font = ("arial", 12), width = 25, bg = "white")
    entradaID_Producto.place (x = 30, y = 80)
    labelCategoria = Label(mainwindow, text = "Categoria", font = ("arial", 12), bg = "midnight blue", fg = "white")
    labelCategoria.place (x = 105, y = 110)
    entradaCategoria = Entry (mainwindow, font = ("arial", 12), width = 25, bg = "white")
    entradaCategoria.place (x = 30, y = 140)
    labelDescripcion = Label(mainwindow, text = "Nombre, descripcion", font = ("arial", 12), bg = "midnight blue", fg = "white")
    labelDescripcion.place (x = 75, y = 170)
    entradaDescripcion = Entry (mainwindow, font = ("arial", 12), width = 25, bg = "white")
    entradaDescripcion.place (x = 30, y = 200)
    labelPrecio = Label(mainwindow, text = "Precio", font = ("arial", 12), bg = "midnight blue", fg = "white")
    labelPrecio.place (x = 115, y = 230)
    entradaPrecio = Entry (mainwindow, font = ("arial", 12), width = 25, bg = "white")
    entradaPrecio.place (x = 30, y = 260)
    labelSS1 = Label(mainwindow, text = "Screenshot 1 \n (debe estar en formato .gif)", font = ("arial", 12), bg = "midnight blue", fg = "white")
    labelSS1.place (x = 280, y = 45)
    entradaSS1 = Entry (mainwindow, font = ("arial", 12), width = 25, bg = "white")
    entradaSS1.place (x = 270, y = 90)
    labelSS2 = Label(mainwindow, text = "Screenshot 1 \n (debe estar en formato .gif)", font = ("arial", 12), bg = "midnight blue", fg = "white")
    labelSS2.place (x = 280, y = 115)
    entradaSS2 = Entry (mainwindow, font = ("arial", 12), width = 25, bg = "white")
    entradaSS2.place (x = 270, y = 160)

    botonAgregarApp = Button(mainwindow, text = "Agregar Aplicación", command = agregarAplicacion)
    botonAgregarApp.place(x = 330, y = 230)

    #CambiarIdioma = Button(mainwindow, text=traduccion[1][IDIOMA], bg="white", fg="dark blue", font=("Arial", 10), command = CambiarIdioma)
    #CambiarIdioma.place(x=1050, y=10)



    # Comando para actualizar la tabla
    mainwindow.bind("<F5>", update)

#############################################################################
ROWS_VENDEDORES = 1
COLUMNS_VENDEDORES = 4

# Tabla donde se guardan los datos
TablaVendedores = []
# Lista de usuarios registrados
vendedores = []
apps = []
    
def mostrarVendedores():
    # Constante para el nombre del archivo
    FILENAME = os.path.join("Vendedores.txt") #Obtiene la ruta completa del archivo
    # Constantes para las posiciones en la tabla
    POS_IDVENDEDOR = 0
    POS_NOMBRE = 1
    POS_CORREO = 2
    POS_SITIO_WEB = 3

    # Valores para la cantidad de filas y columnas de la tabla

    # Crear la ventana
    mainwindow = Tk()
    mainwindow.title("Vendedores")
    mainwindow.config(width=544, height=700, bg="#045FB4")
    mainwindow.resizable(width=False, height=False)
    """
    # Poner la ventana en el centro de la pantalla
    mainwindow.update_idletasks()
    width = mainwindow.winfo_width()
    height = mainwindow.winfo_height()
    x = (mainwindow.winfo_screenwidth() // 2) - (width // 2)
    y = (mainwindow.winfo_screenheight() // 2) - (height // 2)
    mainwindow.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    """
    # Etiqueta titulo
    lbTitle = Label(mainwindow, text="Tabla de vendedores", bg="#045FB4", fg="#EFEFFB",
                       font=("Helvetica", 23), justify=CENTER, width=30)
    lbTitle.place(x=0, y=300)

    # Canvas para la tabla
    canvasTabla = Canvas(mainwindow)
    canvasTabla.place(x=0, y=350)
    def volver( ):
        mainwindow.destroy ( )
    boton = Button (mainwindow, text = "Listo", font = ("Helvetica", 12), width = 6, command = volver)
    boton.place (x = 450, y = 10)

    def limpiarTabla(): #elimina todos los entries creados para hacer nuevos
        global TablaVendedores
        if TablaVendedores == []: #ya se borro todo lo que habia en la tabla
            return None
        elif TablaVendedores[-1] == []:#-1 va de atras para adelante #el ultimo elemento de la tabla esta vacio
            TablaVendedores.pop() #.pop elimina el ultimo elemento de la lista y lo retorna #como una palomita
            return limpiarTabla()
        item = TablaVendedores[-1].pop() #pop es el ultimo elemento y Tabla[-1] es la ultima lista
        del item #destruye de la memoria el entry
        return limpiarTabla()
    
    def createTabla(i, j, rows):
        global TablaVendedores
        if i == ROWS_VENDEDORES:
            return None
        elif j == COLUMNS_VENDEDORES:
            TablaVendedores += [rows]
            return createTabla(i + 1, 0, [])
        item = Entry(canvasTabla, text="", justify=CENTER, width = 22)
        item.grid(row=i, column=j)
        return createTabla(i,  j + 1, rows + [item])

    def crearEncabezado():
        global TablaVendedores
        TablaVendedores[0][POS_IDVENDEDOR].insert(0, "IDVENDEDOR")
        TablaVendedores[0][POS_NOMBRE].insert(0, "NOMBRE")
        TablaVendedores[0][POS_CORREO].insert(0, "CORREO")
        TablaVendedores[0][POS_SITIO_WEB].insert(0, "SITIO WEB")

        """
    def disableEdition(i, j):
        global TablaVendedores
        if i == ROWS_VENDEDORES:
            return None
        elif j == COLUMNS_VENDEDORES:
            return disableEdition(i + 1, 0)
        TablaVendedores[i][j].config(state=DISABLED)
        return disableEdition(i,  j + 1)
        """
    def fillTabla(i, j):
        global TablaVendedores, vendedores
        if i == ROWS_VENDEDORES - 1 or vendedores == []:
            return None
        elif j == COLUMNS_VENDEDORES:
            return fillTabla(i + 1, 0)
        TablaVendedores[i+1][j].insert(0, vendedores[i][j])
        TablaVendedores[i+1][j].config(state=DISABLED)
        return fillTabla(i, j + 1)

    def splitVendedores(i):
        global vendedores
        if i == len(vendedores):
            return
        vendedores[i] = vendedores[i].replace("\n", "").split(";")
        splitVendedores(i + 1)
        
    def openFile(archivo, modo): #abre el archivo
        file = open(archivo, modo)
        return file
    
    archivo = openFile("Vendedores.txt", "r")
    vendedores = archivo.readlines()

    def update(event):
        global vendedores, ROWS_VENDEDORES, TablaApps
        print("\nActualizar")
        limpiarTabla()
        print('Limpia:', TablaApps)
        if os.path.isfile(FILENAME): #verifica que sea un archivo
            file = open(FILENAME, 'r') #abre el archivo en modo lectura(no es directamente editable)
            vendedores = file.readlines() #lo convierte en una lista 
            splitVendedores(0)
            print('Sellers:', vendedores)
            ROWS_VENDEDORES = len(vendedores) + 1 #cantidad de filas para la tabla
            print("Filas: ", ROWS_VENDEDORES)
            file.close()
        print("Creando")
        createTabla(0, 0, [])
        crearEncabezado()
        print('Lllenar tabla')
        fillTabla(0, 0)
        #disableEdition(0, 0)

    update(None)

    def AgregarVendedor(): #permite "editar", o más bien escribir algo y añadirlo en el archivo de texto. Esto sucede al ejecutar el .bind
        nombreV = entradaNombre.get() #obtiene el texto escrito en la entrada
        correoV = entradaCorreo.get()
        SitioV = entradaSitioWeb.get()
        if nombreV != "" and correoV != "": #si las entradas no estan vacias
            if SitioV != "" or SitioV == "vacio":
                with open("Vendedores.txt", "r") as file: #abre el archivo "Vendedores.txt", en modo leer, como "file"
                    largo = len(file.readlines()) #"largo" es la longitud de la lista
                agregar = open("Vendedores.txt", "a")
                agregar.write(str(largo + 1) + ";" + nombreV + ";" + correoV + ";" + SitioV + "\n") #el largo de la lista mas uno (esto es para autoasignarle un ID a el nuevo vendedor)
                agregar.close()
                messagebox.showinfo("Listo", "Vendedor Añadido, presione F5 para actualizar la tabla.")

            else:
                messagebox.showerror("Error en los datos", "Escriba un sitio web. Si no tiene sitio web escriba lo siguiente: vacio")
        else:
            messagebox.showerror("Error en los datos", "Escriba su nombre y su correo.")  

    añadirVendedor = Button(mainwindow, text = "Agregar Vendedor", command = AgregarVendedor)
    añadirVendedor.place(x = 60, y = 260)

    lbModo = Label(mainwindow, text="Añadir Vendedor", font=("Helvetica", 18), bg = "white", fg="dark blue")
    lbModo.place(x=1, y=30)

    labelNombre = Label(mainwindow, text = "Nombre", font = ("Helvetica", 12), bg = "white", fg = "dark blue", width = 19)
    labelNombre.place (x = 15, y = 85)
    entradaNombre = Entry(mainwindow, width = 30)
    entradaNombre.place(x=10, y=115)
    labelCorreo = Label(mainwindow, text = "Correo", font = ("Helvetica", 12), bg = "white", fg = "dark blue", width = 19)
    labelCorreo.place (x = 15, y = 145)
    entradaCorreo = Entry(mainwindow, width = 30)
    entradaCorreo.place(x=10, y=175)
    labelSitioWeb = Label(mainwindow, text = "Sitio Web", font = ("Helvetica", 12), bg = "white", fg = "dark blue", width = 19)
    labelSitioWeb.place (x = 15, y = 205)
    entradaSitioWeb = Entry(mainwindow, width = 30)
    entradaSitioWeb.place(x=10, y=235)

    update(None)
    print (vendedores)

    def splitapps(i):
        global apps
        if i == len(apps):
            return
        apps[i] = apps[i].replace("\n", "").split(";")
        splitapps(i + 1)


    archivo2 = openFile("Apps.txt", "r")
    apps = archivo2.readlines()





    # Comando para actualizar la tabla
    mainwindow.bind("<F5>", update)


    #entrada para eliminar vendedor
    entradaIDVendedor = Entry(mainwindow, width = 30)
    entradaIDVendedor.place(x=210, y=115)
    ID = entradaIDVendedor.get()
    def eliminarVendedor(cont, i): #dos contadores
        global apps, ID, ROWS_VENDEDORES
        ID = entradaIDVendedor.get()
        with open("Vendedores.txt", "r") as ArchivoVendedores: #abre el archivo "Vendedores.txt", en modo leer, como "file"
            largo = len(ArchivoVendedores.readlines())
        if ID != ""  and ID <= str(largo): #si la entrada no está vacia y el ID es válido
            ver = open("Apps.txt", "r")
            apps = ver.readlines()
            ver.close()
            apps.pop(int(ID) - 1)
            eliminar = open("Apps.txt", "w")
            eliminar.write("\n".join(apps))    
            eliminar.close()
            ver2 = open("Vendedores.txt", "r")
            vendedores = ver2.readlines()
            ver2.close()
            vendedores.pop(int(ID) - 1)
            eliminar2 = open("Vendedores.txt", "w")
            eliminar2.write("".join(vendedores))
            eliminar2.close()
            messagebox.showinfo("Listo", "Vendedor Eliminado. Presione F5 para refrescar la lista.")
            update(None) #cuando termine de eliminar vendedores que me llame update para que de una vez se actualice
        else:
            messagebox.showerror("Error en los datos", "Escriba un ID valido.")
        

    EliminarVendedor = Button(mainwindow, text = "Eliminar Vendedor", command = lambda:eliminarVendedor(0,0))
    EliminarVendedor.place(x = 260, y = 145)

    lbModo1 = Label(mainwindow, text="Eliminar Vendedor", font=("Helvetica", 18), bg = "white", fg="dark blue")
    lbModo1.place(x=210, y=30)
    labelIDVendedor = Label(mainwindow, text = "ID del Vendedor", font = ("Helvetica", 12), bg = "white", fg = "dark blue", width = 19)
    labelIDVendedor.place (x = 215, y = 85)

    
            


