from tkinter import *
from tkinter import messagebox
import os
import Table

traduccion =[["Modo Mantenimiento", "Maintenance Mode"], #0
               ["Cambiar el idioma", "Change language "],#1
               ["Ingresar", "Log in"],#2
               ["Administrador", "Administrator"],#3
               ["Contraseña", "  Password "],#4
               ["Administrar Aplicaciones", "    Administrate Apps    "],#5
               ["Administrar Vendedores", "    Administrate Sellers    "],#6
                ]
 
IDIOMA = 0
ESP = 0
ENG = 1

POS_ID_VENDEDOR = 0
POS_ID_PRODUCTO = 1
POS_CATEGORIA = 2
POS_DESCRIPCION = 3
POS_PRECIO = 4
POS_ESTADO = 5
POS_SCREENSHOT1 = 6
POS_SCREENSHOT2 = 7
POS_DOWNLOADS = 8
POS_DOWNLOADSCR = 9

POS_NOMBRE_VENDEDOR = 1
POS_ICORREO = 2 
POS_SITIOWEB = 2



def abrirArchivo(archivo, modo): #abre el archivo
    file = open(archivo, modo)
    return file
def separarVendedores(i): 
    if i == len(listaVendedores):
        return
    listaVendedores[i] = listaVendedores[i].replace("\n", "").split(";")
    separarVendedores(i + 1)
archivo = abrirArchivo("Vendedores.txt", "r")
listaVendedores = archivo.readlines() #lo convierte en una lista
separarVendedores(0) #llama la funcion separarVendedores
archivo.close

def separarApps(i):
    if i == len(listaApps):
        return
    listaApps[i] = listaApps[i].replace("\n", "").split(";")
    separarApps(i + 1)

archivo = abrirArchivo("Apps.txt", "r")
listaApps = archivo.readlines()
separarApps(0)
archivo.close

window = Tk()
window.title("Modo Mantenimiento")
window.minsize(400, 400)
window.maxsize(400, 400)


#funciones generales
def cargar_imagen(nombre): #Cargar imagenes
    ruta = os.path.join("imagenes", nombre)
    imagen = PhotoImage(file = ruta)
    return imagen

bgMante = cargar_imagen("VentanaMant.gif")
fondo1 = cargar_imagen("bg.gif")
fondoApps = cargar_imagen("bg2.gif")

def CambiarIdioma():
    global IDIOMA
    IDIOMA = 1 - IDIOMA
    window.title(traduccion[0][IDIOMA])
    CambiarIdioma.config(text=traduccion[1][IDIOMA])
    Ingresar.config(text=traduccion[2][IDIOMA])
    Ingresar1.config(text=traduccion[2][IDIOMA])
    lbNombreAdmin.config(text=traduccion[3][IDIOMA])
    lbContraseñaAdmin.config(text=traduccion[4][IDIOMA])



def iniciarSesion(): #permite "editar", o más bien escribir algo y añadirlo en el archivo de texto. Esto sucede al ejecutar el .bind
    nombreA = entradaNombreAdmin.get() #obtiene el texto escrito en la entrada
    contraA = entradaContraseñaAdmin.get()
    if nombreA != "" and contraA != "": #si la entrada del nombre no esta vacia
        if nombreA == "Jessica" and contraA == "Hello":
            def crearVentana(): #Abre una nueva ventana donde hay dos botones: Administrar Apps y Administrar Vendedores
                window.withdraw ( )
                vent = Toplevel ( )
                vent.title("Modo Mantenimiento")
                vent.minsize (500, 500)
                canvas1 = Canvas (vent, width = 800, height = 600)
                canvas1.place (x = -1, y = -1)
                fondo = Label(canvas1, image = bgMante)
                fondo.place(x = -1, y = -1)
                def CambiarIdioma():
                    global IDIOMA
                    IDIOMA = 1 - IDIOMA
                    botonApps.config(text=traduccion[5][IDIOMA])
                    botonApps1.config(text=traduccion[6][IDIOMA])
                CambiarIdioma = Button(vent, text=traduccion[1][IDIOMA], bg="white", fg="dark blue", font=("Arial", 10), command = CambiarIdioma)
                CambiarIdioma.place(x=55, y=10)
                def AdminApps():#abre otra ventana para administrar las aplicaciones
                    vent.withdraw ( )
                    VentApps = Toplevel ( )
                    VentApps.title("Administrar Aplicaciones")
                    VentApps.minsize(1350, 1000)
                    VentApps.maxsize(1350, 1000)
                    VentApps.geometry("1350x1000+0+0")
                    canvasApps = Canvas(VentApps, width= 1350, height = 1000, bg = "#001939")
                    canvasApps.place(x=-1, y=-1)
                    lbFondoApps = Label(VentApps, image = fondoApps)
                    lbFondoApps.place(x = -1, y = -1)
                    canvasApps1 = Canvas(VentApps, width= 1350, height = 300)
                    canvasApps1.place(x=-1, y=400)
                    def CambiarIdioma():
                        global IDIOMA
                        IDIOMA = 1 - IDIOMA
                        botonApps.config(text=traduccion[5][IDIOMA])
                        botonApps1.config(text=traduccion[6][IDIOMA])
                        titulos.config(text=traduccion[7][IDIOMA])
                    
                    def volver( ):
                        global tablaApps
                        tablaApps = []
                        VentApps.destroy ( )
                        vent.deiconify ( )
                    boton = Button (VentApps, text = "volver", font = ("arial", 12), width = 6, command = volver)
                    boton.place (x = 1200, y = 10)

                    titulos = Label(VentApps, text = traduccion[7][IDIOMA] , bg = "midnight blue", fg = "white")
                    titulos.place(x =0, y = 375)
                    lbListaApps = Label(VentApps, text = "Lista de Aplicaciones", bg = "midnight blue", fg = "white", font=("Helvetica", 20))
                    lbListaApps.place(x =100, y = 330)


                    CambiarIdioma = Button(VentApps, text=traduccion[1][IDIOMA], bg="white", fg="dark blue", font=("Arial", 10), command = CambiarIdioma)
                    CambiarIdioma.place(x=1050, y=10)
        
                botonApps = Button(canvas1, text = traduccion[5][IDIOMA], command = Table.mostrarApps, font = ("helvetica", 14))
                botonApps.place(x = 20, y = 170)
                botonApps1 = Button(canvas1, text = traduccion[6][IDIOMA], font = ("helvetica", 14), command = Table.mostrarVendedores)
                botonApps1.place(x = 260, y = 170)
                
            crearVentana()
        else:
            messagebox.showerror("Error en los datos","Usuario o contraseña incorrectos.")
    else:
        messagebox.showerror("Error en los datos","Escriba su nombre de usuario y contraseña.")


labelfondo = Label(window, image = fondo1)
labelfondo.place(x = -1, y = -1)
Ingresar = Button(window, text = traduccion[2][IDIOMA], command = iniciarSesion) #boton
Ingresar.place(x = 200, y = 140)
lbNombreAdmin = Label(window, text=traduccion[3][IDIOMA], bg = "white")
lbNombreAdmin.place(x= 50, y = 80)
entradaNombreAdmin = Entry(window)
entradaNombreAdmin.place(x= 150, y = 80)
lbContraseñaAdmin = Label(window, text=traduccion[4][IDIOMA], bg = "white")
lbContraseñaAdmin.place(x= 50, y = 110)
entradaContraseñaAdmin = Entry(window, show = "*")
entradaContraseñaAdmin.place(x= 150, y = 110)

def Vendedores(cont):
    global listaVendedores
    if cont == len(listaVendedores):
        messagebox.showerror("Error", "Vendedor no encontrado.")
    elif entryVend.get() != listaVendedores[cont][POS_NOMBRE_VENDEDOR]:
        Vendedores(cont + 1)
    else:
        ventanaConsulta(cont)
def ventanaConsulta(cont):
    global listaVendedores, listaApps
    ventC = Toplevel ( ) # es para crear una ventana secudaria
    ventC.title("Consulta")
    ventC.minsize (500, 500)
    canvas1 = Canvas (ventC, width = 500, height = 500, bg = "#001939")
    canvas1.place (x = -1, y = -1)

    Apps_en_venta = Label(canvas1, text = "Apps en venta:", bg = "#001939", fg = "white", font=("Helvetica", 10))
    Apps_en_venta.place(x=10, y=50)
    screenShot1 = cargar_imagen(listaApps[cont][POS_SCREENSHOT1])
    labelSS1 = Label(canvas1, image = screenShot1)
    labelSS1.image = screenShot1
    labelSS1.place(x=10, y=100)
    lbdescargas = Label(canvas1, text = "Descargas totales:", bg = "#001939", fg = "white")
    lbdescargas.place(x=230, y=140)
    descargas = Label(canvas1, text = listaApps[cont][POS_DOWNLOADS], bg = "#001939", fg = "white")
    descargas.place(x=400, y=140)
    lbdescargasCR = Label(canvas1, text = "Descargas en Costa Rica:", bg = "#001939", fg = "white")
    lbdescargasCR.place(x=230, y=160)
    descargasCR = Label(canvas1, text = listaApps[cont][POS_DOWNLOADSCR], bg = "#001939", fg = "white")
    descargasCR.place(x=400, y=160)

        
lbVend = Label(window, text = "Vendedor")
lbVend.place(x=60, y = 280)
entryVend = Entry(window)
entryVend.place(x = 150, y = 280)


Ingresar1 = Button(window, text = traduccion[2][IDIOMA], command =lambda: Vendedores(0)) #boton
Ingresar1.place(x = 200, y = 340)
lbNombreAdmin = Label(window, text = traduccion[3][IDIOMA], bg = "white")
lbNombreAdmin.place(x= 50, y = 80)
entradaNombreAdmin = Entry(window)
entradaNombreAdmin.place(x= 150, y = 80)
lbContraseñaAdmin = Label(window, text = "Contraseña", bg = "white")
lbContraseñaAdmin.place(x= 50, y = 110)
entradaContraseñaAdmin = Entry(window, show = "*")
entradaContraseñaAdmin.place(x= 150, y = 110)

CambiarIdioma = Button(window, text=traduccion[1][IDIOMA], bg="white", fg="dark blue", font=("Helvetica", 10), command = CambiarIdioma)
CambiarIdioma.place(x=155, y=10)




window.mainloop()
